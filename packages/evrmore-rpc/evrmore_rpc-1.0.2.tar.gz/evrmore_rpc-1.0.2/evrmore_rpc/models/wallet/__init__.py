"""Wallet related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator, field_validator, ConfigDict
from decimal import Decimal
from ..base import (
    AddressParam, 
    AmountParam, 
    TransactionDetail,
    TransactionInput,
    TransactionOutput
)

class WalletInfoResponse(BaseModel):
    """Model for wallet information"""
    model_config = ConfigDict(extra='allow')
    
    walletname: Optional[str] = None
    walletversion: int
    balance: Decimal
    unconfirmed_balance: Decimal
    immature_balance: Decimal
    txcount: int
    keypoololdest: int
    keypoolsize: int
    unlocked_until: Optional[int] = None
    paytxfee: Decimal
    hdmasterkeyid: Optional[str] = None

class TransactionInfoResponse(BaseModel):
    """Model for wallet transaction information"""
    model_config = ConfigDict(extra='allow')
    
    txid: str
    hash: str
    version: int
    size: int
    vsize: int
    weight: int
    locktime: int
    vin: List[TransactionInput]
    vout: List[TransactionOutput]
    hex: str
    blockhash: Optional[str] = None
    confirmations: Optional[int] = None
    time: Optional[int] = None
    blocktime: Optional[int] = None
    
    # Additional fields for wallet transactions
    amount: Optional[Decimal] = None
    fee: Optional[Decimal] = None
    blockindex: Optional[int] = None
    walletconflicts: Optional[List[str]] = None
    timereceived: Optional[int] = None
    bip125_replaceable: Optional[str] = None
    details: Optional[List[TransactionDetail]] = None
    comment: Optional[str] = None
    to: Optional[str] = None
    trusted: Optional[bool] = None

class ReceivedByAddress(BaseModel):
    """Model for received by address information"""
    address: str
    account: str
    amount: Decimal
    confirmations: int
    label: str
    txids: List[str]

class ListSinceBlockTransaction(BaseModel):
    """Model for transactions since block"""
    account: str
    address: str
    category: str
    amount: Decimal
    vout: int
    fee: Optional[Decimal]
    confirmations: int
    blockhash: str
    blockindex: int
    blocktime: int
    txid: str
    time: int
    timereceived: int
    comment: Optional[str]
    to: Optional[str]

class ListSinceBlockResult(BaseModel):
    """Model for list since block result"""
    transactions: List[ListSinceBlockTransaction]
    removed: Optional[List[ListSinceBlockTransaction]]
    lastblock: str

class MasterKeyInfo(BaseModel):
    """Model for master key information"""
    key: str
    path: str
    status: str

class WalletWords(BaseModel):
    """Model for wallet words"""
    mnemonic: str
    path: Optional[str]
    language: Optional[str]

# Request Models
class AbandonTransactionRequest(BaseModel):
    """Request model for abandontransaction RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class AddMultisigAddressRequest(BaseModel):
    """Request model for addmultisigaddress RPC call"""
    nrequired: int = Field(..., gt=0)
    keys: List[str]
    label: Optional[str] = None
    address_type: Optional[TypeLiteral["legacy", "p2sh-segwit", "bech32"]] = None

class BackupWalletRequest(BaseModel):
    """Request model for backupwallet RPC call"""
    destination: str

class GetBalanceRequest(BaseModel):
    """Request model for getbalance RPC call"""
    dummy: Optional[str] = None
    minconf: int = Field(1, ge=0)
    include_watchonly: bool = False

class GetNewAddressRequest(BaseModel):
    """Request model for getnewaddress RPC call"""
    label: Optional[str] = None
    address_type: Optional[TypeLiteral["legacy", "p2sh-segwit", "bech32"]] = None

class GetReceivedByAddressRequest(AddressParam):
    """Request model for getreceivedbyaddress RPC call"""
    minconf: int = Field(1, ge=0)

class GetTransactionRequest(BaseModel):
    """Request model for gettransaction RPC call"""
    method: str = "gettransaction"
    params: List[str]
    id: Optional[int] = None

class GetWalletInfoRequest(BaseModel):
    """Request model for getwalletinfo RPC call"""
    pass

