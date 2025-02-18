"""Reward related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam,
    AssetNameParam
)

class DistributionStatus(BaseModel):
    """Model for distribution status"""
    status: TypeLiteral["invalid", "valid", "processing", "complete", "failed", "cancelled", "unknown"]
    asset_name: str
    block_height: int
    snapshot_height: Optional[int] = None
    distribution_amount: Optional[Decimal] = None
    recipients_count: Optional[int] = None
    processed_count: Optional[int] = None
    total_amount_sent: Optional[Decimal] = None
    reward_asset_name: Optional[str] = None
    error: Optional[str] = None
    processing_started_time: Optional[int] = None
    processing_ended_time: Optional[int] = None
    canceled_time: Optional[int] = None

class SnapshotResult(BaseModel):
    """Model for snapshot result"""
    asset_name: str
    block_height: int
    snapshot_height: int
    valid: bool
    error: Optional[str] = None
    total_addresses: Optional[int] = None
    total_amount: Optional[Decimal] = None
    distributions: Optional[List[DistributionStatus]] = None

class SnapshotAddress(BaseModel):
    """Model for snapshot address"""
    address: str
    amount: Decimal
    raw_amount: int
    locked: bool

# Request Models
class RequestSnapshotRequest(BaseModel):
    """Request model for requestsnapshot RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    block_height: Optional[int] = None
    
    @validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            raise ValueError("Cannot request snapshot for EVR")
        if not v[0].isalpha():
            raise ValueError("Asset name must start with a letter")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class GetSnapshotRequest(BaseModel):
    """Request model for getsnapshot RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    block_height: Optional[int] = None

class ListSnapshotsRequest(BaseModel):
    """Request model for listsnapshots RPC call"""
    asset_name: Optional[str] = None
    block_height: Optional[int] = None
    count: Optional[int] = None
    start: Optional[int] = None
    verbose: bool = False

class DistributeRewardRequest(BaseModel):
    """Request model for distributereward RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    snapshot_height: int
    distribution_asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    gross_distribution_amount: Decimal = Field(..., gt=0)
    exception_addresses: Optional[List[str]] = None
    change_address: Optional[str] = None
    dry_run: bool = False

class GetDistributeStatusRequest(BaseModel):
    """Request model for getdistributestatus RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    snapshot_height: Optional[int] = None
    verbose: bool = False

class CancelDistributeRequest(BaseModel):
    """Request model for canceldistribute RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    snapshot_height: int

__all__ = [
    # Models
    'DistributionStatus',
    'SnapshotResult',
    'SnapshotAddress',
    
    # Request Models
    'RequestSnapshotRequest',
    'GetSnapshotRequest',
    'ListSnapshotsRequest',
    'DistributeRewardRequest',
    'GetDistributeStatusRequest',
    'CancelDistributeRequest'
] 