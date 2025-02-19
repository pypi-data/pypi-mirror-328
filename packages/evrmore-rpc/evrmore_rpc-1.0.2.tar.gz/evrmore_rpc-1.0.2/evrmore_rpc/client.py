"""Evrmore RPC client implementation"""
import os
import requests
import time
from typing import Any, Dict, Optional, List, Union
from decimal import Decimal
from pathlib import Path
from pydantic import ValidationError

from evrmore_rpc.errors import NodeConnectionError, NodeAuthError, EvrmoreError
from evrmore_rpc.methods import RPCMethod
from evrmore_rpc.config import load_config, EvrmoreConfigError, EvrmoreConfig
from evrmore_rpc.models.base import RPCRequest, RPCResponse, TransactionInput, TransactionOutput
from evrmore_rpc.models.blockchain import (
    BlockInfoResponse,
    GetBlockRequest,
    GetBlockHashRequest,
    BlockHeaderResponse,
    MempoolInfoResponse,
    BlockchainInfoResponse,
    ChainTip,
    GetRawMempoolRequest,
    GetTxOutRequest,
    GetTxOutSetInfoRequest,
    VerifyChainRequest,
    GetBlockHeaderRequest,
    MempoolEntry,
    BlockHeader,
    BlockStats,
    ChainTxStats,
    DecodedBlock,
    SpentInfo,
    TxOutProof,
    MempoolAncestorsResponse,
    MempoolDescendantsResponse,
    TxOutProofResponse,
    VerifyTxOutProofResponse,
    ClearMemPoolRequest,
    DecodeBlockRequest,
    GetBlockHashesRequest,
    GetChainTipsRequest,
    GetChainTxStatsRequest,
    GetMempoolAncestorsRequest,
    GetMempoolDescendantsRequest,
    GetMempoolEntryRequest,
    GetMempoolInfoRequest,
    GetSpentInfoRequest,
    GetTxOutProofRequest,
    PreciousBlockRequest,
    PruneBlockchainRequest,
    SaveMemPoolRequest,
    VerifyTxOutProofRequest,
    TxOutSetInfo
)
from evrmore_rpc.models.assets import (
    AssetInfoResponse,
    GetAssetDataRequest,
    IssueAssetRequest,
    TransferAssetRequest,
    ListAddressesForAssetRequest,
    ListAssetsRequest,
    ReissueAssetRequest,
    SnapshotResult
)
from evrmore_rpc.models.network import NetworkInfoResponse, PeerInfo
from evrmore_rpc.models.wallet import (
    WalletInfoResponse,
    TransactionInfoResponse,
    GetTransactionRequest,
    GetNewAddressRequest,
    GetBalanceRequest,
    ListAccountsResponse,
    ListAddressGroupingsResponse,
    ListReceivedByAddressRequest,
    ListReceivedByAddressResponse,
    ListSinceBlockRequest,
    ListSinceBlockResult,
    ListTransactionsRequest,
    ListTransactionsResponse,
    ListUnspentRequest,
    ListUnspentResponse,
    SendToAddressRequest,
    SetTxFeeRequest,
    AbandonTransactionRequest,
    AddMultisigAddressRequest,
    BackupWalletRequest,
    ImportAddressRequest,
    ImportPrunedFundsRequest,
    SignMessageRequest
)
from evrmore_rpc.models.mining import MiningInfoResponse
from evrmore_rpc.models.control import MemoryInfoResponse, RPCInfoResponse
from evrmore_rpc.models.rawtx import (
    CreateRawTransactionRequest,
    DecodeRawTransactionRequest,
    SignRawTransactionRequest,
    SignRawTransactionResponse,
    SendRawTransactionRequest
)
from evrmore_rpc.models.address import AddressParam
from evrmore_rpc.models.validate import ValidateAddressResult
from evrmore_rpc.models.addressindex import (
    AddressBalance,
    AddressDelta,
    AddressMempoolEntry,
    AddressUtxo,
    GetAddressBalanceRequest,
    GetAddressDeltasRequest,
    GetAddressMempoolRequest,
    GetAddressTxidsRequest,
    GetAddressUtxosRequest
)
from evrmore_rpc.models.messages import (
    MessageChannel,
    Message,
    SendMessageRequest,
    SubscribeToChannelRequest,
    UnsubscribeFromChannelRequest
)
from evrmore_rpc.models.restricted import (
    TaggedAddress,
    AddressRestriction,
    GlobalRestriction,
    IssueQualifierAssetRequest,
    RestrictedAssetRequest,
    ReissueRestrictedAssetRequest,
    AddTagToAddressRequest,
    RemoveTagFromAddressRequest,
    FreezeAddressRequest,
    UnfreezeAddressRequest,
    FreezeRestrictedAssetRequest,
    UnfreezeRestrictedAssetRequest,
    TransferQualifierRequest
)
from evrmore_rpc.models.rewards import (
    SnapshotRequest,
    DistributionStatus,
    CancelSnapshotRequest,
    DistributeRewardRequest,
    GetDistributeStatusRequest,
    GetSnapshotRequest,
    ListSnapshotRequestsRequest,
    RequestSnapshotRequest
)
from evrmore_rpc.models.generating import GenerateRequest

