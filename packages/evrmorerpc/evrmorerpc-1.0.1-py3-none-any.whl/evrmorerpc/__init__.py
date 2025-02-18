"""Evrmore RPC module

This module provides a Python interface to interact with an Evrmore node via RPC.
It includes models for all RPC commands and their responses, as well as
functionality for making RPC calls and handling errors.
"""

# Import main classes
from evrmorerpc.client import EvrmoreRPC
from evrmorerpc.zmq import EvrmoreZMQ

# Import error classes
from evrmorerpc.errors import (
    RPCError,
    NodeConnectionError,
    NodeAuthError,
    EvrmoreError
)

# Import all models
from evrmorerpc.models import *

# Create global instance for convenience
client = EvrmoreRPC()

# Export public interface
__all__ = [
    # Main classes
    'EvrmoreRPC',
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