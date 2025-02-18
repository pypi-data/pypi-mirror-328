"""Wallet related models for RPC requests/responses"""
from typing import Optional, List, Dict, Any, Literal as TypeLiteral
from pydantic import BaseModel, Field, validator
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
    walletname: str
    walletversion: int
    balance: Decimal
    unconfirmed_balance: Decimal
    immature_balance: Decimal
    txcount: int
    keypoololdest: int
    keypoolsize: int
    keypoolsize_hd_internal: int
    paytxfee: Decimal
    hdseedid: str
    hdmasterkeyid: str

class TransactionInfoResponse(BaseModel):
    """Model for wallet transaction information"""
    amount: Decimal
    fee: Optional[Decimal] = None
    confirmations: int = 0
    blockhash: Optional[str] = None
    blockindex: Optional[int] = None
    blocktime: Optional[int] = None
    txid: str
    walletconflicts: Optional[List[str]] = None
    time: int
    timereceived: int
    bip125_replaceable: Optional[str] = None
    details: Optional[List[TransactionDetail]] = None
    hex: str
    comment: Optional[str] = None
    to: Optional[str] = None
    trusted: Optional[bool] = None
    
    class Config:
        """Pydantic model configuration"""
        extra = "allow"  # Allow extra fields that might be present in response

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
    'SignMessageRequest'
] 