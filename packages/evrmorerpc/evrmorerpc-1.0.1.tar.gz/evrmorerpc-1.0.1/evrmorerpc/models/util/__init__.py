"""Utility related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam,
    FeeEstimateModeParam
)

class ValidateAddressResult(BaseModel):
    """Model for validate address result"""
    isvalid: bool
    address: Optional[str]
    scriptPubKey: Optional[str]
    ismine: Optional[bool]
    iswatchonly: Optional[bool]
    isscript: Optional[bool]
    iswitness: Optional[bool]
    witness_version: Optional[int]
    witness_program: Optional[str]
    script: Optional[str]
    hex: Optional[str]
    addresses: Optional[List[str]]
    sigsrequired: Optional[int]
    pubkey: Optional[str]
    iscompressed: Optional[bool]
    account: Optional[str]
    timestamp: Optional[int]
    hdkeypath: Optional[str]
    hdmasterkeyid: Optional[str]
    labels: Optional[List[str]]

class MultisigAddress(BaseModel):
    """Model for multisig address"""
    address: str
    redeemScript: str
    descriptor: str

class EstimateSmartFeeResult(BaseModel):
    """Model for estimate smart fee result"""
    feerate: Optional[Decimal]
    errors: Optional[List[str]]
    blocks: int

# Request Models
class CreateMultiSigRequest(BaseModel):
    """Request model for createmultisig RPC call"""
    nrequired: int = Field(..., gt=0)
    keys: List[str]
    address_type: Optional[Literal["legacy", "p2sh-segwit", "bech32"]] = None
    
    @validator('nrequired')
    def validate_nrequired(cls, v: int, values: Dict[str, Any]) -> int:
        if 'keys' in values and v > len(values['keys']):
            raise ValueError("Required signatures cannot exceed number of keys")
        return v

class EstimateFeeRequest(BaseModel):
    """Request model for estimatefee RPC call"""
    nblocks: int = Field(..., ge=1)

class EstimateSmartFeeRequest(BaseModel):
    """Request model for estimatesmartfee RPC call"""
    conf_target: int = Field(..., ge=1)
    estimate_mode: Optional[Literal["UNSET", "ECONOMICAL", "CONSERVATIVE"]] = "CONSERVATIVE"

class SignMessageWithPrivKeyRequest(BaseModel):
    """Request model for signmessagewithprivkey RPC call"""
    privkey: str
    message: str

class ValidateAddressRequest(BaseModel):
    """Request model for validateaddress RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")

class VerifyMessageRequest(BaseModel):
    """Request model for verifymessage RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    signature: str
    message: str

class ValidatePublicKeyRequest(BaseModel):
    """Request model for validatepubkey RPC call"""
    pubkey: str

class CreateMessageRequest(BaseModel):
    """Request model for createmessage RPC call"""
    message: str
    timestamp: Optional[int] = None
    expire_time: Optional[int] = None

class VerifyMessageSignatureRequest(BaseModel):
    """Request model for verifymessagesignature RPC call"""
    signature: str
    message: str
    pubkey: str

class ConvertAddressRequest(BaseModel):
    """Request model for convertaddress RPC call"""
    address: str
    type: Literal["legacy", "p2sh-segwit", "bech32"]

__all__ = [
    # Models
    'ValidateAddressResult',
    'MultisigAddress',
    'EstimateSmartFeeResult',
    
    # Request Models
    'CreateMultiSigRequest',
    'EstimateFeeRequest',
    'EstimateSmartFeeRequest',
    'SignMessageWithPrivKeyRequest',
    'ValidateAddressRequest',
    'VerifyMessageRequest',
    'ValidatePublicKeyRequest',
    'CreateMessageRequest',
    'VerifyMessageSignatureRequest',
    'ConvertAddressRequest'
] 