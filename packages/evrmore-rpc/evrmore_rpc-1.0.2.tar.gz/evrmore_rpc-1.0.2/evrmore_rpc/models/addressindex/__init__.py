"""Address index related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal
from ..base import AddressParam

class AddressBalance(BaseModel):
    """Model for address balance information"""
    model_config = ConfigDict(extra='allow')
    
    balance: Decimal
    received: Decimal

class AddressDelta(BaseModel):
    """Model for address delta information"""
    model_config = ConfigDict(extra='allow')
    
    satoshis: int
    txid: str
    index: int
    blockindex: int
    height: int
    address: str

class AddressUnspent(BaseModel):
    """Model for address unspent"""
    model_config = ConfigDict(extra='allow')
    
    txid: str
    outputIndex: int
    script: str
    satoshis: int
    height: int

class AddressMempoolEntry(BaseModel):
    """Model for address mempool entry"""
    model_config = ConfigDict(extra='allow')
    
    address: str
    txid: str
    index: int
    satoshis: int
    timestamp: int
    prevtxid: Optional[str] = None
    prevout: Optional[int] = None

class AddressUtxo(BaseModel):
    """Model for address UTXO information"""
    model_config = ConfigDict(extra='allow')
    
    address: str
    txid: str
    outputIndex: int
    script: str
    satoshis: int
    height: int

# Request Models
class GetAddressBalanceRequest(BaseModel):
    """Request model for getaddressbalance RPC call"""
    model_config = ConfigDict(extra='allow')
    
    addresses: List[str] = Field(..., min_length=1)
    
    @field_validator('addresses')
    @classmethod
    def validate_addresses(cls, v: List[str]) -> List[str]:
        if not all(addr.strip() for addr in v):
            raise ValueError("All addresses must be non-empty strings")
        return v

class GetAddressDeltasRequest(BaseModel):
    """Request model for getaddressdeltas RPC call"""
    model_config = ConfigDict(extra='allow')
    
    addresses: List[str] = Field(..., min_length=1)
    start: Optional[int] = None
    end: Optional[int] = None
    chainInfo: Optional[bool] = None
    
    @field_validator('addresses')
    @classmethod
    def validate_addresses(cls, v: List[str]) -> List[str]:
        if not all(addr.strip() for addr in v):
            raise ValueError("All addresses must be non-empty strings")
        return v

class GetAddressMempoolRequest(BaseModel):
    """Request model for getaddressmempool RPC call"""
    model_config = ConfigDict(extra='allow')
    
    addresses: List[str] = Field(..., min_length=1)
    
    @field_validator('addresses')
    @classmethod
    def validate_addresses(cls, v: List[str]) -> List[str]:
        if not all(addr.strip() for addr in v):
            raise ValueError("All addresses must be non-empty strings")
        return v

class GetAddressTxidsRequest(BaseModel):
    """Request model for getaddresstxids RPC call"""
    model_config = ConfigDict(extra='allow')
    
    addresses: List[str] = Field(..., min_length=1)
    start: Optional[int] = None
    end: Optional[int] = None
    
    @field_validator('addresses')
    @classmethod
    def validate_addresses(cls, v: List[str]) -> List[str]:
        if not all(addr.strip() for addr in v):
            raise ValueError("All addresses must be non-empty strings")
        return v

class GetAddressUtxosRequest(BaseModel):
    """Request model for getaddressutxos RPC call"""
    model_config = ConfigDict(extra='allow')
    
    addresses: List[str] = Field(..., min_length=1)
    chainInfo: Optional[bool] = None
    
    @field_validator('addresses')
    @classmethod
    def validate_addresses(cls, v: List[str]) -> List[str]:
        if not all(addr.strip() for addr in v):
            raise ValueError("All addresses must be non-empty strings")
        return v

__all__ = [
    # Models
    'AddressBalance',
    'AddressDelta',
    'AddressUnspent',
    'AddressMempoolEntry',
    'AddressUtxo',
    
    # Request Models
    'GetAddressBalanceRequest',
    'GetAddressDeltasRequest',
    'GetAddressMempoolRequest',
    'GetAddressTxidsRequest',
    'GetAddressUtxosRequest'
] 