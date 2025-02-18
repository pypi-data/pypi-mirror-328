"""Address index related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import AddressParam

class AddressBalance(BaseModel):
    """Model for address balance"""
    balance: Decimal
    received: Decimal
    immature: Optional[Decimal]

class AddressDelta(BaseModel):
    """Model for address delta"""
    satoshis: int
    txid: str
    index: int
    blockindex: int
    height: int
    address: str

class AddressUnspent(BaseModel):
    """Model for address unspent"""
    txid: str
    outputIndex: int
    script: str
    satoshis: int
    height: int

class AddressMempool(BaseModel):
    """Model for address mempool"""
    address: str
    txid: str
    index: int
    satoshis: int
    timestamp: int
    prevtxid: str
    prevout: int

class AddressUtxo(BaseModel):
    """Model for address UTXO"""
    address: str
    txid: str
    outputIndex: int
    script: str
    satoshis: int
    height: int
    assetName: Optional[str]
    amount: Optional[Decimal]

# Request Models
class GetAddressBalanceRequest(BaseModel):
    """Request model for getaddressbalance RPC call"""
    addresses: List[str] = Field(..., min_items=1)
    
    @validator('addresses')
    def validate_addresses(cls, v: List[str]) -> List[str]:
        for addr in v:
            if not addr.startswith('E') or len(addr) != 34:
                raise ValueError(f"Invalid Evrmore address format: {addr}")
        return v

class GetAddressDeltas(BaseModel):
    """Request model for getaddressdeltas RPC call"""
    addresses: List[str] = Field(..., min_items=1)
    start: Optional[int] = None
    end: Optional[int] = None
    chainInfo: bool = False
    
    @validator('addresses')
    def validate_addresses(cls, v: List[str]) -> List[str]:
        for addr in v:
            if not addr.startswith('E') or len(addr) != 34:
                raise ValueError(f"Invalid Evrmore address format: {addr}")
        return v

class GetAddressMempool(BaseModel):
    """Request model for getaddressmempool RPC call"""
    addresses: List[str] = Field(..., min_items=1)
    
    @validator('addresses')
    def validate_addresses(cls, v: List[str]) -> List[str]:
        for addr in v:
            if not addr.startswith('E') or len(addr) != 34:
                raise ValueError(f"Invalid Evrmore address format: {addr}")
        return v

class GetAddressUtxos(BaseModel):
    """Request model for getaddressutxos RPC call"""
    addresses: List[str] = Field(..., min_items=1)
    chainInfo: bool = False
    assetName: Optional[str] = None
    
    @validator('addresses')
    def validate_addresses(cls, v: List[str]) -> List[str]:
        for addr in v:
            if not addr.startswith('E') or len(addr) != 34:
                raise ValueError(f"Invalid Evrmore address format: {addr}")
        return v
    
    @validator('assetName')
    def validate_asset_name(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if v == "EVR":
                return v
            if not v[0].isalpha():
                raise ValueError("Asset name must start with a letter")
            if ".." in v:
                raise ValueError("Asset name cannot contain consecutive dots")
            if v.endswith("."):
                raise ValueError("Asset name cannot end with a dot")
        return v

class GetAddressTxids(BaseModel):
    """Request model for getaddresstxids RPC call"""
    addresses: List[str] = Field(..., min_items=1)
    start: Optional[int] = None
    end: Optional[int] = None
    
    @validator('addresses')
    def validate_addresses(cls, v: List[str]) -> List[str]:
        for addr in v:
            if not addr.startswith('E') or len(addr) != 34:
                raise ValueError(f"Invalid Evrmore address format: {addr}")
        return v

__all__ = [
    # Models
    'AddressBalance',
    'AddressDelta',
    'AddressUnspent',
    'AddressMempool',
    'AddressUtxo',
    
    # Request Models
    'GetAddressBalanceRequest',
    'GetAddressDeltas',
    'GetAddressMempool',
    'GetAddressUtxos',
    'GetAddressTxids'
] 