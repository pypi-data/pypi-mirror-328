"""Control related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal

class LockedMemoryInfo(BaseModel):
    """Model for locked memory details"""
    used: int
    free: int
    total: int
    locked: int
    chunks_used: int
    chunks_free: int

class MemoryInfoResponse(BaseModel):
    """Model for memory information"""
    locked: LockedMemoryInfo

class RPCInfoResponse(BaseModel):
    """Model for RPC information"""
    active_commands: List[Dict[str, Any]]
    logpath: str

class MemPoolInfoResponse(BaseModel):
    """Model for mempool information"""
    loaded: bool
    size: int
    bytes: int
    usage: int
    maxmempool: int
    mempoolminfee: Decimal
    minrelaytxfee: Decimal

class NodeInfoResponse(BaseModel):
    """Model for node information"""
    version: int
    subversion: str
    protocolversion: int
    localservices: str
    localrelay: bool
    timeoffset: int
    networkactive: bool
    connections: int
    networks: List[Dict[str, Any]]
    relayfee: Decimal
    incrementalfee: Decimal
    localaddresses: List[Dict[str, Any]]
    warnings: str
    balance: Decimal
    blocks: int
    timeoffset: int
    connections: int
    proxy: Optional[str]
    difficulty: Decimal
    testnet: bool
    keypoololdest: int
    keypoolsize: int
    paytxfee: Decimal
    relayfee: Decimal
    errors: str

# Request Models
class GetMemoryInfoRequest(BaseModel):
    """Request model for getmemoryinfo RPC call"""
    mode: Literal["stats", "mallocinfo"] = "stats"

class GetRPCInfoRequest(BaseModel):
    """Request model for getrpcinfo RPC call"""
    pass

class GetMemPoolInfoRequest(BaseModel):
    """Request model for getmempoolinfo RPC call"""
    pass

class GetInfoRequest(BaseModel):
    """Request model for getinfo RPC call"""
    pass

class HelpRequest(BaseModel):
    """Request model for help RPC call"""
    command: Optional[str] = None

class StopRequest(BaseModel):
    """Request model for stop RPC call"""
    pass

class UptimeRequest(BaseModel):
    """Request model for uptime RPC call"""
    pass

class GetMemPoolEntryRequest(BaseModel):
    """Request model for getmempoolentry RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class GetMemPoolAncestorsRequest(BaseModel):
    """Request model for getmempoolancestors RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    verbose: bool = False

class GetMemPoolDescendantsRequest(BaseModel):
    """Request model for getmempooldescendants RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    verbose: bool = False

class GetRawMemPoolRequest(BaseModel):
    """Request model for getrawmempool RPC call"""
    verbose: bool = False

class SaveMemPoolRequest(BaseModel):
    """Request model for savemempool RPC call"""
    pass

class SetLogLevelRequest(BaseModel):
    """Request model for setloglevel RPC call"""
    level: Literal["trace", "debug", "info", "warning", "error", "none"] = "info"

class LoggingRequest(BaseModel):
    """Request model for logging RPC call"""
    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None

# Response Models
class LoggingResponse(BaseModel):
    """Response model for logging RPC call"""
    log_events: Optional[bool]
    debug: Optional[bool]
    libevent: Optional[bool]
    http: Optional[bool]
    bench: Optional[bool]
    zmq: Optional[bool]
    db: Optional[bool]
    rpc: Optional[bool]
    estimatefee: Optional[bool]
    addrman: Optional[bool]
    selectcoins: Optional[bool]
    reindex: Optional[bool]
    cmpctblock: Optional[bool]
    rand: Optional[bool]
    prune: Optional[bool]
    proxy: Optional[bool]
    mempoolrej: Optional[bool]
    libevent: Optional[bool]
    coindb: Optional[bool]
    qt: Optional[bool]
    leveldb: Optional[bool]

__all__ = [
    # Models
    'MemoryInfoResponse',
    'RPCInfoResponse',
    'MemPoolInfoResponse',
    'NodeInfoResponse',
    'LoggingResponse',
    
    # Request Models
    'GetMemoryInfoRequest',
    'GetRPCInfoRequest',
    'GetMemPoolInfoRequest',
    'GetInfoRequest',
    'HelpRequest',
    'StopRequest',
    'UptimeRequest',
    'GetMemPoolEntryRequest',
    'GetMemPoolAncestorsRequest',
    'GetMemPoolDescendantsRequest',
    'GetRawMemPoolRequest',
    'SaveMemPoolRequest',
    'SetLogLevelRequest',
    'LoggingRequest'
] 