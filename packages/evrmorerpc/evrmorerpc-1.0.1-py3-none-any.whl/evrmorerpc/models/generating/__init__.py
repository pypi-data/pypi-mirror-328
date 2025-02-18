"""Generating related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal

class GeneratedBlock(BaseModel):
    """Model for generated block"""
    hash: str
    height: int
    confirmations: int
    size: int
    weight: int
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
    previousblockhash: Optional[str]
    nextblockhash: Optional[str]

# Request Models
class GenerateRequest(BaseModel):
    """Request model for generate RPC call"""
    nblocks: int = Field(..., gt=0, le=1000000)
    maxtries: Optional[int] = None

class GenerateToAddressRequest(BaseModel):
    """Request model for generatetoaddress RPC call"""
    nblocks: int = Field(..., gt=0, le=1000000)
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    maxtries: Optional[int] = None

class GetGenerateRequest(BaseModel):
    """Request model for getgenerate RPC call"""
    pass

class SetGenerateRequest(BaseModel):
    """Request model for setgenerate RPC call"""
    generate: bool
    genproclimit: Optional[int] = Field(None, ge=-1)

# Response Models
class GetGenerateResponse(BaseModel):
    """Response model for getgenerate RPC call"""
    generate: bool
    genproclimit: int
    generatepos: bool

__all__ = [
    # Models
    'GeneratedBlock',
    'GetGenerateResponse',
    
    # Request Models
    'GenerateRequest',
    'GenerateToAddressRequest',
    'GetGenerateRequest',
    'SetGenerateRequest'
] 