class ImportAddressRequest(BaseModel):
    """Request model for importaddress RPC call"""
    address: str
    label: Optional[str] = None
    rescan: bool = True
    p2sh: bool = False

class ListReceivedByAddressRequest(BaseModel):
    """Request model for listreceivedbyaddress RPC call"""
    minconf: int = Field(1, ge=0)
    include_empty: bool = False
    include_watchonly: bool = False
    address_filter: Optional[str] = None

class ListSinceBlockRequest(BaseModel):
    """Request model for listsinceblock RPC call"""
    blockhash: Optional[str] = None
    target_confirmations: Optional[int] = None
    include_watchonly: bool = False
    include_removed: bool = True

class ListTransactionsRequest(BaseModel):
    """Request model for listtransactions RPC call"""
    label: Optional[str] = None
    count: int = Field(10, ge=0)
    skip: int = Field(0, ge=0)
    include_watchonly: bool = False

class ListUnspentRequest(BaseModel):
    """Request model for listunspent RPC call"""
    minconf: int = Field(1, ge=0)
    maxconf: int = Field(9999999, ge=0)
    addresses: Optional[List[str]] = None
    include_unsafe: bool = True
    query_options: Optional[Dict[str, Any]] = None

class SendToAddressRequest(BaseModel):
    """Request model for sendtoaddress RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    amount: Decimal = Field(..., ge=0)
    comment: Optional[str] = None
    comment_to: Optional[str] = None
    subtractfeefromamount: bool = False
    replaceable: bool = False
    conf_target: Optional[int] = None
    estimate_mode: Optional[TypeLiteral["UNSET", "ECONOMICAL", "CONSERVATIVE"]] = None
    avoid_reuse: bool = False

class SetTxFeeRequest(BaseModel):
    """Request model for settxfee RPC call"""
    amount: Decimal = Field(..., ge=0)

class SignMessageRequest(BaseModel):
    """Request model for signmessage RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    message: str

class AbortRescanRequest(BaseModel):
    """Request model for abortrescan RPC call"""
    pass

class GetAccountRequest(BaseModel):
    """Request model for getaccount RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")

class GetAccountAddressRequest(BaseModel):
    """Request model for getaccountaddress RPC call"""
    account: str

class GetAddressesByAccountRequest(BaseModel):
    """Request model for getaddressesbyaccount RPC call"""
    account: str

class GetMasterKeyInfoRequest(BaseModel):
    """Request model for getmasterkeyinfo RPC call"""
    pass

class GetMyWordsRequest(BaseModel):
    """Request model for getmywords RPC call"""
    account: Optional[str] = None

class GetReceivedByAccountRequest(BaseModel):
    """Request model for getreceivedbyaccount RPC call"""
    account: str
    minconf: int = Field(1, ge=0)

class ImportMultiRequest(BaseModel):
    """Request model for importmulti RPC call"""
    requests: List[Dict[str, Any]]
    options: Optional[Dict[str, Any]] = None

class ImportPrunedFundsRequest(BaseModel):
    """Request model for importprunedfunds RPC call"""
    rawtransaction: str
    txoutproof: str

class ListWalletsRequest(BaseModel):
    """Request model for listwallets RPC call"""
    pass

class MoveRequest(BaseModel):
    """Request model for move RPC call"""
    fromaccount: str
    toaccount: str
    amount: Decimal = Field(..., ge=0)
    minconf: Optional[int] = Field(1, ge=0)
    comment: Optional[str] = None

class RemovePrunedFundsRequest(BaseModel):
    """Request model for removeprunedfunds RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class RescanBlockchainRequest(BaseModel):
    """Request model for rescanblockchain RPC call"""
    start_height: Optional[int] = None
    stop_height: Optional[int] = None

class SendFromRequest(BaseModel):
    """Request model for sendfrom RPC call"""
    fromaccount: str
    toaddress: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    amount: Decimal = Field(..., ge=0)
    minconf: int = Field(1, ge=0)
    comment: Optional[str] = None
    comment_to: Optional[str] = None

