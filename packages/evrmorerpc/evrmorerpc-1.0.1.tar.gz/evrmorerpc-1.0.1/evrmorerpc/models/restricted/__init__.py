"""Restricted asset related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam,
    AssetNameParam,
    IPFSHashParam,
    UnitsParam
)

class VerifierString(BaseModel):
    """Model for verifier string"""
    string: str
    active: bool

class AddressRestriction(BaseModel):
    """Model for address restriction"""
    addresses: List[str]
    restricted: bool
    time: int
    txid: str
    
class GlobalRestriction(BaseModel):
    """Model for global restriction"""
    restricted: bool
    time: int
    txid: str

class QualifierAddress(BaseModel):
    """Model for qualifier address"""
    address: str
    tag: str
    time: int
    txid: str

# Request Models
class IssueRestrictedAssetRequest(BaseModel):
    """Request model for issuerestrictedasset RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._$]{3,}$")
    qty: Decimal = Field(..., gt=0)
    verifier: str
    to_address: Optional[str] = None
    change_address: Optional[str] = None
    units: int = Field(0, ge=0, le=8)
    reissuable: bool = True
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None
    
    @validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if not v.startswith("$"):
            raise ValueError("Restricted asset name must start with $")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class ReissueRestrictedAssetRequest(BaseModel):
    """Request model for reissuerestrictedasset RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")
    qty: Decimal = Field(..., gt=0)
    to_address: Optional[str] = None
    change_address: Optional[str] = None
    reissuable: Optional[bool] = None
    verifier: Optional[str] = None
    ipfs_hash: Optional[str] = None

class IssueQualifierAssetRequest(BaseModel):
    """Request model for issuequalifierasset RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._#]{3,}$")
    qty: Decimal = Field(..., gt=0)
    to_address: Optional[str] = None
    change_address: Optional[str] = None
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None
    
    @validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if not v.startswith("#"):
            raise ValueError("Qualifier asset name must start with #")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class AddTagToAddressRequest(BaseModel):
    """Request model for addtagtoaddress RPC call"""
    tag_name: str = Field(..., min_length=3, pattern="^#[A-Z0-9._]{3,}$")
    to_address: str
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class RemoveTagFromAddressRequest(BaseModel):
    """Request model for removetagfromaddress RPC call"""
    tag_name: str = Field(..., min_length=3, pattern="^#[A-Z0-9._]{3,}$")
    to_address: str
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class FreezeAddressRequest(BaseModel):
    """Request model for freezeaddress RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")
    address: str
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class UnfreezeAddressRequest(BaseModel):
    """Request model for unfreezeaddress RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")
    address: str
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class FreezeRestrictedAssetRequest(BaseModel):
    """Request model for freezerestrictedasset RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class UnfreezeRestrictedAssetRequest(BaseModel):
    """Request model for unfreezerestrictedasset RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")
    change_address: Optional[str] = None
    asset_data: Optional[str] = None

class ListAddressRestrictionsRequest(BaseModel):
    """Request model for listaddressrestrictions RPC call"""
    address: str
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class ListGlobalRestrictionsRequest(BaseModel):
    """Request model for listglobalrestrictions RPC call"""
    asset_name: Optional[str] = None
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class ListQualifierAddressesRequest(BaseModel):
    """Request model for listqualifieraddresses RPC call"""
    qualifier: str = Field(..., min_length=3, pattern="^#[A-Z0-9._]{3,}$")
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class CheckAddressRestrictionRequest(BaseModel):
    """Request model for checkaddressrestriction RPC call"""
    address: str
    restricted_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")

class CheckGlobalRestrictionRequest(BaseModel):
    """Request model for checkglobalrestriction RPC call"""
    restricted_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")

class CheckAddressTagRequest(BaseModel):
    """Request model for checkaddresstag RPC call"""
    address: str
    qualifier_name: str = Field(..., min_length=3, pattern="^#[A-Z0-9._]{3,}$")

class GetVerifierStringRequest(BaseModel):
    """Request model for getverifierstring RPC call"""
    restricted_name: str = Field(..., min_length=3, pattern="^\\$[A-Z0-9._]{3,}$")

class RestrictedAddressInfo(BaseModel):
    """Model for restricted address information"""
    address: str
    restricted_name: str
    restricted: bool
    from_height: int
    timestamp: int

class TaggedAddressInfo(BaseModel):
    """Model for tagged address information"""
    address: str
    tag_name: str
    from_height: int
    timestamp: int

class ViewMyRestrictedAddressesRequest(BaseModel):
    """Request model for viewmyrestrictedaddresses RPC call"""
    pass

class ViewMyTaggedAddressesRequest(BaseModel):
    """Request model for viewmytaggedaddresses RPC call"""
    pass

__all__ = [
    # Models
    'VerifierString',
    'AddressRestriction',
    'GlobalRestriction',
    'QualifierAddress',
    'RestrictedAddressInfo',
    'TaggedAddressInfo',
    
    # Request Models
    'IssueRestrictedAssetRequest',
    'ReissueRestrictedAssetRequest',
    'IssueQualifierAssetRequest',
    'AddTagToAddressRequest',
    'RemoveTagFromAddressRequest',
    'FreezeAddressRequest',
    'UnfreezeAddressRequest',
    'FreezeRestrictedAssetRequest',
    'UnfreezeRestrictedAssetRequest',
    'ListAddressRestrictionsRequest',
    'ListGlobalRestrictionsRequest',
    'ListQualifierAddressesRequest',
    'CheckAddressRestrictionRequest',
    'CheckGlobalRestrictionRequest',
    'CheckAddressTagRequest',
    'GetVerifierStringRequest',
    'ViewMyRestrictedAddressesRequest',
    'ViewMyTaggedAddressesRequest'
] 