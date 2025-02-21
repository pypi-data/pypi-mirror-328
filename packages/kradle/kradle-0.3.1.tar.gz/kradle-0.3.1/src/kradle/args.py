import argparse
import os
import inspect
from typing import NamedTuple

class KradleArgs(NamedTuple):
    create: bool
    script_name: str
    is_interactive: bool

class KradleArgumentParser:
    """Parser for Kradle agent runner arguments and environment detection."""
    
    @staticmethod
    def parse() -> KradleArgs:
        """Parse command line arguments and detect environment details.
        
        Returns:
            KradleArgs containing parsed arguments and environment info
        """
        args = KradleArgumentParser._get_cli_args()
        script_name = KradleArgumentParser._get_script_name()
        is_interactive = KradleArgumentParser._is_interactive()
        
        return KradleArgs(
            create=args.create,
            script_name=script_name,
            is_interactive=is_interactive
        )

    @staticmethod
    def _get_cli_args() -> argparse.Namespace:
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(description='Kradle Agent Runner')
        parser.add_argument(
            '-c', '--create',
            action='store_true',
            help='Create agent if it doesn\'t exist'
        )
        # Parse known args to avoid conflicts
        args, _ = parser.parse_known_args()
        return args

    @staticmethod
    def _is_interactive() -> bool:
        """Check if running in interactive environment (Jupyter/Colab)."""
        try:
            # Only import IPython when needed
            from IPython import get_ipython
            shell = get_ipython().__class__.__name__
            if shell in ['ZMQInteractiveShell', 'Shell', 'Google.Colab']:
                return True
        except (NameError, ImportError):
            pass
        return False

    @staticmethod
    def _get_script_name() -> str:
        """Get the name of the running script."""
        try:
            frame = inspect.stack()[-1]
            return os.path.basename(frame.filename)
        except Exception:
            return "script.py"