class SendFromAddressRequest(BaseModel):
    """Request model for sendfromaddress RPC call"""
    from_address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    to_address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    amount: Decimal = Field(..., ge=0)
    comment: Optional[str] = None
    comment_to: Optional[str] = None
    subtractfeefromamount: bool = False
    replaceable: bool = False
    conf_target: Optional[int] = None
    estimate_mode: Optional[TypeLiteral["UNSET", "ECONOMICAL", "CONSERVATIVE"]] = None

class SetAccountRequest(BaseModel):
    """Request model for setaccount RPC call"""
    address: str = Field(..., min_length=34, max_length=34, pattern="^[E][a-km-zA-HJ-NP-Z1-9]{33}$")
    account: str

class AccountBalance(BaseModel):
    """Model for account balance"""
    account: str
    balance: Decimal
    watchonly: Optional[bool] = None

class AddressGrouping(BaseModel):
    """Model for address grouping"""
    address: str
    amount: Decimal
    account: Optional[str] = None

class UnspentOutput(BaseModel):
    """Model for unspent output"""
    txid: str
    vout: int
    address: str
    account: Optional[str] = None
    scriptPubKey: str
    amount: Decimal
    confirmations: int
    redeemScript: Optional[str] = None
    spendable: bool
    solvable: bool
    safe: bool

class ListAccountsResponse(BaseModel):
    """Response model for listaccounts RPC call"""
    model_config = ConfigDict(extra='allow')
    
    accounts: Dict[str, Decimal]
    
    @field_validator('accounts')
    def validate_accounts(cls, v: Dict[str, Decimal]) -> Dict[str, Decimal]:
        """Validate account balances"""
        for balance in v.values():
            if balance < 0:
                raise ValueError("Account balance cannot be negative")
        return v

class ListAddressGroupingsResponse(BaseModel):
    """Response model for listaddressgroupings RPC call"""
    groupings: List[List[AddressGrouping]]

class ListUnspentResponse(BaseModel):
    """Response model for listunspent RPC call"""
    outputs: List[UnspentOutput]

class ListReceivedByAddressResponse(BaseModel):
    """Response model for listreceivedbyaddress RPC call"""
    received: List[ReceivedByAddress]

class ListSinceBlockResponse(BaseModel):
    """Response model for listsinceblock RPC call"""
    transactions: List[ListSinceBlockTransaction]
    removed: Optional[List[ListSinceBlockTransaction]] = None
    lastblock: str

class ListTransactionsResponse(BaseModel):
    """Response model for listtransactions RPC call"""
    transactions: List[TransactionDetail]

__all__ = [
    # Models
    'WalletInfoResponse',
    'TransactionInfoResponse',
    'ReceivedByAddress',
    'ListSinceBlockTransaction',
    'ListSinceBlockResult',
    'MasterKeyInfo',
    'WalletWords',
    
    # Request Models
    'AbandonTransactionRequest',
    'AbortRescanRequest',
    'AddMultisigAddressRequest',
    'BackupWalletRequest',
    'GetAccountRequest',
    'GetAccountAddressRequest',
    'GetAddressesByAccountRequest',
    'GetBalanceRequest',
    'GetMasterKeyInfoRequest',
    'GetMyWordsRequest',
    'GetNewAddressRequest',
    'GetReceivedByAccountRequest',
    'GetReceivedByAddressRequest',
    'GetTransactionRequest',
    'GetWalletInfoRequest',
    'ImportAddressRequest',
    'ImportMultiRequest',
    'ImportPrunedFundsRequest',
    'ListReceivedByAddressRequest',
    'ListSinceBlockRequest',
    'ListTransactionsRequest',
    'ListUnspentRequest',
    'ListWalletsRequest',
    'MoveRequest',
    'RemovePrunedFundsRequest',
    'RescanBlockchainRequest',
    'SendFromRequest',
    'SendFromAddressRequest',
    'SendToAddressRequest',
    'SetAccountRequest',
    'SetTxFeeRequest',
    'SignMessageRequest',
    
    # Response Models
    'AccountBalance',
    'AddressGrouping',
    'UnspentOutput',
    'ListAccountsResponse',
    'ListAddressGroupingsResponse',
    'ListUnspentResponse',
    'ListReceivedByAddressResponse',
    'ListSinceBlockResponse',
    'ListTransactionsResponse'
] 