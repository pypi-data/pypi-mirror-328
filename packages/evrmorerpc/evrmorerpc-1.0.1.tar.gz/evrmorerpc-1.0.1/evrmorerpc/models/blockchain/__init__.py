"""Blockchain related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral, Union
from pydantic import BaseModel, Field
from decimal import Decimal
from ..base import BlockHashParam, TransactionHashParam

class BlockHeader(BaseModel):
    """Model for block header information"""
    hash: str
    confirmations: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    time: int
    mediantime: int
    nonce: int
    bits: str
    difficulty: Decimal
    chainwork: str
    previousblockhash: Optional[str]
    nextblockhash: Optional[str]

class BlockHeaderResponse(BlockHeader):
    """Response model for getblockheader RPC call"""
    pass

class BlockInfoResponse(BlockHeader):
    """Model for full block information"""
    strippedsize: int
    size: int
    weight: int
    tx: List[str]
    headerhash: str
    mixhash: str
    nonce64: int
    ntx: Optional[int] = None
    previousblockhash: Optional[str] = None
    nextblockhash: Optional[str] = None
    coinbase_payload: Optional[str] = None

class BlockStats(BaseModel):
    """Model for block statistics"""
    avgfee: Optional[int]
    avgfeerate: Optional[int]
    avgtxsize: Optional[int]
    blockhash: str
    feerate_percentiles: Optional[List[int]]
    height: int
    ins: Optional[int]
    maxfee: Optional[int]
    maxfeerate: Optional[int]
    maxtxsize: Optional[int]
    medianfee: Optional[int]
    mediantime: Optional[int]
    mediantxsize: Optional[int]
    minfee: Optional[int]
    minfeerate: Optional[int]
    mintxsize: Optional[int]
    outs: Optional[int]
    subsidy: Optional[int]
    swtotal_size: Optional[int]
    swtotal_weight: Optional[int]
    swtxs: Optional[int]
    time: Optional[int]
    total_out: Optional[int]
    total_size: Optional[int]
    total_weight: Optional[int]
    totalfee: Optional[int]
    txs: Optional[int]
    utxo_increase: Optional[int]
    utxo_size_inc: Optional[int]

class ChainTip(BaseModel):
    """Model for chain tip information"""
    height: int
    hash: str
    branchlen: int
    status: TypeLiteral["active", "valid-fork", "valid-headers", "headers-only", "invalid"]

class ChainTxStats(BaseModel):
    """Model for chain transaction statistics"""
    time: int
    txcount: int
    window_final_block_hash: str
    window_final_block_height: int
    window_block_count: int
    window_tx_count: int
    window_interval: int
    txrate: float

class SpentInfoResponse(BaseModel):
    """Model for spent information"""
    txid: str
    index: int
    height: Optional[int]

class DecodedBlock(BaseModel):
    """Model for decoded block"""
    hash: str
    confirmations: int
    size: int
    strippedsize: int
    weight: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    tx: List[str]
    time: int
    mediantime: int
    nonce: int
    bits: str
    difficulty: Decimal
    chainwork: str
    nTx: int
    previousblockhash: Optional[str]
    nextblockhash: Optional[str]
    coinbase_payload: Optional[str]

class TxOutProof(BaseModel):
    """Model for transaction output proof"""
    data: str

class MempoolEntry(BaseModel):
    """Model for mempool entry information"""
    size: int
    fee: Decimal
    modifiedfee: Decimal
    time: int
    height: int
    descendantcount: int
    descendantsize: int
    descendantfees: int
    ancestorcount: int
    ancestorsize: int
    ancestorfees: int
    wtxid: str
    depends: List[str]

class MempoolInfoResponse(BaseModel):
    """Model for mempool information"""
    size: int
    bytes: int
    usage: int
    maxmempool: int
    mempoolminfee: Decimal

# Request Models
class GetBlockRequest(BaseModel):
    """Request model for getblock RPC call"""
    method: str = "getblock"
    params: List[Union[str, int]]
    id: Optional[int] = None

class GetBlockHashRequest(BaseModel):
    """Request model for getblockhash RPC call"""
    method: str = "getblockhash"
    params: List[int]
    id: Optional[int] = None

class GetBlockHeaderRequest(BlockHashParam):
    """Request model for getblockheader RPC call"""
    verbose: bool = True

class GetBlockStatsRequest(BaseModel):
    """Request model for getblockstats RPC call"""
    hash_or_height: str | int
    stats: Optional[List[str]] = None

    class Config:
        json_schema_extra = {
            "example": {
                "hash_or_height": "00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09",
                "stats": ["height", "time", "txs", "size"]
            }
        }

class GetChainTipsRequest(BaseModel):
    """Request model for getchaintips RPC call"""
    pass

class GetMempoolEntryRequest(TransactionHashParam):
    """Request model for getmempoolentry RPC call"""
    pass

class GetMempoolInfoRequest(BaseModel):
    """Request model for getmempoolinfo RPC call"""
    pass

class GetRawMempoolRequest(BaseModel):
    """Request model for getrawmempool RPC call"""
    verbose: bool = False

class GetTxOutRequest(BaseModel):
    """Request model for gettxout RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    n: int = Field(..., ge=0)
    include_mempool: bool = True

