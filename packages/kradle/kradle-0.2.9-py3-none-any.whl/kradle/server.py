from flask import Flask, jsonify, request
import threading
import socket
from werkzeug.serving import make_server
import signal
from flask_cors import CORS
import logging
from kradle.models import Observation
from kradle.logger import KradleLogger
from dataclasses import dataclass
import requests
from dotenv import load_dotenv
import os
from kradle.ssh_tunnel import create_tunnel
from kradle.args import KradleArgumentParser
from typing import Optional, Union, List, Dict, Any
import sys
from kradle.hotreload import setup_hot_reload
import kradle.utils as utils

load_dotenv()

@dataclass
class AgentConfig:
    participant_id: str
    session_id: str
    task: str
    agent_modes: list
    commands: list
    js_functions: list
    available_events: list

class Kradle:
    _instance = None
    _server = None
    _server_ready = threading.Event()
    _shutdown_event = threading.Event()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Kradle, cls).__new__(cls)
            cls._instance._agents = {}  # participant_id -> agent instance
            cls._instance._agent_classes = {}  # slug -> {class: agent_class, count: int}
            cls._instance._app = None
            cls._instance.port = None
            cls._instance._server_thread = None
            cls._instance._main_thread = None
            cls._instance._logger = KradleLogger()
        return cls._instance

    def _is_port_available(self, port, host='localhost'):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                return True
        except OSError:
            return False

    def _find_free_port(self, start_port=1500, end_port=1549):
        for port in range(start_port, end_port + 1):
            if self._is_port_available(port):
                return port
        raise RuntimeError(f"No free ports available in range {start_port}-{end_port}")

    def _get_or_create_agent(self, participant_id, slug):
        if participant_id in self._agents:
            return self._agents[participant_id]

        if slug is None:
            if not self._agent_classes:
                raise ValueError("No agent classes registered")
            slug = next(iter(self._agent_classes))

        if slug in self._agent_classes:
            agent_class = self._agent_classes[slug]['class']
        else:        
            if "*" in self._agent_classes:
                agent_class = self._agent_classes["*"]['class']
            else:
                raise ValueError(f"No agent class registered for slug: {slug}, no catch-all agent found")
        
        agent = agent_class(slug=slug)
        agent.participant_id = participant_id
        self._agents[participant_id] = agent
            
        return self._agents[participant_id]

    def _get_instance_counts(self, slug=None):
        if slug:
            if slug not in self._agent_classes:
                return None
            class_name = self._agent_classes[slug]['class'].__name__
            count = self._agent_classes[slug]['count']
            return {'class_name': class_name, 'instances': count}
            
        counts = {}
        for slug, info in self._agent_classes.items():
            counts[slug] = {
                'class_name': info['class'].__name__,
                'instances': info['count']
            }
        return counts

    def _create_app(self):
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['ENV'] = 'development'
        CORS(app)

        @app.after_request
        def after_request(response):
            self._logger.log_api_call(
                request.method,
                request.path,
                response.status_code
            )
            return response

        @app.route('/')
        def index():
            base_url = f"http://localhost:{self.port}"
            response = {
                'status': 'online',
                'agents': {},
            }
            
            for slug in self._agent_classes.keys():
                agent_urls = {
                    'base': f"{base_url}/{slug}",
                    'ping': f"{base_url}/{slug}/ping",
                    'init': f"{base_url}/{slug}/init",
                    'event': f"{base_url}/{slug}/event"
                }
                response['agents'][slug] = agent_urls
                
            return jsonify(response)

        @app.route('/<slug>')
        def agent_index(slug):
            if slug not in self._agent_classes:
                return '', 404
                
            base_url = f"http://localhost:{self.port}/{slug}"
            stats = self._get_instance_counts(slug)
            
            return jsonify({
                'status': 'online',
                'class_name': stats['class_name'],
                'instances': stats['instances'],
                'urls': {
                    'ping': f"{base_url}/ping",
                    'init': f"{base_url}/init",
                    'event': f"{base_url}/event"
                }
            })

        @app.route('/ping', defaults={'slug': None})
        @app.route('/<slug>/ping')
        def ping(slug):
            if slug:
                if slug not in self._agent_classes:
                    return '', 404
                stats = self._get_instance_counts(slug)
                return jsonify({
                    'status': 'online',
                    'class_name': stats['class_name'],
                    'instances': stats['instances']
                })

            return jsonify({
                'status': 'online',
                'agents': self._get_instance_counts()
            })

        @app.route('/init', defaults={'slug': None}, methods=['POST'])
        @app.route('/<slug>/init', methods=['POST'])
        def init(slug):
            data = request.get_json() or {}
            participant_id = data.get('participantId')

            if participant_id is None:
                self._logger.log_error("Missing participantId in init request")
                return jsonify({'error': 'participantId is required'}), 400

            try:
                agent = self._get_or_create_agent(participant_id, slug)
                agent_config = AgentConfig(
                    participant_id=participant_id,
                    session_id=data.get('sessionId'),
                    task=data.get('task'),
                    agent_modes=data.get('agent_modes'),
                    commands=data.get('commands'),
                    js_functions=data.get('js_functions'),
                    available_events=data.get('available_events')
                )
                init_data = agent.initialize_agent(agent_config)
                self._logger.log_success(f"Agent initialized for participant {participant_id}")
                return jsonify({'choices': init_data})
            except ValueError as e:
                self._logger.log_error(f"Failed to initialize agent: {str(e)}")
                return jsonify({'error': str(e)}), 400

        @app.route('/event', defaults={'slug': None}, methods=['POST'])
        @app.route('/<slug>/event', methods=['POST'])
        def event(slug):
            data = request.get_json() or {}
            observation = Observation.from_event(data)
            participant_id = data.get('participantId')
            
            if participant_id is None:
                self._logger.log_error("Missing participantId in event request")
                return jsonify({'error': 'participantId is required'}), 400

            try:
                agent = self._get_or_create_agent(participant_id, slug)
                result = agent.on_event(observation)
                return jsonify(result)
            except ValueError as e:
                self._logger.log_error("Error in event handler", e)
                return jsonify({'error': str(e)}), 400
            
        return app

    def _run_server(self):
        try:
            self._server = make_server('0.0.0.0', self.port, self._app)
            self._server_ready.set()
            self._server.serve_forever()
        except Exception as e:
            self._logger.log_error("Server crashed", e)
            self._shutdown_event.set()
            raise e
            
    def _setup_signal_handlers(self):
        def handle_shutdown(signum, frame):
            self._logger.on_shutdown()
            self._shutdown_event.set()
            if self._server:
                self._server.shutdown()
        
        signal.signal(signal.SIGINT, handle_shutdown)
        signal.signal(signal.SIGTERM, handle_shutdown)

    @classmethod
    def set_api_key(cls, api_key):
        instance = cls()
        instance._api_key = api_key
        if instance._api_key:
            instance._logger.log_info("API key found")
        else:
            instance._logger.log_error("API key not found")

    def _get_app_url(self):
        """Get the base URL for the Kradle application.
        
        Returns:
            str: The base URL for the Kradle application
        """
        return (
            "http://localhost:3000" 
            if os.getenv("KRADLE_DEV") 
            else "https://dev.kradle.ai"
    )
    
    @classmethod
    def register_agent(cls, slug, url):
        if not slug or slug == "*":
            return False

        instance = cls()
        KRADLE_APP_URL = (
            "http://localhost:3000" 
            if os.getenv("KRADLE_DEV") 
            else "https://app.kradle.ai"
        )

        try:
            response = requests.post(
                f'{KRADLE_APP_URL}/api/setAgentUrl',
                headers={
                    'Content-Type': 'application/json',
                    'kradle-api-key': instance._api_key
                },
                json={
                    'agentSlug': slug,
                    'agentUrl': url
                },
                timeout=30
            )
            
            if response.status_code == 404:
                instance._logger.log_error(
                    "Agent not found\n\n"
                    "To fix this:\n"
                    "1. Create a new agent profile at https://app.kradle.ai/workbench/agents\n"
                    "2. Use the same slug in your code as the one you created\n"
                    "3. Try running your agent again\n"
                )
                sys.exit(1)
                
            if response.status_code in (200, 201):
                instance._logger.log_success(f"Agent '{slug}' registered successfully")
                return True
                
            instance._logger.log_error(f"Failed to register agent '{slug}': Status {response.status_code}")
            return False
                    
        except Exception as e:
            instance._logger.log_error(f"Failed to register agent '{slug}'", e)
            return False

    def _create_tunnel(self, port):
        tunnel_instance, tunnel_url = create_tunnel(port)
        if tunnel_instance:
            self._tunnel = tunnel_instance
            self._logger.log_success(f"Tunnel created successfully")
            return tunnel_url
        else:
            self._logger.log_warning("Failed to create tunnel, falling back to local URL")
            return None
    
    @classmethod
    def serve_agent(cls, agent_class, slug, port=None, tunnel=True, host='localhost', hot_reload=True):
        """Start the agent server with automatic agent creation support."""
        instance = cls()
        
        # Initial setup and validation
        utils.validate_api_key(instance)
        args = KradleArgumentParser.parse()
        port = port if port is not None else instance._find_free_port()
        
        # Set up URLs
        agent_url = utils.setup_agent_url(instance, slug, port, tunnel)
        
        # Try to register or create agent
        success, was_created = utils.register_or_create_agent(
            instance._api_key,
            instance._get_app_url(),
            agent_class.__name__,
            agent_url,
            slug,
            args,
            instance._logger
        )
        
        if not success:
            sys.exit(1)

        # Handle hot reload case
        is_hot_reload = slug in instance._agent_classes and hasattr(agent_class, 'url')
        if is_hot_reload:
            instance._agent_classes[slug]['class'] = agent_class
            if hot_reload:
                instance._hot_reload_observer = setup_hot_reload(instance, agent_class)
            return agent_class.url

        # Register new agent class
        if slug not in instance._agent_classes:
            instance._agent_classes[slug] = {'class': agent_class, 'count': 1}

        # Initialize or use existing server
        if not instance._app:
            # Set up new server
            instance._app = instance._create_app()
            instance.port = port
            utils.setup_server(instance, port, host)
            
            # Set agent properties
            if slug != "*":
                agent_class.url = agent_url
                agent_class.slug = slug

            if hot_reload:
                instance._hot_reload_observer = setup_hot_reload(instance, agent_class)

            # Display startup banner
            instance._logger.display_startup_banner({
                'env': instance._app.config['ENV'],
                'debug': instance._app.config['DEBUG'],
                'port': instance.port,
                'agent_slug': slug,
                'agent_url': agent_url,
                'challenge_url': f'{instance._get_app_url()}/workbench/challenges'
            })
            
            # Start main thread
            instance._main_thread = threading.Thread(target=instance._shutdown_event.wait)
            instance._main_thread.daemon = False
            instance._main_thread.start()
            
            return agent_url
        
        # Handle existing server case
        if slug != "*":
            agent_class.url = agent_url
            agent_class.slug = slug

        if hot_reload:
            instance._hot_reload_observer = setup_hot_reload(instance, agent_class)
            
        return agent_url
        
    @classmethod
    def get_agent_behavior(cls, slug):
        instance = cls()
        FALLBACK_BEHAVIOR = {
            "persona": "You are a helpful assistant",
            "model": "openai/gpt-4",
            "respondWithCode": False,
            "subscribedEvents": ['command_executed', 'message']
        }
        
        KRADLE_APP_URL = (
            "http://localhost:3000"
            if os.getenv("KRADLE_DEV") 
            else "https://app.kradle.ai"
        )

        print(f"KRADLE_APP_URL: {KRADLE_APP_URL}")

        try:
            response = requests.post(
                f'{KRADLE_APP_URL}/api/getAgentBehavior',
                headers={
                    'Content-Type': 'application/json',
                    'kradle-api-key': instance._api_key
                },
                json={
                    'agentSlug': slug,
                },
                timeout=30
            )
            
            if response.status_code in (200, 201):
                instance._logger.log_success(f"Retrieved behavior for agent '{slug}'")
                return response.json()
            else:
                instance._logger.log_error(f"Failed to get behavior for agent '{slug}': Status {response.status_code}")
                return FALLBACK_BEHAVIOR
                    
        except Exception as e:
            instance._logger.log_error(f"Failed to get behavior for agent '{slug}'", e)
            return FALLBACK_BEHAVIOR
    
    @classmethod
    def create_log(cls, session_id, participant_id, level, message):
        instance = cls()
        KRADLE_APP_URL = (
            "http://localhost:3000" 
            if os.getenv("KRADLE_DEV") 
            else "https://app.kradle.ai"
        )

        try:
            response = requests.post(
                f'{KRADLE_APP_URL}/api/createLog',
                headers={
                    'Content-Type': 'application/json',
                    'kradle-api-key': instance._api_key
                },
                json={
                    'level': level,
                    'message': message,
                    'sessionId': session_id,
                    'participantId': participant_id
                },
                timeout=30
            )
            
            if response.status_code in (200, 201):
                instance._logger.log_success(f"stored log for participant_id '{participant_id}'")
                return True
            else:
                instance._logger.log_error(f"Failed to store log for participant_id '{participant_id}': Status {response.status_code}")
                return False
                    
        except Exception as e:
            instance._logger.log_error(f"Failed to store log for participant_id '{participant_id}': Status {response.status_code}")
            return None


    @classmethod
    def create_session(cls, challenge_slug, agents):
        """Create a new challenge session for one or more agents."""
        instance = cls()
        base_url = "http://localhost:3000" if os.getenv("KRADLE_DEV") else "https://app.kradle.ai"
        
        # Validate API key
        if not hasattr(instance, '_api_key') or not instance._api_key:
            instance._logger.log_error(
                "No API key found. Please set your API key before creating a session:\n\n"
                "1. Get your API key from https://app.kradle.ai\n"
                "2. Add it to your .env file: KRADLE_API_KEY=your_api_key\n"
                "3. Load it in your code:\n"
                "   load_dotenv()\n"
                "   MY_API_KEY = os.getenv('KRADLE_API_KEY')\n"
                "   Kradle.set_api_key(MY_API_KEY)"
            )
            sys.exit(1)
        
        try:
            agent_list = [agents] if not isinstance(agents, list) else agents
            
            for agent in agent_list:
                if not agent.url or not hasattr(agent, 'slug'):
                    raise ValueError(f"Agent {getattr(agent, 'slug', 'unknown')} is not properly configured")
            
            agent_data = [{'agentSlug': agent.slug, 'agentUrl': agent.url} for agent in agent_list]
            instance._logger.log_info("Launching session...")
            
            response = requests.post(
                f'{base_url}/api/createSession',
                headers={'Content-Type': 'application/json', 'kradle-api-key': instance._api_key},
                json={'challengeSlug': challenge_slug, 'agents': agent_data},
                timeout=30
            )
            
            response.raise_for_status()
            session_id = response.json()['sessionId']
            
            instance._logger.log_success("Session launched successfully!")
            instance._logger.log_info(f"View it live: {base_url}/workbench/sessions/{session_id}")
            
            return session_id
            
        except Exception as e:
            instance._logger.log_error("Session creation failed", e)