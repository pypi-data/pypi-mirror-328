"""Models for Evrmore RPC requests and responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator, field_validator, ConfigDict
from decimal import Decimal

from .base import (
    RPCRequest,
    RPCResponse,
    AddressParam,
    AmountParam,
    TransactionDetail,
    TransactionInput,
    TransactionOutput
)

from .wallet import *

__all__ = [
    'RPCRequest',
    'RPCResponse',
    'AddressParam',
    'AmountParam',
    'TransactionDetail',
    'TransactionInput',
    'TransactionOutput',
    
    # Response Models
    'WalletInfoResponse',
    'TransactionInfoResponse',
    'ReceivedByAddress',
    'ListSinceBlockTransaction',
    'ListSinceBlockResult',
    'MasterKeyInfo',
    'WalletWords',
    'UnspentOutput',
    'AddressGrouping',
    'ListReceivedByAddressResponse',
    'ListSinceBlockResponse',
    'ListTransactionsResponse',
    'ListAccountsResponse',
    'ListAddressGroupingsResponse',
    'RescanBlockchainResponse',
    
    # Request Models
    'AbandonTransactionRequest',
    'AddMultisigAddressRequest',
    'BackupWalletRequest',
    'GetBalanceRequest',
    'GetNewAddressRequest',
    'GetReceivedByAddressRequest',
    'GetTransactionRequest',
    'GetWalletInfoRequest',
    'ImportAddressRequest',
    'ListReceivedByAddressRequest',
    'ListSinceBlockRequest',
    'ListTransactionsRequest',
    'ListUnspentRequest',
    'SendToAddressRequest',
    'SetTxFeeRequest',
    'SignMessageRequest',
    'AbortRescanRequest',
    'GetAccountRequest',
    'GetAccountAddressRequest',
    'GetAddressesByAccountRequest',
    'GetMasterKeyInfoRequest',
    'GetMyWordsRequest',
    'GetReceivedByAccountRequest',
    'ImportMultiRequest',
    'ImportPrunedFundsRequest',
    'ListWalletsRequest',
    'MoveRequest',
    'RescanBlockchainRequest'
] 