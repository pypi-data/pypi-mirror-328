"""Evrmore RPC module

This module provides a Python interface to interact with an Evrmore node via RPC.
It includes models for all RPC commands and their responses, as well as
functionality for making RPC calls and handling errors.
"""

# Import main classes
from evrmore_rpc.client import evrmore_rpc
from evrmore_rpc.zmq import EvrmoreZMQ

# Import error classes
from evrmore_rpc.errors import (
    RPCError,
    NodeConnectionError,
    NodeAuthError,
    EvrmoreError
)

# Import all models
import evrmore_rpc.models as models

# Create global instance for convenience
client = evrmore_rpc()

# Export public interface
__all__ = [
    # Main classes
    'evrmore_rpc',
    'EvrmoreZMQ',
    
    # Exceptions
    'RPCError',
    'NodeConnectionError',
    'NodeAuthError',
    'EvrmoreError',
    
    # Global instance
    'client'
]

# Add all models to __all__
__all__ += models.__all__