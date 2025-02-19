"""Base models and common parameters for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, field_validator, ConfigDict
from decimal import Decimal

# Base RPC Models
class RPCRequest(BaseModel):
    """Base model for RPC requests"""
    model_config = ConfigDict(extra='allow')
    
    jsonrpc: TypeLiteral["2.0"] = "2.0"
    method: str
    params: List[Any] = Field(default_factory=list)
    id: int

class RPCResponse(BaseModel):
    """Base model for RPC responses"""
    model_config = ConfigDict(extra='allow')
    
    jsonrpc: TypeLiteral["2.0"] = "2.0"
    result: Any
    error: Optional[Dict[str, Any]] = None
    id: int

class RPCError(BaseModel):
    """Model for RPC error responses"""
    model_config = ConfigDict(extra='allow')
    
    code: int
    message: str
    method: Optional[str] = None

# Common Parameter Models
class BlockHashParam(BaseModel):
    """Model for block hash parameter"""
    model_config = ConfigDict(extra='allow')
    
    block_hash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class BlockHeightParam(BaseModel):
    """Model for block height parameter"""
    model_config = ConfigDict(extra='allow')
    
    height: int = Field(..., ge=0)

class TransactionHashParam(BaseModel):
    """Model for transaction hash parameter"""
    model_config = ConfigDict(extra='allow')
    
    tx_hash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class AddressParam(BaseModel):
    """Model for Evrmore address parameter"""
    model_config = ConfigDict(extra='allow')
    
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")

class AssetNameParam(BaseModel):
    """Model for asset name parameter"""
    model_config = ConfigDict(extra='allow')
    
    asset_name: str = Field(..., min_length=3, pattern="^[A-Z0-9._]{3,}$")
    
    @field_validator('asset_name')
    @classmethod
    def validate_asset_name(cls, v: str) -> str:
        if v == "EVR":
            return v
        if not v[0].isalpha():
            raise ValueError("Asset name must start with a letter")
        if ".." in v:
            raise ValueError("Asset name cannot contain consecutive dots")
        if v.endswith("."):
            raise ValueError("Asset name cannot end with a dot")
        return v

class IPFSHashParam(BaseModel):
    """Model for IPFS hash parameter"""
    model_config = ConfigDict(extra='allow')
    
    ipfs_hash: str = Field(..., min_length=46, max_length=46, pattern="^Qm[a-zA-Z0-9]{44}$")

class AmountParam(BaseModel):
    """Model for amount parameter"""
    model_config = ConfigDict(extra='allow')
    
    amount: Decimal = Field(..., ge=0)

class UnitsParam(BaseModel):
    """Model for units parameter"""
    model_config = ConfigDict(extra='allow')
    
    units: int = Field(..., ge=0, le=8)

class FeeEstimateModeParam(BaseModel):
    """Model for fee estimate mode parameter"""
    model_config = ConfigDict(extra='allow')
    
    estimate_mode: TypeLiteral["UNSET", "ECONOMICAL", "CONSERVATIVE"] = "UNSET"

# Common Transaction Models
class ScriptPubKey(BaseModel):
    """Model for scriptPubKey in transaction outputs"""
    model_config = ConfigDict(extra='allow')
    
    asm: str
    hex: str
    reqSigs: Optional[int]
    type: str
    addresses: Optional[List[str]]

class TransactionInput(BaseModel):
    """Model for transaction inputs"""
    model_config = ConfigDict(extra='allow')
    
    txid: str
    vout: int
    scriptSig: Dict[str, str]
    sequence: int
    txinwitness: Optional[List[str]]

class TransactionOutput(BaseModel):
    """Model for transaction outputs"""
    model_config = ConfigDict(extra='allow')
    
    value: Decimal
    n: int
    scriptPubKey: ScriptPubKey

class TransactionDetail(BaseModel):
    """Model for transaction detail"""
    model_config = ConfigDict(extra='allow')
    
    account: str
    address: str
    category: str
    amount: Decimal
    label: str
    vout: int
    fee: Optional[Decimal] = None
    abandoned: Optional[bool] = None

__all__ = [
    # Base Models
    'RPCRequest',
    'RPCResponse',
    'RPCError',
    
    # Parameter Models
    'BlockHashParam',
    'BlockHeightParam',
    'TransactionHashParam',
    'AddressParam',
    'AssetNameParam',
    'IPFSHashParam',
    'AmountParam',
    'UnitsParam',
    'FeeEstimateModeParam',
    
    # Transaction Models
    'ScriptPubKey',
    'TransactionInput',
    'TransactionOutput',
    'TransactionDetail'
] 