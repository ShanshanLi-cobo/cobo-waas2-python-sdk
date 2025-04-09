# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionDestinationType(str, Enum):
    """
    The transaction destination type. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type. 
    """

    """
    allowed enum values
    """
    ADDRESS = 'Address'
    EXCHANGEWALLET = 'ExchangeWallet'
    EVM_CONTRACT = 'EVM_Contract'
    SOL_CONTRACT = 'SOL_Contract'
    COSMOS_CONTRACT = 'COSMOS_Contract'
    EVM_EIP_191_SIGNATURE = 'EVM_EIP_191_Signature'
    EVM_EIP_712_SIGNATURE = 'EVM_EIP_712_Signature'
    BTC_BIP_137_SIGNATURE = 'BTC_BIP_137_Signature'
    BTC_BIP_322_SIGNATURE = 'BTC_BIP_322_Signature'
    COSMOS_ADR_36_SIGNATURE = 'COSMOS_ADR_36_Signature'
    RAW_MESSAGE_SIGNATURE = 'Raw_Message_Signature'
    DEPOSITTOADDRESS = 'DepositToAddress'
    DEPOSITTOWALLET = 'DepositToWallet'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionDestinationType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


