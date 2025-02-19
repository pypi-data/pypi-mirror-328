"""Blockchain related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral, Union
from pydantic import BaseModel, Field, ConfigDict, field_validator
from decimal import Decimal
from ..base import BlockHashParam, TransactionHashParam, RPCRequest
from ..wallet import TransactionInfoResponse

class BlockchainInfo(BaseModel):
    """Model for blockchain info"""
    model_config = ConfigDict(extra='allow')

class BlockHeader(BaseModel):
    """Model for block header information"""
    model_config = ConfigDict(extra='allow', arbitrary_types_allowed=True)
    
    hash: Optional[str]
    confirmations: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    time: int
    mediantime: int
    nonce: int
    bits: str
    difficulty: Decimal
    chainwork: str
    previousblockhash: Optional[str] = None
    nextblockhash: Optional[str] = None

class Block(BaseModel):
    """Model for block"""
    model_config = ConfigDict(extra='allow')

class ChainTip(BaseModel):
    """Model for chain tip"""
    model_config = ConfigDict(extra='allow')

class MempoolInfo(BaseModel):
    """Model for mempool info"""
    model_config = ConfigDict(extra='allow')

class ChainTxStats(BaseModel):
    """Model for chain transaction stats"""
    model_config = ConfigDict(extra='allow')
    
    time: int
    txcount: int
    window_block_count: int
    window_tx_count: int
    window_interval: int
    txrate: float
    window_final_block_hash: Optional[str] = None
    window_final_block_height: Optional[int] = None

class BlockStats(BaseModel):
    """Model for block stats"""
    model_config = ConfigDict(extra='allow')

class BlockStatsRequest(BaseModel):
    """Request model for getblockstats RPC call"""
    model_config = ConfigDict(extra='allow')

class BlockHeaderResponse(BlockHeader):
    """Response model for getblockheader RPC call"""
    pass

class BlockInfoResponse(BaseModel):
    """Model for full block information"""
    model_config = ConfigDict(extra='allow')
    
    hash: str
    confirmations: int
    size: int
    strippedsize: int
    weight: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    tx: Union[List[str], List[Dict[str, Any]]]  # Can be list of txids or full tx objects
    time: int
    mediantime: int
    nonce: int
    bits: str
    difficulty: Decimal
    chainwork: str
    headerhash: Optional[str] = None
    mixhash: Optional[str] = None
    nonce64: Optional[int] = None
    previousblockhash: Optional[str] = None
    nextblockhash: Optional[str] = None

class BlockchainInfoResponse(BaseModel):
    """Response model for getblockchaininfo RPC call"""
    model_config = ConfigDict(extra='allow')
    
    chain: str
    blocks: int
    headers: int
    bestblockhash: str
    difficulty: float
    mediantime: int
    verificationprogress: float
    initialblockdownload: Optional[bool] = None
    chainwork: str
    size_on_disk: int
    pruned: bool
    softforks: Union[List[Any], Dict[str, Any]] = Field(default_factory=list)
    warnings: Optional[str] = None

class SpentInfoResponse(BaseModel):
    """Model for spent information"""
    txid: str
    index: int
    height: Optional[int]

class DecodedBlock(BaseModel):
    """Model for decoded block information"""
    model_config = ConfigDict(extra='allow')
    
    hash: str
    size: int
    strippedsize: int
    weight: int
    height: int
    version: int
    versionHex: str
    merkleroot: str
    tx: List[Dict[str, Any]]  # List of transaction objects
    time: int
    nonce: int
    bits: str
    difficulty: Optional[Decimal] = None
    chainwork: Optional[str] = None
    headerhash: Optional[str] = None
    mixhash: Optional[str] = None
    nonce64: Optional[int] = None
    previousblockhash: Optional[str] = None
    nextblockhash: Optional[str] = None

class TxOutProof(BaseModel):
    """Model for transaction output proof"""
    data: str

class MempoolEntry(BaseModel):
    """Model for mempool entry information"""
    model_config = ConfigDict(extra='allow')
    
    size: int = Field(..., description="virtual transaction size as defined in BIP 141")
    fee: Decimal = Field(..., description="transaction fee in EVR")
    modifiedfee: Decimal = Field(..., description="transaction fee with fee deltas used for mining priority")
    time: int = Field(..., description="local time transaction entered pool in seconds since 1 Jan 1970 GMT")
    height: int = Field(..., description="block height when transaction entered pool")
    descendantcount: int = Field(..., description="number of in-mempool descendant transactions (including this one)")
    descendantsize: int = Field(..., description="virtual transaction size of in-mempool descendants (including this one)")
    descendantfees: int = Field(..., description="modified fees of in-mempool descendants (including this one)")
    ancestorcount: int = Field(..., description="number of in-mempool ancestor transactions (including this one)")
    ancestorsize: int = Field(..., description="virtual transaction size of in-mempool ancestors (including this one)")
    ancestorfees: int = Field(..., description="modified fees of in-mempool ancestors (including this one)")
    wtxid: str = Field(..., description="hash of serialized transaction, including witness data")
    depends: List[str] = Field(default_factory=list, description="unconfirmed transactions used as inputs for this transaction")

class MempoolInfoResponse(BaseModel):
    """Model for mempool information"""
    size: int
    bytes: int
    usage: int
    maxmempool: int
    mempoolminfee: Decimal

# Request Models
class GetBlockRequest(RPCRequest):
    """Request model for getblock RPC call"""
    method: str = "getblock"
    params: List[Any] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, blockhash: str, verbosity: int = 1, **data):
        super().__init__(**data)
        self.params = [blockhash, verbosity]

class GetBlockHashRequest(RPCRequest):
    """Request model for getblockhash RPC call"""
    method: str = "getblockhash"
    params: List[int] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, height: int, **data):
        super().__init__(**data)
        self.params = [height]

class GetBlockHashesRequest(RPCRequest):
    """Request model for getblockhashes RPC call"""
    timestamp: int = Field(..., description="The timestamp to get block hashes for")
    high: Optional[int] = None
    low: Optional[int] = None

class GetBlockHeaderRequest(RPCRequest):
    """Request model for getblockheader RPC call"""
    method: str = "getblockheader"
    params: List[Any] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, blockhash: str, verbose: bool = True, **data):
        super().__init__(**data)
        self.params = [blockhash, verbose]
        self.method = "getblockheader"

    @field_validator('params')
    def validate_params(cls, v: List[Any]) -> List[Any]:
        if len(v) < 1:
            raise ValueError("blockhash is required")
        if len(v) > 2:
            raise ValueError("too many parameters")
        if not isinstance(v[0], str):
            raise ValueError("blockhash must be a string")
        if len(v) == 2 and not isinstance(v[1], bool):
            raise ValueError("verbose must be a boolean")
        return v

class GetChainTxStatsRequest(RPCRequest):
    """Request model for getchaintxstats RPC call"""
    method: str = "getchaintxstats"
    params: List[Union[int, str]] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, nblocks: Optional[int] = None, blockhash: Optional[str] = None, **data):
        super().__init__(**data)
        if nblocks is not None:
            self.params.append(nblocks)
        if blockhash is not None:
            self.params.append(blockhash)

class GetMempoolAncestorsRequest(RPCRequest):
    """Request model for getmempoolancestors RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    verbose: bool = False

