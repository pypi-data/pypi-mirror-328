"""Rewards related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam,
    AssetNameParam
)

class SnapshotRequest(BaseModel):
    """Model for snapshot request"""
    model_config = ConfigDict(extra='allow')
    
    asset_name: str
    block_height: int
    status: str
    timestamp: int
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        """Validate asset name format"""
        if not v.strip():
            raise ValueError("Asset name cannot be empty")
        return v

class DistributionStatus(BaseModel):
    """Model for distribution status"""
    model_config = ConfigDict(extra='allow')
    
    asset_name: str
    block_height: int
    status: str
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        """Validate asset name format"""
        if not v.strip():
            raise ValueError("Asset name cannot be empty")
        return v

class SnapshotResult(BaseModel):
    """Model for snapshot result"""
    model_config = ConfigDict(extra='allow')
    
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
    model_config = ConfigDict(extra='allow')
    
    address: str
    amount: Decimal
    raw_amount: int
    locked: bool

# Request Models
class CancelSnapshotRequest(BaseModel):
    """Request model for cancelsnapshotrequest RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    asset_name: str
    block_height: int
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        """Validate asset name format"""
        if not v.strip():
            raise ValueError("Asset name must be non-empty")
        return v

class DistributeRewardRequest(BaseModel):
    """Model for distribute reward request"""
    model_config = ConfigDict(extra='allow')
    
    asset_name: str
    snapshot_height: int
    distribution_asset_name: str
    gross_distribution_amount: Decimal
    exception_addresses: Optional[List[str]] = None
    change_address: Optional[str] = None
    dry_run: bool = False
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        """Validate asset name format"""
        if not v.strip():
            raise ValueError("Asset name cannot be empty")
        return v

class GetDistributeStatusRequest(BaseModel):
    """Request model for getdistributestatus RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    asset_name: str
    snapshot_height: int
    distribution_asset_name: str
    gross_distribution_amount: Decimal
    exception_addresses: Optional[List[str]] = None

class GetSnapshotRequest(BaseModel):
    """Request model for getsnapshotrequest RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    asset_name: str
    block_height: int

class ListSnapshotRequestsRequest(BaseModel):
    """Request model for listsnapshotrequests RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    asset_name: Optional[str] = None
    block_height: Optional[int] = None

class RequestSnapshotRequest(BaseModel):
    """Request model for requestsnapshot RPC call"""
    model_config = ConfigDict(extra='forbid')
    
    asset_name: str
    block_height: int
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        """Validate asset name format"""
        if not v.strip():
            raise ValueError("Asset name must be non-empty")
        return v

__all__ = [
    # Models
    'SnapshotRequest',
    'DistributionStatus',
    'SnapshotResult',
    'SnapshotAddress',
    
    # Request Models
    'CancelSnapshotRequest',
    'DistributeRewardRequest',
    'GetDistributeStatusRequest',
    'GetSnapshotRequest',
    'ListSnapshotRequestsRequest',
    'RequestSnapshotRequest'
] 