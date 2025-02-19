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


class MessageSignDestinationType(str, Enum):
    """
    The type of the signature format. Refer to [Transaction sources and destinations](https://www.cobo.com/developers/v2/guides/transactions/sources-and-destinations) for a detailed introduction about the supported sources and destinations for each transaction type.  Each signature format type requires a different set of properties. Switch between the above tabs for details. 
    """

    """
    allowed enum values
    """
    EVM_EIP_191_SIGNATURE = 'EVM_EIP_191_Signature'
    EVM_EIP_712_SIGNATURE = 'EVM_EIP_712_Signature'
    BTC_EIP_191_SIGNATURE = 'BTC_EIP_191_Signature'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageSignDestinationType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


