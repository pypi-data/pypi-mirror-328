import requests
import sys
import threading
from typing import Optional, Dict, List, Any, Tuple

def register_or_create_agent(
    api_key: str,
    app_url: str,
    agent_name: str,
    agent_url: str,
    slug: str,
    args,
    logger
) -> Tuple[bool, bool]:
    """Try to register agent, create if needed."""
    # First try to register the URL - this tells us if agent exists
    try:
        response = requests.post(
            f'{app_url}/api/setAgentUrl',
            headers={
                'kradle-api-key': api_key,
                'Content-Type': 'application/json'
            },
            json={
                'agentSlug': slug,
                'agentUrl': agent_url
            },
            timeout=30
        )
        
        # Agent exists and URL was updated
        if response.status_code in (200, 201):
            if args.create:
                logger.log_info(f"Agent '{slug}' already exists, using it")
            else:
                logger.log_success(f"Agent '{slug}' registered successfully")
            return True, False
            
        # Agent doesn't exist - create it if requested
        if response.status_code == 404 and args.create:
            return create_agent(api_key, app_url, agent_name, agent_url, slug, logger)
            
        # Agent doesn't exist - show options
        if response.status_code == 404:
            logger.log_warning(
                f"\n> No agent found: '{slug}'\n\n"
                "Options:\n"
                f"  1. Auto-create: python {args.script_name} -c\n"
                f"  2. Create manually: {app_url}/workbench/create/agent\n"
            )
            return False, False
            
        # Other errors
        logger.log_error(f"Registration failed: {response.json().get('error', 'Unknown error')}")
        return False, False
        
    except Exception as e:
        logger.log_error(f"Registration failed: {str(e)}")
        return False, False

def create_agent(
    api_key: str, 
    app_url: str, 
    agent_name: str,
    agent_url: str,
    slug: str,
    logger
) -> Tuple[bool, bool]:
    """Create a new agent."""
    try:
        logger.log_info(f"Creating agent '{slug}'...")
        response = requests.post(
            f'{app_url}/api/createAgent',
            headers={
                'kradle-api-key': api_key,
                'Content-Type': 'application/json'
            },
            json={
                'name': agent_name,
                'url': agent_url,
                'slug': slug
            }
        )
        
        if response.status_code in (200, 201):
            logger.log_success(
                f"\n✨ Created agent '{slug}'\n"
                f"Configure: {app_url}/workbench/create/agent\n"
            )
            return True, True
            
        error_msg = response.json().get('error', 'Unknown error') if response.text else f'Status {response.status_code}'
        logger.log_error(f"Creation failed: {error_msg}")
        return False, False
        
    except Exception as e:
        logger.log_error(f"Creation failed: {str(e)}")
        return False, False

def setup_server(instance, port: int, host: str = 'localhost') -> None:
    """Set up and start the server."""
    if not instance._is_port_available(port):
        instance._logger.log_error(f"Port {port} is not available")
        raise ValueError(f"Port {port} is not available")
    
    instance._setup_signal_handlers()
    instance._server_thread = threading.Thread(target=instance._run_server, daemon=True)
    instance._server_thread.start()
    
    if not instance._server_ready.wait(timeout=5.0):
        instance._logger.log_error("Server failed to start within timeout")
        raise RuntimeError("Server failed to start within timeout")

def setup_agent_url(instance, slug: str, port: int, tunnel: bool = True) -> str:
    """Set up agent URL with optional tunnel."""
    agent_url = f"http://localhost:{port}/{slug}"

    if tunnel:
        if not hasattr(instance, '_tunnel_url'):
            tunnel_url = instance._create_tunnel(port)
            if tunnel_url:
                instance._tunnel_url = tunnel_url
                agent_url = f"{tunnel_url}/{slug}"
        else:
            agent_url = f"{instance._tunnel_url}/{slug}"
    
    return agent_url

def validate_api_key(instance) -> None:
    """Validate API key existence."""
    if not hasattr(instance, '_api_key') or not instance._api_key:
        instance._logger.log_warning(
            "\n> API key required\n\n"
            "Setup:\n"
            "  1. Get your key: https://app.kradle.ai\n"
            "  2. Add to .env: KRADLE_API_KEY=your_api_key\n"
            "  3. Load in code:\n"
            "     load_dotenv()\n"
            "     Kradle.set_api_key(os.getenv('KRADLE_API_KEY'))\n"
        )
        sys.exit(1)