class GetMempoolDescendantsRequest(RPCRequest):
    """Request model for getmempooldescendants RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    verbose: bool = False

class GetMempoolEntryRequest(RPCRequest):
    """Request model for getmempoolentry RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class GetMempoolInfoRequest(RPCRequest):
    """Request model for getmempoolinfo RPC call"""
    pass

class GetRawMempoolRequest(RPCRequest):
    """Request model for getrawmempool RPC call"""
    method: str = "getrawmempool"
    params: List[bool] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, verbose: bool = False, **data):
        super().__init__(**data)
        self.params = [verbose]

class GetSpentInfoRequest(RPCRequest):
    """Request model for getspentinfo RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    index: int = Field(..., ge=0)

class GetTxOutRequest(RPCRequest):
    """Request model for gettxout RPC call"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    n: int = Field(..., ge=0)
    include_mempool: bool = True

class GetTxOutProofRequest(RPCRequest):
    """Request model for gettxoutproof RPC call"""
    txids: List[str] = Field(..., min_length=1)
    blockhash: Optional[str] = Field(None, min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class GetTxOutSetInfoRequest(RPCRequest):
    """Request model for gettxoutsetinfo RPC call"""
    pass

class PreciousBlockRequest(RPCRequest):
    """Request model for preciousblock RPC call"""
    blockhash: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")

class PruneBlockchainRequest(RPCRequest):
    """Request model for pruneblockchain RPC call"""
    height: int = Field(..., ge=0)

class SaveMemPoolRequest(RPCRequest):
    """Request model for savemempool RPC call"""
    pass

class VerifyChainRequest(RPCRequest):
    """Request model for verifychain RPC call"""
    checklevel: Optional[int] = Field(3, ge=0, le=4)
    nblocks: Optional[int] = Field(6, ge=0)

class VerifyTxOutProofRequest(RPCRequest):
    """Request model for verifytxoutproof RPC call"""
    proof: str = Field(..., min_length=1)

class ClearMemPoolRequest(RPCRequest):
    """Request model for clearmempool RPC call"""
    pass

class DecodeBlockRequest(RPCRequest):
    """Request model for decodeblock RPC call"""
    method: str = "decodeblock"
    params: List[Any] = Field(default_factory=list)
    id: Optional[int] = None

    def __init__(self, blockhex: str, **data):
        super().__init__(**data)
        self.params = [blockhex]

class GetChainTipsRequest(RPCRequest):
    """Request model for getchaintips RPC call"""
    pass

# Response Models
class MempoolAncestorsResponse(BaseModel):
    """Response model for getmempoolancestors RPC call"""
    model_config = ConfigDict(extra='allow')

class MempoolDescendantsResponse(BaseModel):
    """Response model for getmempooldescendants RPC call"""
    model_config = ConfigDict(extra='allow')

class TxOutProofResponse(BaseModel):
    """Response model for gettxoutproof RPC call"""
    data: str

class VerifyTxOutProofResponse(BaseModel):
    """Response model for verifytxoutproof RPC call"""
    txids: List[str]

class SpentInfo(BaseModel):
    """Model for spent information"""
    txid: str = Field(..., min_length=64, max_length=64, pattern="^[0-9a-fA-F]{64}$")
    index: int = Field(..., ge=0)
    height: Optional[int] = None

class TxOutSetInfo(BaseModel):
    """Model for transaction output set information"""
    model_config = ConfigDict(extra='allow')
    
    height: int = Field(..., description="The current block height (index)")
    bestblock: str = Field(..., description="The best block hash hex")
    transactions: int = Field(..., description="The number of transactions")
    txouts: int = Field(..., description="The number of output transactions")
    bogosize: int = Field(..., description="A meaningless metric for UTXO set size")
    hash_serialized_2: str = Field(..., description="The serialized hash")
    disk_size: int = Field(..., description="The estimated size of the chainstate on disk")
    total_amount: Decimal = Field(..., description="The total amount")

__all__ = [
    # Models
    'BlockHeader',
    'BlockHeaderResponse',
    'BlockInfoResponse',
    'BlockStats',
    'ChainTip',
    'ChainTxStats',
    'SpentInfoResponse',
    'DecodedBlock',
    'TxOutProof',
    'MempoolEntry',
    'MempoolInfoResponse',
    'TxOutSetInfo',
    
    # Request Models
    'GetBlockRequest',
    'GetBlockHashRequest',
    'GetBlockHeaderRequest',
    'GetChainTxStatsRequest',
    'GetMempoolAncestorsRequest',
    'GetMempoolDescendantsRequest',
    'GetMempoolEntryRequest',
    'GetMempoolInfoRequest',
    'GetRawMempoolRequest',
    'GetSpentInfoRequest',
    'GetTxOutRequest',
    'GetTxOutProofRequest',
    'GetTxOutSetInfoRequest',
    'PreciousBlockRequest',
    'PruneBlockchainRequest',
    'SaveMemPoolRequest',
    'VerifyChainRequest',
    'VerifyTxOutProofRequest',
    'ClearMemPoolRequest',
    'DecodeBlockRequest',
    'GetBlockHashesRequest',
    'GetChainTipsRequest',
    
    # Response Models
    'MempoolAncestorsResponse',
    'MempoolDescendantsResponse',
    'TxOutProofResponse',
    'VerifyTxOutProofResponse',
    'SpentInfo',
    'BlockchainInfoResponse'
] 