class GetTxOutSetInfoRequest(BaseModel):
    """Request model for gettxoutsetinfo RPC call"""
    pass

class ClearMemPoolRequest(BaseModel):
    """Request model for clearmempool RPC call"""
    pass

class DecodeBlockRequest(BaseModel):
    """Request model for decodeblock RPC call"""
    blockhex: str = Field(..., min_length=1)

class GetBlockHashesRequest(BaseModel):
    """Request model for getblockhashes RPC call"""
    high: int
    low: int
    options: Optional[Dict[str, Any]] = None

class GetChainTxStatsRequest(BaseModel):
    """Request model for getchaintxstats RPC call"""
    nblocks: Optional[int] = None
    blockhash: Optional[str] = None

class GetSpentInfoRequest(BaseModel):
    """Request model for getspentinfo RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    index: int = Field(..., ge=0)

class GetTxOutProofRequest(BaseModel):
    """Request model for gettxoutproof RPC call"""
    txids: List[str] = Field(..., min_items=1)
    blockhash: Optional[str] = None

class PreciousBlockRequest(BaseModel):
    """Request model for preciousblock RPC call"""
    blockhash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class PruneBlockchainRequest(BaseModel):
    """Request model for pruneblockchain RPC call"""
    height: int = Field(..., ge=0)

class VerifyChainRequest(BaseModel):
    """Request model for verifychain RPC call"""
    checklevel: Optional[int] = Field(3, ge=0, le=4)
    nblocks: Optional[int] = Field(6, ge=0)

class VerifyTxOutProofRequest(BaseModel):
    """Request model for verifytxoutproof RPC call"""
    proof: str

__all__ = [
    # Models
    'BlockHeader',
    'BlockHeaderResponse',
    'BlockInfoResponse',
    'BlockStats',
    'ChainTip',
    'ChainTxStats',
    'SpentInfoResponse',
    'DecodedBlock',
    'TxOutProof',
    'MempoolEntry',
    'MempoolInfoResponse',
    
    # Request Models
    'GetBlockRequest',
    'GetBlockHashRequest',
    'GetBlockHeaderRequest',
    'GetBlockStatsRequest',
    'GetChainTipsRequest',
    'GetMempoolEntryRequest',
    'GetMempoolInfoRequest',
    'GetRawMempoolRequest',
    'GetTxOutRequest',
    'GetTxOutSetInfoRequest',
    'ClearMemPoolRequest',
    'DecodeBlockRequest',
    'GetBlockHashesRequest',
    'GetChainTxStatsRequest',
    'GetSpentInfoRequest',
    'GetTxOutProofRequest',
    'PreciousBlockRequest',
    'PruneBlockchainRequest',
    'VerifyChainRequest',
    'VerifyTxOutProofRequest'
] 