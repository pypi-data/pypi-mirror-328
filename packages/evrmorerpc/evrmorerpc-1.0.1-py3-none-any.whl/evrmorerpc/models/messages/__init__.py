"""Message related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam
)

class MessageChannel(BaseModel):
    """Model for message channel"""
    name: str
    time: int
    expires: Optional[int] = None
    message_type: Literal["channel", "message", "verifier", "restriction", "qualifier", "tag", "freeze"]
    description: Optional[str] = None
    restricted: bool = False
    from_address: Optional[str] = None
    to_address: Optional[str] = None

class Message(BaseModel):
    """Model for message"""
    timestamp: int
    message: str
    expires: Optional[int] = None
    channel: str
    from_address: str
    to_address: Optional[str] = None
    asset_name: Optional[str] = None
    txid: str
    verified: bool = False

# Request Models
class ClearMessagesRequest(BaseModel):
    """Request model for clearmessages RPC call"""
    pass

class SendMessageRequest(BaseModel):
    """Request model for sendmessage RPC call"""
    channel_name: str = Field(..., min_length=1)
    ipfs_hash: str = Field(..., min_length=46, max_length=46, pattern="^Qm[a-zA-Z0-9]{44}$")
    expire_time: Optional[int] = None
    
    @validator('channel_name')
    def validate_channel_name(cls, v: str) -> str:
        if len(v) > 12:
            raise ValueError("Channel name cannot be longer than 12 characters")
        if not v.isalnum() and not "_" in v:
            raise ValueError("Channel name can only contain alphanumeric characters and underscores")
        return v

class SubscribeToChannelRequest(BaseModel):
    """Request model for subscribetochannel RPC call"""
    channel_name: str = Field(..., min_length=1)
    
    @validator('channel_name')
    def validate_channel_name(cls, v: str) -> str:
        if len(v) > 12:
            raise ValueError("Channel name cannot be longer than 12 characters")
        if not v.isalnum() and not "_" in v:
            raise ValueError("Channel name can only contain alphanumeric characters and underscores")
        return v

class UnsubscribeFromChannelRequest(BaseModel):
    """Request model for unsubscribefromchannel RPC call"""
    channel_name: str = Field(..., min_length=1)

class ViewAllMessageChannelsRequest(BaseModel):
    """Request model for viewallmessagechannels RPC call"""
    pass

class ViewAllMessagesRequest(BaseModel):
    """Request model for viewallmessages RPC call"""
    from_time: Optional[int] = None
    to_time: Optional[int] = None
    limit: Optional[int] = Field(None, ge=1, le=100)
    offset: Optional[int] = Field(None, ge=0)

class ListMessagesRequest(BaseModel):
    """Request model for listmessages RPC call"""
    channel_name: Optional[str] = None
    from_time: Optional[int] = None
    to_time: Optional[int] = None
    from_address: Optional[str] = None
    to_address: Optional[str] = None
    limit: Optional[int] = Field(None, ge=1, le=100)
    offset: Optional[int] = Field(None, ge=0)
    
    @validator('channel_name')
    def validate_channel_name(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if len(v) > 12:
                raise ValueError("Channel name cannot be longer than 12 characters")
            if not v.isalnum() and not "_" in v:
                raise ValueError("Channel name can only contain alphanumeric characters and underscores")
        return v

class ListChannelsRequest(BaseModel):
    """Request model for listchannels RPC call"""
    channel_name: Optional[str] = None
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class GetMessageByTxidRequest(BaseModel):
    """Request model for getmessagebytxid RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class GetMessagesByAddressRequest(BaseModel):
    """Request model for getmessagesbyaddress RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    from_time: Optional[int] = None
    to_time: Optional[int] = None
    limit: Optional[int] = Field(None, ge=1, le=100)
    offset: Optional[int] = Field(None, ge=0)

__all__ = [
    # Models
    'MessageChannel',
    'Message',
    
    # Request Models
    'ClearMessagesRequest',
    'SendMessageRequest',
    'SubscribeToChannelRequest',
    'UnsubscribeFromChannelRequest',
    'ViewAllMessageChannelsRequest',
    'ViewAllMessagesRequest',
    'ListMessagesRequest',
    'ListChannelsRequest',
    'GetMessageByTxidRequest',
    'GetMessagesByAddressRequest'
] 