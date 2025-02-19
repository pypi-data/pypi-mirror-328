"""ZMQ notification related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral, Union
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal
from ..base import BlockHashParam, TransactionHashParam
from datetime import datetime

class ZMQNotificationBase(BaseModel):
    """Base model for all ZMQ notifications"""
    model_config = ConfigDict(arbitrary_types_allowed=True)  # Allow bytes type
    
    topic: bytes = Field(..., description="ZMQ topic this notification was received on")
    sequence: int = Field(..., ge=0, description="Monotonically increasing sequence number")

class ZMQNotification(ZMQNotificationBase):
    """Base class for ZMQ notifications"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    topic: bytes = Field(..., description="Notification topic")
    sequence: int = Field(..., description="Notification sequence number")

class HashTxNotification(ZMQNotification):
    """Model for transaction hash notifications"""
    topic: TypeLiteral[b"hashtx"] = Field(b"hashtx")
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class RawTxNotification(ZMQNotification):
    """Model for raw transaction notifications"""
    topic: TypeLiteral[b"rawtx"] = Field(b"rawtx")
    txhex: str = Field(..., min_length=2)
    size: int = Field(..., gt=0)
    vsize: Optional[int] = None
    weight: Optional[int] = None

class HashBlockNotification(ZMQNotification):
    """Model for block hash notifications"""
    topic: TypeLiteral[b"hashblock"] = Field(b"hashblock")
    blockhash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class RawBlockNotification(ZMQNotification):
    """Model for raw block notifications"""
    topic: TypeLiteral[b"rawblock"] = Field(b"rawblock")
    blockhex: str = Field(..., min_length=2)
    size: int = Field(..., gt=0)
    height: Optional[int] = None
    version: Optional[int] = None
    merkleroot: Optional[str] = None
    time: Optional[int] = None
    nonce: Optional[int] = None
    bits: Optional[str] = None
    difficulty: Optional[Decimal] = None

class SequenceNotification(ZMQNotification):
    """Model for sequence notifications during chain reorganization"""
    topic: TypeLiteral[b"sequence"] = Field(b"sequence")
    height: int = Field(..., ge=0)
    blockhash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    is_reorg: bool = Field(False, description="Whether this is part of a chain reorganization")

class ZMQEndpoint(BaseModel):
    """Model for ZMQ endpoint configuration"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    address: str = Field(..., pattern="^tcp://[^:]+:\\d+$")
    topics: List[bytes] = Field(..., min_length=1)
    hwm: int = Field(1000, ge=0, description="High water mark for message queue")
    
    @field_validator('topics')
    def validate_topics(cls, v: List[bytes]) -> List[bytes]:
        """Validate ZMQ topics"""
        if not v:
            raise ValueError("Must provide at least one topic")
        valid_topics = {b"hashtx", b"rawtx", b"hashblock", b"rawblock", b"sequence"}
        for topic in v:
            if topic not in valid_topics:
                raise ValueError(f"Invalid topic: {topic}. Must be one of {valid_topics}")
        return v

class ZMQSubscription(BaseModel):
    """Model for ZMQ subscription"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    topics: List[bytes] = Field(..., min_length=1)
    endpoint: ZMQEndpoint
    active: bool = True
    last_sequence: Dict[bytes, int] = Field(default_factory=dict)
    connected: bool = Field(default=False, description="Whether the socket is connected")
    last_message: Optional[datetime] = Field(default=None, description="Time of last message received")

class ZMQStats(BaseModel):
    """Model for ZMQ statistics"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    total_notifications: int = 0
    notifications_by_topic: Dict[bytes, int] = Field(default_factory=dict)
    last_notification_time: Optional[int] = None
    active_subscriptions: int = 0
    dropped_notifications: int = 0
    reconnects: int = 0

class ZMQConfig(BaseModel):
    """Model for ZMQ configuration"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    endpoints: List[ZMQEndpoint]
    receive_timeout: int = Field(1000, ge=0, description="Socket receive timeout in milliseconds")
    reconnect_interval: int = Field(1000, ge=0, description="Time to wait before reconnecting in milliseconds")
    max_queued_notifications: int = Field(10000, ge=0, description="Maximum number of notifications to queue")

# Request Models
class GetZMQNotificationsRequest(BaseModel):
    """Request model for getzmqnotifications RPC call"""
    model_config = ConfigDict(extra='forbid')

# Response Models
class ZMQNotificationInfo(BaseModel):
    """Response model for getzmqnotifications RPC call"""
    model_config = ConfigDict(extra='allow')
    
    type: str
    address: str
    hwm: int

ZMQNotification = Union[
    HashTxNotification,
    RawTxNotification,
    HashBlockNotification,
    RawBlockNotification,
    SequenceNotification
]

__all__ = [
    # Base Models
    'ZMQNotificationBase',
    'ZMQEndpoint',
    'ZMQSubscription',
    'ZMQStats',
    'ZMQConfig',
    
    # Notification Models
    'HashTxNotification',
    'RawTxNotification',
    'HashBlockNotification',
    'RawBlockNotification',
    'SequenceNotification',
    'ZMQNotification',  # Union type
    
    # Request/Response Models
    'GetZMQNotificationsRequest',
    'ZMQNotificationInfo'
] 