"""Validation related models for RPC requests/responses"""
from typing import Optional, List
from pydantic import BaseModel, Field

class ValidateAddressResult(BaseModel):
    """Model for validateaddress RPC response"""
    isvalid: bool
    address: Optional[str] = None
    scriptPubKey: Optional[str] = None
    ismine: Optional[bool] = None
    iswatchonly: Optional[bool] = None
    isscript: Optional[bool] = None
    script: Optional[str] = None
    hex: Optional[str] = None
    addresses: Optional[List[str]] = None
    sigsrequired: Optional[int] = None
    pubkey: Optional[str] = None
    iscompressed: Optional[bool] = None
    account: Optional[str] = None
    timestamp: Optional[int] = None
    hdkeypath: Optional[str] = None
    hdmasterkeyid: Optional[str] = None

__all__ = [
    'ValidateAddressResult'
] 