class evrmore_rpc:
    """Evrmore RPC client"""
    
    def __init__(self, config_path: Optional[Path] = None, max_retries: int = 3, retry_interval: float = 1.0):
        """Initialize RPC client
        
        Args:
            config_path: Optional path to evrmore.conf. If not provided,
                        will look in default location (~/.evrmore/evrmore.conf)
                        or use EVRMORE_ROOT environment variable.
            max_retries: Maximum number of connection retry attempts
            retry_interval: Time to wait between retries in seconds
        
        Raises:
            EvrmoreConfigError: If configuration is invalid or cannot be loaded
            NodeConnectionError: If cannot connect to the node after retries
        """
        self.max_retries = max_retries
        self.retry_interval = retry_interval
        
        # Load and validate configuration
        try:
            self.config = load_config(config_path)
        except EvrmoreConfigError as e:
            # Try environment variables if config file fails
            self.config = self._load_env_config()
            
        # Build RPC URL using config settings
        self.url = self._build_rpc_url()
        
        # Initialize session with auth
        self.session = requests.Session()
        self.session.auth = (self.config.rpcuser, self.config.rpcpassword)
        self.session.headers['content-type'] = 'application/json'
        
        # Request ID counter
        self._request_id = 0
        
        # Verify connection
        self._verify_connection()
    
    def _load_env_config(self) -> EvrmoreConfig:
        """Load configuration from environment variables"""
        config_dict = {
            'rpcuser': os.getenv('EVRMORE_RPC_USER'),
            'rpcpassword': os.getenv('EVRMORE_RPC_PASSWORD'),
            'rpcport': int(os.getenv('EVRMORE_RPC_PORT', '8819')),
            'rpcbind': os.getenv('EVRMORE_RPC_BIND', '127.0.0.1'),
            'server': True
        }
        
        # Add optional ZMQ settings if present
        if zmq_hash_tx := os.getenv('EVRMORE_ZMQ_HASHTX'):
            config_dict['zmqpubhashtx'] = zmq_hash_tx
        if zmq_hash_block := os.getenv('EVRMORE_ZMQ_HASHBLOCK'):
            config_dict['zmqpubhashblock'] = zmq_hash_block
            
        try:
            return EvrmoreConfig(**config_dict)
        except ValidationError as e:
            raise EvrmoreConfigError(
                "Invalid environment configuration:\n" + 
                "\n".join(f"- {err['msg']}" for err in e.errors())
            )

    def _build_rpc_url(self) -> str:
        """Build RPC URL from config settings"""
        # Check if custom URL is set in environment
        if custom_url := os.getenv('EVRMORE_RPC_URL'):
            return custom_url
            
        # Build URL from config components
        protocol = 'https' if os.getenv('EVRMORE_RPC_SSL') else 'http'
        host = self.config.rpcbind
        port = self.config.rpcport
        
        # Handle IPv6 addresses
        if ':' in host and not host.startswith('['):
            host = f'[{host}]'
            
        # Handle 0.0.0.0 binding
        if host == '0.0.0.0':
            host = '127.0.0.1'  # Connect to localhost when bound to all interfaces
            
        return f"{protocol}://{host}:{port}"
    
    def _verify_connection(self) -> None:
        """Verify connection to the Evrmore node"""
        for attempt in range(self.max_retries):
            try:
                # Try to get blockchain info
                self._call_method("getblockchaininfo")
                return
                
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise NodeConnectionError(
                        f"Failed to connect to Evrmore node at {self.url} after {self.max_retries} attempts: {str(e)}\n"
                        "Please ensure the Evrmore daemon is running and accepting connections."
                    )
                time.sleep(self.retry_interval)
    
    def _get_request_id(self) -> int:
        """Get unique request ID"""
        self._request_id += 1
        return self._request_id
    
    def _call_method(self, method: str, *args) -> Any:
        """Make an RPC call to the Evrmore node
        
        Args:
            method: RPC method name
            *args: Method arguments
            
        Returns:
            Method result
            
        Raises:
            NodeConnectionError: If cannot connect to the node
            NodeAuthError: If authentication fails
            EvrmoreError: If the node returns an error
        """
        # Create request payload
        request = {
            'jsonrpc': '2.0',
            'method': method,
            'params': list(args),
            'id': self._get_request_id()
        }

        for attempt in range(self.max_retries):
            try:
                # Make HTTP request
                response = self.session.post(
                    self.url,
                    json=request,
                    timeout=10
                )
                
                # Check for auth error
                if response.status_code == 401:
                    raise NodeAuthError(
                        "Authentication failed. Please check rpcuser and rpcpassword in evrmore.conf"
                    )
                
                # Handle 500 errors with more detail
                if response.status_code == 500:
                    try:
                        error_data = response.json()
                        if 'error' in error_data:
                            error = error_data['error']
                            raise EvrmoreError(
                                code=error.get('code', -1),
                                message=error.get('message', 'Unknown error'),
                                method=method
                            )
                    except ValueError:
                        # If we can't parse the JSON, include the raw response text
                        error_text = response.text[:200] + '...' if len(response.text) > 200 else response.text
                        raise NodeConnectionError(
                            f"Server error (500) from node at {self.url}\n"
                            f"Method: {method}\n"
                            f"Arguments: {args}\n"
                            f"Response: {error_text}"
                        )
                
                # Check for other HTTP errors
                response.raise_for_status()
                
                # Parse response
                try:
                    result = response.json()
                except ValueError:
                    raise NodeConnectionError(
                        f"Invalid JSON response from node for method '{method}'\n"
                        f"Raw response: {response.text[:200]}..."
                    )

                # Check for RPC error
                if error := result.get('error'):
                    raise EvrmoreError(
                        code=error.get('code', -1),
                        message=error.get('message', 'Unknown error'),
                        method=method
                    )

                return result.get('result')
                
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise NodeConnectionError(
                        f"Failed to connect to Evrmore node at {self.url}\n"
                        f"Method: {method}\n"
                        f"Arguments: {args}\n"
                        f"Error: {str(e)}"
                    )
                time.sleep(self.retry_interval)
            
            except NodeAuthError:
                raise  # Don't retry auth errors
            
            except (NodeConnectionError, EvrmoreError) as e:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(self.retry_interval)
    
    # Blockchain Methods
    clearmempool = RPCMethod('clearmempool', ClearMemPoolRequest, None)
    decodeblock = RPCMethod('decodeblock', DecodeBlockRequest, DecodedBlock)
    getbestblockhash = RPCMethod('getbestblockhash', response_model=str)
    getblock = RPCMethod('getblock', GetBlockRequest, BlockInfoResponse)
    getblockchaininfo = RPCMethod('getblockchaininfo', response_model=BlockchainInfoResponse)
    getblockcount = RPCMethod('getblockcount', response_model=int)
    getblockhash = RPCMethod('getblockhash', GetBlockHashRequest, response_model=str)
    getblockhashes = RPCMethod('getblockhashes', GetBlockHashesRequest, response_model=List[str])
    getblockheader = RPCMethod('getblockheader', GetBlockHeaderRequest, BlockHeaderResponse)
    getchaintips = RPCMethod('getchaintips', GetChainTipsRequest, response_model=List[ChainTip])
    getchaintxstats = RPCMethod('getchaintxstats', GetChainTxStatsRequest, ChainTxStats)
    getdifficulty = RPCMethod('getdifficulty', response_model=Decimal)
    getmempoolancestors = RPCMethod('getmempoolancestors', GetMempoolAncestorsRequest, MempoolAncestorsResponse)
    getmempooldescendants = RPCMethod('getmempooldescendants', GetMempoolDescendantsRequest, MempoolDescendantsResponse)
    getmempoolentry = RPCMethod('getmempoolentry', GetMempoolEntryRequest, MempoolEntry)
    getmempoolinfo = RPCMethod('getmempoolinfo', GetMempoolInfoRequest, MempoolInfoResponse)
    getrawmempool = RPCMethod('getrawmempool', GetRawMempoolRequest, response_model=Union[List[str], Dict[str, MempoolEntry]])
    getspentinfo = RPCMethod('getspentinfo', GetSpentInfoRequest, SpentInfo)
    gettxout = RPCMethod('gettxout', GetTxOutRequest, TransactionOutput)
    gettxoutproof = RPCMethod('gettxoutproof', GetTxOutProofRequest, TxOutProofResponse)
    gettxoutsetinfo = RPCMethod('gettxoutsetinfo', GetTxOutSetInfoRequest, TxOutSetInfo)
    preciousblock = RPCMethod('preciousblock', PreciousBlockRequest, None)
    pruneblockchain = RPCMethod('pruneblockchain', PruneBlockchainRequest, int)
    savemempool = RPCMethod('savemempool', SaveMemPoolRequest, None)
    verifychain = RPCMethod('verifychain', VerifyChainRequest, bool)
    verifytxoutproof = RPCMethod('verifytxoutproof', VerifyTxOutProofRequest, VerifyTxOutProofResponse)
    
    # Network Methods
    getnetworkinfo = RPCMethod('getnetworkinfo', response_model=NetworkInfoResponse)
    getpeerinfo = RPCMethod('getpeerinfo', response_model=List[PeerInfo])
    getconnectioncount = RPCMethod('getconnectioncount', response_model=int)
    ping = RPCMethod('ping', response_model=None)
    
    # Asset Methods
    getassetdata = RPCMethod('getassetdata', GetAssetDataRequest, AssetInfoResponse)
    getcacheinfo = RPCMethod('getcacheinfo', response_model=Dict[str, Any])
    getsnapshot = RPCMethod('getsnapshot', response_model=SnapshotResult)
    issue = RPCMethod('issue', IssueAssetRequest, response_model=str)
    issueunique = RPCMethod('issueunique', response_model=str)
    listaddressesbyasset = RPCMethod('listaddressesbyasset', ListAddressesForAssetRequest, response_model=Dict[str, Decimal])
    listassetbalancesbyaddress = RPCMethod('listassetbalancesbyaddress', response_model=Dict[str, Decimal])
    listassets = RPCMethod('listassets', ListAssetsRequest, response_model=Dict[str, AssetInfoResponse])
    listmyassets = RPCMethod('listmyassets', ListAssetsRequest, response_model=Dict[str, Decimal])
    reissue = RPCMethod('reissue', ReissueAssetRequest, response_model=str)
    transfer = RPCMethod('transfer', TransferAssetRequest, response_model=str)
    transferfromaddress = RPCMethod('transferfromaddress', response_model=str)
    transferfromaddresses = RPCMethod('transferfromaddresses', response_model=str)
    
    # Wallet Methods
    abandontransaction = RPCMethod('abandontransaction', AbandonTransactionRequest)
    addmultisigaddress = RPCMethod('addmultisigaddress', AddMultisigAddressRequest, response_model=str)
    addwitnessaddress = RPCMethod('addwitnessaddress', AddressParam, response_model=str)
    backupwallet = RPCMethod('backupwallet', BackupWalletRequest)
    dumpprivkey = RPCMethod('dumpprivkey', AddressParam, response_model=str)
    dumpwallet = RPCMethod('dumpwallet', response_model=None)
    encryptwallet = RPCMethod('encryptwallet', response_model=None)
    getbalance = RPCMethod('getbalance', GetBalanceRequest, response_model=Decimal)
    getnewaddress = RPCMethod('getnewaddress', GetNewAddressRequest, response_model=str)
    getrawchangeaddress = RPCMethod('getrawchangeaddress', response_model=str)
    gettransaction = RPCMethod('gettransaction', GetTransactionRequest, TransactionInfoResponse)
    getunconfirmedbalance = RPCMethod('getunconfirmedbalance', response_model=Decimal)
    getwalletinfo = RPCMethod('getwalletinfo', response_model=WalletInfoResponse)
    importaddress = RPCMethod('importaddress', ImportAddressRequest)
    importprivkey = RPCMethod('importprivkey', response_model=None)
    importprunedfunds = RPCMethod('importprunedfunds', ImportPrunedFundsRequest)
    importpubkey = RPCMethod('importpubkey', response_model=None)
    importwallet = RPCMethod('importwallet', response_model=None)
    keypoolrefill = RPCMethod('keypoolrefill', response_model=None)
    listaccounts = RPCMethod('listaccounts', response_model=ListAccountsResponse)
    listaddressgroupings = RPCMethod('listaddressgroupings', response_model=ListAddressGroupingsResponse)
    listlockunspent = RPCMethod('listlockunspent', response_model=List[Dict[str, Any]])
    listreceivedbyaddress = RPCMethod('listreceivedbyaddress', ListReceivedByAddressRequest, ListReceivedByAddressResponse)
    listsinceblock = RPCMethod('listsinceblock', ListSinceBlockRequest, ListSinceBlockResult)
    listtransactions = RPCMethod('listtransactions', ListTransactionsRequest, ListTransactionsResponse)
    listunspent = RPCMethod('listunspent', ListUnspentRequest, ListUnspentResponse)
    lockunspent = RPCMethod('lockunspent', response_model=bool)
    sendmany = RPCMethod('sendmany', response_model=str)
    sendtoaddress = RPCMethod('sendtoaddress', SendToAddressRequest, response_model=str)
    settxfee = RPCMethod('settxfee', SetTxFeeRequest, response_model=bool)
    signmessage = RPCMethod('signmessage', SignMessageRequest, response_model=str)
    walletlock = RPCMethod('walletlock', response_model=None)
    walletpassphrase = RPCMethod('walletpassphrase', response_model=None)
    walletpassphrasechange = RPCMethod('walletpassphrasechange', response_model=None)
    
    # Raw Transaction Methods
    createrawtransaction = RPCMethod('createrawtransaction', CreateRawTransactionRequest)
    decoderawtransaction = RPCMethod('decoderawtransaction', DecodeRawTransactionRequest)
    decodescript = RPCMethod('decodescript')
    fundrawtransaction = RPCMethod('fundrawtransaction')
    getrawtransaction = RPCMethod('getrawtransaction', response_model=TransactionInfoResponse)
    sendrawtransaction = RPCMethod('sendrawtransaction', SendRawTransactionRequest)
    signrawtransaction = RPCMethod('signrawtransaction', SignRawTransactionRequest, SignRawTransactionResponse)
    
    # Mining Methods
    getmininginfo = RPCMethod('getmininginfo', response_model=MiningInfoResponse)
    getnetworkhashps = RPCMethod('getnetworkhashps')
    prioritisetransaction = RPCMethod('prioritisetransaction')
    submitblock = RPCMethod('submitblock')
    generate = RPCMethod('generate', GenerateRequest, response_model=List[str])
    
    # Control Methods
    getmemoryinfo = RPCMethod('getmemoryinfo', response_model=MemoryInfoResponse)
    getrpcinfo = RPCMethod('getrpcinfo', response_model=RPCInfoResponse)
    help = RPCMethod('help')
    stop = RPCMethod('stop')
    uptime = RPCMethod('uptime')
    
    # Utility Methods
    createmultisig = RPCMethod('createmultisig')
    estimatefee = RPCMethod('estimatefee')
    validateaddress = RPCMethod('validateaddress')
    verifymessage = RPCMethod('verifymessage')
    
    # Addressindex Methods
    getaddressbalance = RPCMethod('getaddressbalance', GetAddressBalanceRequest, AddressBalance)
    getaddressdeltas = RPCMethod('getaddressdeltas', GetAddressDeltasRequest, List[AddressDelta])
    getaddressmempool = RPCMethod('getaddressmempool', GetAddressMempoolRequest, List[AddressMempoolEntry])
    getaddresstxids = RPCMethod('getaddresstxids', GetAddressTxidsRequest, List[str])
    getaddressutxos = RPCMethod('getaddressutxos', GetAddressUtxosRequest, List[AddressUtxo])
    
    # Message Methods
    clearmessages = RPCMethod('clearmessages', response_model=None)
    sendmessage = RPCMethod('sendmessage', SendMessageRequest, response_model=str)
    subscribetochannel = RPCMethod('subscribetochannel', SubscribeToChannelRequest, response_model=None)
    unsubscribefromchannel = RPCMethod('unsubscribefromchannel', UnsubscribeFromChannelRequest, response_model=None)
    viewallmessagechannels = RPCMethod('viewallmessagechannels', response_model=List[MessageChannel])
    viewallmessages = RPCMethod('viewallmessages', response_model=List[Message])
    
    # Restricted Asset Methods
    addtagtoaddress = RPCMethod('addtagtoaddress', AddTagToAddressRequest, response_model=str)
    checkaddressrestriction = RPCMethod('checkaddressrestriction', response_model=bool)
    checkaddresstag = RPCMethod('checkaddresstag', response_model=bool)
    checkglobalrestriction = RPCMethod('checkglobalrestriction', response_model=bool)
    freezeaddress = RPCMethod('freezeaddress', FreezeAddressRequest, response_model=str)
    freezerestrictedasset = RPCMethod('freezerestrictedasset', FreezeRestrictedAssetRequest, response_model=str)
    getverifierstring = RPCMethod('getverifierstring', response_model=str)
    issuequalifierasset = RPCMethod('issuequalifierasset', IssueQualifierAssetRequest, response_model=str)
    issuerestrictedasset = RPCMethod('issuerestrictedasset', RestrictedAssetRequest, response_model=str)
    isvalidverifierstring = RPCMethod('isvalidverifierstring', response_model=bool)
    listaddressesfortag = RPCMethod('listaddressesfortag', response_model=List[TaggedAddress])
    listaddressrestrictions = RPCMethod('listaddressrestrictions', response_model=List[AddressRestriction])
    listglobalrestrictions = RPCMethod('listglobalrestrictions', response_model=List[GlobalRestriction])
    listtagsforaddress = RPCMethod('listtagsforaddress', response_model=List[str])
    reissuerestrictedasset = RPCMethod('reissuerestrictedasset', ReissueRestrictedAssetRequest, response_model=str)
    removetagfromaddress = RPCMethod('removetagfromaddress', RemoveTagFromAddressRequest, response_model=str)
    transferqualifier = RPCMethod('transferqualifier', TransferQualifierRequest, response_model=str)
    unfreezeaddress = RPCMethod('unfreezeaddress', UnfreezeAddressRequest, response_model=str)
    unfreezerestrictedasset = RPCMethod('unfreezerestrictedasset', UnfreezeRestrictedAssetRequest, response_model=str)
    viewmyrestrictedaddresses = RPCMethod('viewmyrestrictedaddresses', response_model=List[str])
    viewmytaggedaddresses = RPCMethod('viewmytaggedaddresses', response_model=List[str])
    
    # Rewards Methods
    cancelsnapshotrequest = RPCMethod('cancelsnapshotrequest', CancelSnapshotRequest, response_model=bool)
    distributereward = RPCMethod('distributereward', DistributeRewardRequest, response_model=str)
    getdistributestatus = RPCMethod('getdistributestatus', GetDistributeStatusRequest, response_model=DistributionStatus)
    getsnapshotrequest = RPCMethod('getsnapshotrequest', GetSnapshotRequest, response_model=SnapshotRequest)
    listsnapshotrequests = RPCMethod('listsnapshotrequests', ListSnapshotRequestsRequest, response_model=List[SnapshotRequest])
    requestsnapshot = RPCMethod('requestsnapshot', RequestSnapshotRequest, response_model=bool)

__all__ = ['evrmore_rpc'] 