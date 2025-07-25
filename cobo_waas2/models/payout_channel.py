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


class PayoutChannel(str, Enum):
    """
    The channel through which settlement funds will be transferred. Available options: - `Crypto`: Direct withdrawal to a registered crypto address. - `OffRamp`: Settle to a registered bank account. 
    """

    """
    allowed enum values
    """
    CRYPTO = 'Crypto'
    OFFRAMP = 'OffRamp'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PayoutChannel from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


