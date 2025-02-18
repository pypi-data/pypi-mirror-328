"""Network related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal

class NetworkAddress(BaseModel):
    """Model for network address"""
    address: str
    port: int
    score: int

class Network(BaseModel):
    """Model for network information"""
    name: str
    limited: bool
    reachable: bool
    proxy: str
    proxy_randomize_credentials: bool

class NetworkInfoResponse(BaseModel):
    """Model for network information"""
    version: int
    subversion: str
    protocolversion: int
    localservices: str
    localrelay: bool
    timeoffset: int
    networkactive: bool
    connections: int
    networks: List[Network]
    relayfee: Decimal
    incrementalfee: Decimal
    localaddresses: List[NetworkAddress]
    warnings: str

class PeerInfo(BaseModel):
    """Model for peer information"""
    id: int
    addr: str
    addrbind: str
    addrlocal: Optional[str]
    services: str
    relaytxes: bool
    lastsend: int
    lastrecv: int
    bytessent: int
    bytesrecv: int
    conntime: int
    timeoffset: int
    pingtime: Optional[float]
    minping: Optional[float]
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
    minfeefilter: Decimal
    bytessent_per_msg: Dict[str, int]
    bytesrecv_per_msg: Dict[str, int]

class BannedPeer(BaseModel):
    """Model for banned peer information"""
    address: str
    banned_until: int
    ban_created: int
    ban_reason: str

class NetTotals(BaseModel):
    """Model for network totals"""
    totalbytesrecv: int
    totalbytessent: int
    timemillis: int
    uploadtarget: Dict[str, Any]

# Request Models
class AddNodeRequest(BaseModel):
    """Request model for addnode RPC call"""
    node: str
    command: Literal["add", "remove", "onetry"]

class DisconnectNodeRequest(BaseModel):
    """Request model for disconnectnode RPC call"""
    address: Optional[str] = None
    nodeid: Optional[int] = None
    
    @validator('address', 'nodeid')
    def validate_either_address_or_nodeid(cls, v, values, **kwargs):
        if 'address' not in values and 'nodeid' not in values:
            raise ValueError("Either address or nodeid must be provided")
        if 'address' in values and 'nodeid' in values:
            raise ValueError("Only one of address or nodeid should be provided")
        return v

class GetAddedNodeInfoRequest(BaseModel):
    """Request model for getaddednodeinfo RPC call"""
    node: Optional[str] = None

class GetConnectionCountRequest(BaseModel):
    """Request model for getconnectioncount RPC call"""
    pass

class GetNetTotalsRequest(BaseModel):
    """Request model for getnettotals RPC call"""
    pass

class GetNetworkInfoRequest(BaseModel):
    """Request model for getnetworkinfo RPC call"""
    pass

class GetPeerInfoRequest(BaseModel):
    """Request model for getpeerinfo RPC call"""
    pass

class ListBannedRequest(BaseModel):
    """Request model for listbanned RPC call"""
    pass

class PingRequest(BaseModel):
    """Request model for ping RPC call"""
    pass

class SetBanRequest(BaseModel):
    """Request model for setban RPC call"""
    subnet: str
    command: Literal["add", "remove"]
    bantime: Optional[int] = None
    absolute: bool = False

class SetNetworkActiveRequest(BaseModel):
    """Request model for setnetworkactive RPC call"""
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