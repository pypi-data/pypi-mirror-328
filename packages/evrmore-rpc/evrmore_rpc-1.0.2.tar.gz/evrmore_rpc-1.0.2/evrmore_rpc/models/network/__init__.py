"""Network related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal, Union
from pydantic import BaseModel, Field, validator, field_validator, ConfigDict
from decimal import Decimal

class NetworkAddress(BaseModel):
    """Model for network address"""
    model_config = ConfigDict(extra='allow')
    
    address: str
    port: int
    score: int

class Network(BaseModel):
    """Model for network information"""
    model_config = ConfigDict(extra='allow')
    
    name: str
    limited: bool
    reachable: bool
    proxy: str
    proxy_randomize_credentials: bool

class NetworkInfoResponse(BaseModel):
    """Response model for getnetworkinfo RPC call"""
    model_config = ConfigDict(extra='allow')
    
    version: int
    subversion: str
    protocolversion: int
    localservices: str
    localrelay: bool
    timeoffset: int
    connections: int
    networks: List[Dict[str, Any]]
    relayfee: float
    localaddresses: List[Dict[str, Any]]
    warnings: str

class PeerInfo(BaseModel):
    """Model for peer information"""
    model_config = ConfigDict(extra='allow')
    
    id: int
    addr: str
    addrbind: str
    addrlocal: Optional[str] = None
    services: str
    relaytxes: bool
    lastsend: int
    lastrecv: int
    bytessent: int
    bytesrecv: int
    conntime: int
    timeoffset: int
    pingtime: Optional[float] = None
    minping: Optional[float] = None
    version: int
    subver: str
    inbound: bool
    addnode: bool
    startingheight: int
    banscore: int
    synced_headers: int
    synced_blocks: int
    inflight: List[int]
    whitelisted: bool
    permissions: List[str]
    minfeefilter: float
    bytessent_per_msg: Dict[str, int]
    bytesrecv_per_msg: Dict[str, int]
    
    @field_validator('addr')
    def validate_addr(cls, v: str) -> str:
        """Validate address format"""
        if not v:
            raise ValueError("Address cannot be empty")
        return v

class BannedPeer(BaseModel):
    """Model for banned peer information"""
    model_config = ConfigDict(extra='allow')
    
    address: str
    banned_until: int
    ban_created: int
    ban_reason: str
    
    @field_validator('address')
    def validate_address(cls, v: str) -> str:
        """Validate address format"""
        if not v:
            raise ValueError("Address cannot be empty")
        return v

class NetTotals(BaseModel):
    """Model for network totals"""
    model_config = ConfigDict(extra='allow')
    
    totalbytesrecv: int
    totalbytessent: int
    timemillis: int
    uploadtarget: Dict[str, Any]

# Request Models
class AddNodeRequest(BaseModel):
    """Request model for addnode RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    node: str
    command: Literal["add", "remove", "onetry"]

class DisconnectNodeRequest(BaseModel):
    """Request model for disconnectnode RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    address: Optional[str] = None
    nodeid: Optional[int] = None
    
    @field_validator('address', 'nodeid')
    def validate_node_info(cls, v: Optional[Union[str, int]]) -> Optional[Union[str, int]]:
        """Validate node information"""
        if isinstance(v, str) and not v.strip():
            raise ValueError("Address must be non-empty if provided")
        return v

class GetAddedNodeInfoRequest(BaseModel):
    """Request model for getaddednodeinfo RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    node: Optional[str] = None

class GetConnectionCountRequest(BaseModel):
    """Request model for getconnectioncount RPC call"""
    model_config = ConfigDict(extra='forbid')

class GetNetTotalsRequest(BaseModel):
    """Request model for getnettotals RPC call"""
    model_config = ConfigDict(extra='forbid')

class GetNetworkInfoRequest(BaseModel):
    """Request model for getnetworkinfo RPC call"""
    model_config = ConfigDict(extra='forbid')

class GetPeerInfoRequest(BaseModel):
    """Request model for getpeerinfo RPC call"""
    model_config = ConfigDict(extra='forbid')

class ListBannedRequest(BaseModel):
    """Request model for listbanned RPC call"""
    model_config = ConfigDict(extra='forbid')

class PingRequest(BaseModel):
    """Request model for ping RPC call"""
    model_config = ConfigDict(extra='forbid')

class SetBanRequest(BaseModel):
    """Request model for setban RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    subnet: str
    command: Literal["add", "remove"]
    bantime: Optional[int] = None
    absolute: bool = False

class SetNetworkActiveRequest(BaseModel):
    """Request model for setnetworkactive RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    state: bool

__all__ = [
    # Models
    'NetworkInfoResponse',
    'PeerInfo',
    'BannedPeer',
    'NetTotals',
    
    # Request Models
    'AddNodeRequest',
    'DisconnectNodeRequest',
    'GetAddedNodeInfoRequest',
    'GetConnectionCountRequest',
    'GetNetTotalsRequest',
    'GetNetworkInfoRequest',
    'GetPeerInfoRequest',
    'ListBannedRequest',
    'PingRequest',
    'SetBanRequest',
    'SetNetworkActiveRequest'
]