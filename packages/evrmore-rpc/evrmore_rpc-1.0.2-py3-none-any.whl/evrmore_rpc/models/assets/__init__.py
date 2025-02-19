"""Asset related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral, Union
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal
from ..base import (
    AddressParam,
    AmountParam,
    AssetNameParam,
    IPFSHashParam,
    UnitsParam
)

class AssetInfoResponse(BaseModel):
    """Model for asset data"""
    model_config = ConfigDict(extra='allow')
    
    name: str
    amount: Union[int, Decimal]  # Can be int or decimal depending on units
    units: int
    reissuable: Union[int, bool]  # Can be 0/1 or True/False
    has_ipfs: Union[int, bool]    # Can be 0/1 or True/False
    block_height: Optional[int] = None
    blockhash: Optional[str] = None
    txid: Optional[str] = None
    verifier_string: Optional[str] = None
    ipfs_hash: Optional[str] = None
    owner: Optional[str] = None
    divisible: Optional[bool] = None
    locked: Optional[bool] = None
    source: Optional[str] = None

class AssetAllocation(BaseModel):
    """Model for asset allocation"""
    asset_name: str
    owner: str
    amount: Decimal
    raw_amount: int
    locked: bool

class AssetHolder(BaseModel):
    """Model for asset holder"""
    address: str
    amount: Decimal
    raw_amount: int
    locked: bool

class SnapshotResult(BaseModel):
    """Model for getsnapshot RPC response"""
    model_config = ConfigDict(extra='allow')
    
    name: str
    height: int
    owners: List[AssetHolder]
    total: Decimal
    divisibility: int
    ipfs_hash: Optional[str] = None
    reissuable: bool

# Request Models
class IssueAssetRequest(BaseModel):
    """Request model for issue RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    qty: Decimal = Field(..., gt=0)
    to_address: Optional[str] = None
    change_address: Optional[str] = None
    units: int = Field(0, ge=0, le=8)
    reissuable: bool = True
    has_ipfs: bool = False
    ipfs_hash: Optional[str] = None
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            raise ValueError("Cannot issue EVR as an asset")
        if not v[0].isalpha():
            raise ValueError("Asset name must start with a letter")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class ReissueAssetRequest(BaseModel):
    """Request model for reissue RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    qty: Decimal = Field(..., gt=0)
    to_address: Optional[str] = None
    change_address: Optional[str] = None
    reissuable: Optional[bool] = None
    ipfs_hash: Optional[str] = None
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            raise ValueError("Cannot reissue EVR")
        return v

class TransferAssetRequest(BaseModel):
    """Request model for transfer RPC call"""
    method: str = "transfer"
    params: List[Union[str, int, Decimal]]
    id: Optional[int] = None

class ListAssetsRequest(BaseModel):
    """Request model for listassets RPC call"""
    asset: Optional[str] = None
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class ListAssetBalancesRequest(BaseModel):
    """Request model for listassetbalances RPC call"""
    asset: Optional[str] = None
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None
    
class ListAddressesForAssetRequest(BaseModel):
    """Request model for listaddressesforasset RPC call"""
    asset_name: str
    onlytotal: bool = False
    count: Optional[int] = None
    start: Optional[int] = None

class GetAssetDataRequest(BaseModel):
    """Request model for getassetdata RPC call"""
    method: str = "getassetdata"
    params: List[str]
    id: Optional[int] = None

class GetAssetsForAddressRequest(AddressParam):
    """Request model for getassetsforaddress RPC call"""
    pass

class BurnAssetRequest(BaseModel):
    """Request model for burnasset RPC call"""
    asset_name: str
    qty: Decimal
    change_address: Optional[str] = None
    asset_change_address: Optional[str] = None

class ListBurnHistoryRequest(BaseModel):
    """Request model for listburnhistory RPC call"""
    asset_name: Optional[str] = None
    blocks: Optional[int] = None
    count: Optional[int] = None
    start: Optional[int] = None

class ListAssetTransactionsRequest(BaseModel):
    """Request model for listassettransactions RPC call"""
    asset_name: str
    verbose: bool = False
    count: Optional[int] = None
    start: Optional[int] = None
    
class GetAssetMetadataRequest(BaseModel):
    """Request model for getassetmetadata RPC call"""
    asset_name: str
    txid: Optional[str] = None

class PurgeSnapshotRequest(BaseModel):
    """Request model for purgesnapshot RPC call"""
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    block_height: int = Field(..., ge=0)
    
    @field_validator('asset_name')
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            raise ValueError("Cannot purge snapshot for EVR")
        if not v[0].isalpha():
            raise ValueError("Asset name must start with a letter")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class AssetData(BaseModel):
    """Model for asset data"""
    model_config = ConfigDict(extra='allow')

__all__ = [
    # Models
    'AssetInfoResponse',
    'AssetAllocation',
    'AssetHolder',
    'SnapshotResult',
    
    # Request Models
    'IssueAssetRequest',
    'ReissueAssetRequest',
    'TransferAssetRequest',
    'ListAssetsRequest',
    'ListAssetBalancesRequest',
    'ListAddressesForAssetRequest',
    'GetAssetDataRequest',
    'GetAssetsForAddressRequest',
    'BurnAssetRequest',
    'ListBurnHistoryRequest',
    'ListAssetTransactionsRequest',
    'GetAssetMetadataRequest',
    'PurgeSnapshotRequest'
] 