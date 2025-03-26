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


class TransactionSourceType(str, Enum):
    """
    The transaction source. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type. 
    """

    """
    allowed enum values
    """
    ASSET = 'Asset'
    WEB3 = 'Web3'
    ORG_CONTROLLED = 'Org-Controlled'
    USER_CONTROLLED = 'User-Controlled'
    SAFE_WALLET = 'Safe{Wallet}'
    MAIN = 'Main'
    SUB = 'Sub'
    DEPOSITFROMADDRESS = 'DepositFromAddress'
    DEPOSITFROMWALLET = 'DepositFromWallet'
    DEPOSITFROMLOOP = 'DepositFromLoop'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionSourceType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


