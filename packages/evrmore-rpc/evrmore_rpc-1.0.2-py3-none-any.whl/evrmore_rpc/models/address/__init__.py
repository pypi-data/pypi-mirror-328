"""Address related models for RPC requests/responses"""
from typing import Dict, List, Optional, Union
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class AddressParam(BaseModel):
    """Model for address parameters"""
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "address": "EXaMPLEaDDreSS123456789"
        }
    })
    
    address: str = Field(..., description="The Evrmore address")

class AddressBalance(BaseModel):
    """Model for address balance"""
    model_config = ConfigDict(extra='allow')

__all__ = [
    'AddressParam'
] 