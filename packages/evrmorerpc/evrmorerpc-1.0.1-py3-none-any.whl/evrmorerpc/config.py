"""Configuration handling for EvrmoreRPC

This module handles loading and validation of Evrmore node configuration.
By default, it looks for evrmore.conf in the user's home directory (~/.evrmore/),
but this can be overridden by setting EVRMORE_ROOT environment variable or
passing the path explicitly when creating the RPC client.
"""
import os
import configparser
from pathlib import Path
from typing import Dict, Any, Optional

class ConfigError(Exception):
    """Base class for configuration errors"""
    pass

class EvrmoreConfigError(ConfigError):
    """Raised when there are issues with evrmore.conf"""
    pass

def get_default_config_path() -> Path:
    """Get the default path to evrmore.conf"""
    # Check environment variable first
    evrmore_root = os.getenv('EVRMORE_ROOT')
    if evrmore_root:
        return Path(evrmore_root) / 'evrmore.conf'
    
    # Default to ~/.evrmore/evrmore.conf
    return Path.home() / '.evrmore' / 'evrmore.conf'

def validate_config(config: Dict[str, Any]) -> None:
    """Validate the loaded configuration
    
    Args:
        config: Dictionary of configuration settings
        
    Raises:
        EvrmoreConfigError: If configuration is invalid
    """
    required_settings = {
        'rpcuser': str,
        'rpcpassword': str,
        'rpcport': int,
        'server': bool
    }
    
    errors = []
    
    # Check required settings
    for setting, expected_type in required_settings.items():
        if setting not in config:
            errors.append(f"Missing required setting: {setting}")
            continue
            
        value = config[setting]
        if expected_type == bool:
            if not isinstance(value, bool) and str(value) not in ('0', '1'):
                errors.append(f"Invalid value for {setting}: expected boolean (0/1)")
        elif expected_type == int:
            try:
                int(value)
            except ValueError:
                errors.append(f"Invalid value for {setting}: expected integer")
    
    # Verify server mode is enabled
    if 'server' in config and not config['server']:
        errors.append("server=1 is required in evrmore.conf")
    
    if errors:
        raise EvrmoreConfigError(
            "Configuration validation failed:\n" + "\n".join(f"- {e}" for e in errors)
        )

def load_config(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load and validate Evrmore configuration
    
    Args:
        config_path: Optional path to evrmore.conf. If not provided,
                    will use default location.
    
    Returns:
        Dictionary of configuration settings
        
    Raises:
        EvrmoreConfigError: If configuration is invalid or cannot be loaded
    """
    if config_path is None:
        config_path = get_default_config_path()
    
    if not config_path.exists():
        raise EvrmoreConfigError(
            f"Configuration file not found: {config_path}\n"
            "Please ensure Evrmore is properly configured."
        )
    
    config = configparser.ConfigParser()
    try:
        with open(config_path) as f:
            # Add a dummy section header since evrmore.conf doesn't have one
            config.read_string('[evrmore]\n' + f.read())
    except Exception as e:
        raise EvrmoreConfigError(f"Failed to read configuration: {e}")
    
    # Extract settings from the evrmore section
    settings = {}
    for key, value in config['evrmore'].items():
        # Convert some known types
        if value.lower() in ('0', '1'):
            settings[key] = bool(int(value))
        elif value.isdigit():
            settings[key] = int(value)
        else:
            settings[key] = value
    
    # Validate the configuration
    validate_config(settings)
    
    # Set defaults for optional settings
    settings.setdefault('rpchost', '127.0.0.1')
    
    return settings 