"""
evrmore-rpc: A typed Python wrapper for evrmore-cli commands with ZMQ support
Copyright (c) 2025 Manticore Technologies
MIT License - See LICENSE file for details
"""

__version__ = "1.1.0"
__author__ = "Manticore Technologies"
__email__ = "dev@manticore.tech"

from evrmore_rpc.client import EvrmoreRPCClient, EvrmoreRPCError
from evrmore_rpc.models.base import (
    Amount,
    Address,
    Asset,
    Transaction,
    Block,
    RPCResponse
)
from evrmore_rpc.utils import (
    format_amount,
    validate_response,
    validate_list_response,
    validate_dict_response,
    format_command_args
)
from evrmore_rpc.zmq.client import EvrmoreZMQClient

__all__ = [
    "EvrmoreRPCClient",
    "EvrmoreRPCError",
    "Amount",
    "Address",
    "Asset",
    "Transaction",
    "Block",
    "RPCResponse",
    "format_amount",
    "validate_response",
    "validate_list_response",
    "validate_dict_response",
    "format_command_args",
    "EvrmoreZMQClient"
] 