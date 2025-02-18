"""Base models and common parameters for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator
from decimal import Decimal

# Base RPC Models
class RPCRequest(BaseModel):
    """Base model for RPC requests"""
    jsonrpc: TypeLiteral["2.0"] = "2.0"
    method: str
    params: List[Any] = Field(default_factory=list)
    id: int

class RPCResponse(BaseModel):
    """Base model for RPC responses"""
    jsonrpc: TypeLiteral["2.0"] = "2.0"
    result: Any
    error: Optional[Dict[str, Any]] = None
    id: int

class RPCError(BaseModel):
    """Model for RPC error responses"""
    code: int
    message: str
    method: Optional[str] = None

# Common Parameter Models
class BlockHashParam(BaseModel):
    """Model for block hash parameter"""
    block_hash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class BlockHeightParam(BaseModel):
    """Model for block height parameter"""
    height: int = Field(..., ge=0)

class TransactionHashParam(BaseModel):
    """Model for transaction hash parameter"""
    tx_hash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class AddressParam(BaseModel):
    """Model for Evrmore address parameter"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")

class AssetNameParam(BaseModel):
    """Model for asset name parameter"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    
    @validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            return v
        if not v[0].isalpha():
            raise ValueError("Asset name must start with a letter")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class IPFSHashParam(BaseModel):
    """Model for IPFS hash parameter"""
    ipfs_hash: str = Field(..., min_length=46, max_length=46, pattern="^Qm[a-zA-Z0-9]{44}$")

class AmountParam(BaseModel):
    """Model for amount parameter"""
    amount: Decimal = Field(..., ge=0)

class UnitsParam(BaseModel):
    """Model for units parameter"""
    units: int = Field(..., ge=0, le=8)

class FeeEstimateModeParam(BaseModel):
    """Model for fee estimate mode parameter"""
    estimate_mode: TypeLiteral["UNSET", "ECONOMICAL", "CONSERVATIVE"] = "UNSET"

# Common Transaction Models
class ScriptPubKey(BaseModel):
    """Model for scriptPubKey in transaction outputs"""
    asm: str
    hex: str
    reqSigs: Optional[int]
    type: str
    addresses: Optional[List[str]]

class TransactionInput(BaseModel):
    """Model for transaction inputs"""
    txid: str
    vout: int
    scriptSig: Dict[str, str]
    sequence: int
    txinwitness: Optional[List[str]]

class TransactionOutput(BaseModel):
    """Model for transaction outputs"""
    value: Decimal
    n: int
    scriptPubKey: ScriptPubKey

class TransactionDetail(BaseModel):
    """Model for transaction detail"""
    account: str
    address: str
    category: str
    amount: Decimal
    label: str
    vout: int
    fee: Optional[Decimal] = None
    abandoned: Optional[bool] = None

__all__ = [
    # Base Models
    'RPCRequest',
    'RPCResponse',
    'RPCError',
    
    # Parameter Models
    'BlockHashParam',
    'BlockHeightParam',
    'TransactionHashParam',
    'AddressParam',
    'AssetNameParam',
    'IPFSHashParam',
    'AmountParam',
    'UnitsParam',
    'FeeEstimateModeParam',
    
    # Transaction Models
    'ScriptPubKey',
    'TransactionInput',
    'TransactionOutput',
    'TransactionDetail'
] 