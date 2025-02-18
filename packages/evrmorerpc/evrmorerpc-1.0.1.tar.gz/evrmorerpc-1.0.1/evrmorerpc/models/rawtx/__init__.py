"""Raw transaction related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal, Union
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import (
    TransactionInput,
    TransactionOutput,
    ScriptPubKey
)

class PrevTx(BaseModel):
    """Model for previous transaction"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    vout: int = Field(..., ge=0)
    scriptPubKey: str
    redeemScript: Optional[str] = None
    witnessScript: Optional[str] = None
    amount: Optional[Decimal] = None

class SignatureHashType(BaseModel):
    """Model for signature hash type"""
    sighash: Literal["ALL", "NONE", "SINGLE", "ALL|ANYONECANPAY", "NONE|ANYONECANPAY", "SINGLE|ANYONECANPAY"] = "ALL"

class AssetTransfer(BaseModel):
    """Model for asset transfer in raw transaction"""
    asset_name: str
    amount: Decimal
    message: Optional[str] = None
    expire_time: Optional[int] = None
    
class AssetIssue(BaseModel):
    """Model for asset issuance in raw transaction"""
    asset_name: str
    asset_quantity: Decimal
    units: int = Field(0, ge=0, le=8)
    reissuable: bool = True
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None

class AssetReissue(BaseModel):
    """Model for asset reissuance in raw transaction"""
    asset_name: str
    asset_quantity: Decimal
    reissuable: Optional[bool] = None
    ipfs_hash: Optional[str] = None

class UniqueAssetIssue(BaseModel):
    """Model for unique asset issuance in raw transaction"""
    root_name: str
    asset_tags: List[str]
    ipfs_hashes: Optional[List[str]] = None

class RestrictedAssetIssue(BaseModel):
    """Model for restricted asset issuance in raw transaction"""
    asset_name: str
    asset_quantity: Decimal
    verifier: str
    units: int = Field(0, ge=0, le=8)
    reissuable: bool = True
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None

class QualifierAssetIssue(BaseModel):
    """Model for qualifier asset issuance in raw transaction"""
    asset_name: str
    asset_quantity: Decimal
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None

class AddressTagging(BaseModel):
    """Model for address tagging in raw transaction"""
    tag_name: str
    to_address: str
    asset_data: Optional[str] = None

class AddressFreezing(BaseModel):
    """Model for address freezing in raw transaction"""
    asset_name: str
    address: str
    asset_data: Optional[str] = None

class AssetFreezing(BaseModel):
    """Model for asset freezing in raw transaction"""
    asset_name: str
    asset_data: Optional[str] = None

# Request Models
class CreateRawTransactionRequest(BaseModel):
    """Request model for createrawtransaction RPC call"""
    inputs: List[Dict[str, Any]] = Field(..., min_items=1)
    outputs: Dict[str, Union[Decimal, Dict[str, Any]]]
    locktime: Optional[int] = None
    replaceable: Optional[bool] = None
    
    @validator('inputs')
    def validate_inputs(cls, v: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for input in v:
            if 'txid' not in input or 'vout' not in input:
                raise ValueError("Each input must contain 'txid' and 'vout'")
            if not isinstance(input['txid'], str) or len(input['txid']) != 64:
                raise ValueError("txid must be a 64-character hex string")
            if not isinstance(input['vout'], int) or input['vout'] < 0:
                raise ValueError("vout must be a non-negative integer")
        return v

class DecodeRawTransactionRequest(BaseModel):
    """Request model for decoderawtransaction RPC call"""
    hexstring: str
    iswitness: Optional[bool] = None

class SignRawTransactionRequest(BaseModel):
    """Request model for signrawtransactionwithkey RPC call"""
    hexstring: str
    privkeys: List[str]
    prevtxs: Optional[List[PrevTx]] = None
    sighashtype: SignatureHashType = SignatureHashType(sighash="ALL")

class SignRawTransactionResponse(BaseModel):
    """Response model for signrawtransactionwithkey RPC call"""
    hex: str
    complete: bool
    errors: Optional[List[Dict[str, Any]]] = None

class SendRawTransactionRequest(BaseModel):
    """Request model for sendrawtransaction RPC call"""
    hexstring: str
    maxfeerate: Optional[Decimal] = None

class TestMempoolAcceptRequest(BaseModel):
    """Request model for testmempoolaccept RPC call"""
    rawtxs: List[str]
    maxfeerate: Optional[Decimal] = None

class CombineRawTransactionRequest(BaseModel):
    """Request model for combinerawtransaction RPC call"""
    txs: List[str] = Field(..., min_items=2)

class AnalyzePsbtRequest(BaseModel):
    """Request model for analyzepsbt RPC call"""
    psbt: str

class DecodePsbtRequest(BaseModel):
    """Request model for decodepsbt RPC call"""
    psbt: str

class FinalizePsbtRequest(BaseModel):
    """Request model for finalizepsbt RPC call"""
    psbt: str
    extract: bool = True

__all__ = [
    # Models
    'PrevTx',
    'SignatureHashType',
    'AssetTransfer',
    'AssetIssue',
    'AssetReissue',
    'UniqueAssetIssue',
    'RestrictedAssetIssue',
    'QualifierAssetIssue',
    'AddressTagging',
    'AddressFreezing',
    'AssetFreezing',
    
    # Request/Response Models
    'CreateRawTransactionRequest',
    'DecodeRawTransactionRequest',
    'SignRawTransactionRequest',
    'SignRawTransactionResponse',
    'SendRawTransactionRequest',
    'TestMempoolAcceptRequest',
    'CombineRawTransactionRequest',
    'AnalyzePsbtRequest',
    'DecodePsbtRequest',
    'FinalizePsbtRequest'
] 