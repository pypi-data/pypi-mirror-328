"""Mining related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal

class BlockTemplate(BaseModel):
    """Model for block template"""
    capabilities: List[str]
    version: int
    rules: List[str]
    vbavailable: Dict[str, int]
    vbrequired: int
    previousblockhash: str
    transactions: List[Dict[str, Any]]
    coinbaseaux: Dict[str, str]
    coinbasevalue: int
    longpollid: str
    target: str
    mintime: int
    mutable: List[str]
    noncerange: str
    sigoplimit: int
    sizelimit: int
    curtime: int
    bits: str
    height: int
    default_witness_commitment: Optional[str]

class MiningInfoResponse(BaseModel):
    """Model for mining information"""
    blocks: int
    currentblockweight: int
    currentblocktx: int
    difficulty: Decimal
    networkhashps: Decimal
    hashespersec: int
    pooledtx: int
    chain: str
    warnings: str

class ProgPowHashResult(BaseModel):
    """Model for ProgPoW hash result"""
    header_hash: str
    mix_hash: str
    final_hash: str

# Request Models
class GetBlockTemplateRequest(BaseModel):
    """Request model for getblocktemplate RPC call"""
    template_request: Optional[Dict[str, Any]] = None
    capabilities: Optional[List[str]] = None
    rules: Optional[List[str]] = None

class GetMiningInfoRequest(BaseModel):
    """Request model for getmininginfo RPC call"""
    pass

class GetNetworkHashPSRequest(BaseModel):
    """Request model for getnetworkhashps RPC call"""
    nblocks: Optional[int] = None
    height: Optional[int] = None

class GetEvrProgPowHashRequest(BaseModel):
    """Request model for getevrprogpowhash RPC call"""
    header_hash: str
    nonce: int
    block_height: int
    mix_hash: Optional[str] = None
    final_hash: Optional[str] = None
    dag_epochs: Optional[int] = None

class PPRPCSBRequest(BaseModel):
    """Request model for pprpcsb RPC call"""
    header_hash: str
    mix_hash: str

class PrioritiseTransactionRequest(BaseModel):
    """Request model for prioritisetransaction RPC call"""
    txid: str
    priority_delta: int
    fee_delta: int

class SubmitBlockRequest(BaseModel):
    """Request model for submitblock RPC call"""
    hexdata: str
    dummy: Optional[str] = None

class GetBlockSubsidyRequest(BaseModel):
    """Request model for getblocksubsidy RPC call"""
    height: Optional[int] = None

class EstimateRewardRequest(BaseModel):
    """Request model for estimatereward RPC call"""
    blocks: Optional[int] = None
    rewardperiod: Optional[int] = None

# Response Models
class BlockSubsidyResponse(BaseModel):
    """Response model for getblocksubsidy RPC call"""
    miner: int
    masternode: int
    governance: int

class EstimateRewardResponse(BaseModel):
    """Response model for estimatereward RPC call"""
    blocks: int
    estimate: Decimal

__all__ = [
    # Models
    'BlockTemplate',
    'MiningInfoResponse',
    'ProgPowHashResult',
    'BlockSubsidyResponse',
    'EstimateRewardResponse',
    
    # Request Models
    'GetBlockTemplateRequest',
    'GetMiningInfoRequest',
    'GetNetworkHashPSRequest',
    'GetEvrProgPowHashRequest',
    'PPRPCSBRequest',
    'PrioritiseTransactionRequest',
    'SubmitBlockRequest',
    'GetBlockSubsidyRequest',
    'EstimateRewardRequest'
] 