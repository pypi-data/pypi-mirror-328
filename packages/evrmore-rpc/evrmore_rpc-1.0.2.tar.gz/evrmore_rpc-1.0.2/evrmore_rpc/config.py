"""Configuration handling for evrmore_rpc

This module handles loading and validation of Evrmore node configuration.
By default, it looks for evrmore.conf in the user's home directory (~/.evrmore/),
but this can be overridden by setting EVRMORE_ROOT environment variable or
passing the path explicitly when creating the RPC client.
"""
import os
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict

class ConfigError(Exception):
    """Base class for configuration errors"""
    pass

class EvrmoreConfigError(ConfigError):
    """Raised when there are issues with evrmore.conf"""
    pass

class EvrmoreConfig(BaseModel):
    """Model for Evrmore node configuration"""
    model_config = ConfigDict(extra='allow')
    
    rpcuser: str = Field(..., min_length=1, description="RPC username for authentication")
    rpcpassword: str = Field(..., min_length=1, description="RPC password for authentication")
    rpcport: int = Field(8819, gt=0, lt=65536, description="RPC port (default: 8819)")
    rpcbind: str = Field("127.0.0.1", description="IP address to bind RPC server")
    server: bool = Field(True, description="Whether to enable RPC server")
    
    # Optional ZMQ settings
    zmqpubhashtx: Optional[str] = Field(None, description="ZMQ endpoint for transaction hash notifications")
    zmqpubhashblock: Optional[str] = Field(None, description="ZMQ endpoint for block hash notifications")
    
    @field_validator('rpcuser')
    @classmethod
    def validate_rpcuser(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("rpcuser cannot be empty")
        return v
    
    @field_validator('rpcpassword')
    @classmethod
    def validate_rpcpassword(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("rpcpassword cannot be empty")
        if len(v) < 8:
            raise ValueError("rpcpassword should be at least 8 characters long")
        return v
    
    @field_validator('server')
    @classmethod
    def validate_server(cls, v: bool) -> bool:
        if not v:
            raise ValueError("server=1 is required for RPC functionality")
        return v

def get_default_config_path() -> Path:
    """Get the default path to evrmore.conf"""
    # Check environment variable first
    if evrmore_root := os.getenv('EVRMORE_ROOT'):
        return Path(evrmore_root) / 'evrmore.conf'
    
    # Default to ~/.evrmore/evrmore.conf
    return Path.home() / '.evrmore' / 'evrmore.conf'

def load_config(config_path: Optional[Path] = None) -> EvrmoreConfig:
    """Load and validate Evrmore configuration
    
    Args:
        config_path: Optional path to evrmore.conf. If not provided,
                    will use default location.
    
    Returns:
        Validated configuration object
        
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
    
    try:
        # Read config file
        config = {}
        with open(config_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Convert known types
                    if value.lower() in ('0', '1', 'true', 'false'):
                        config[key] = bool(int(value == '1' or value.lower() == 'true'))
                    elif value.isdigit():
                        config[key] = int(value)
                    else:
                        config[key] = value
        
        # Validate using model
        return EvrmoreConfig(**config)
        
    except Exception as e:
        raise EvrmoreConfigError(f"Failed to load configuration: {e}") 