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


class SwapSingingStatus(str, Enum):
    """
    The transaction signing result. Possible values include:    - `Pending`: Waiting for signing from the signer.   - `Approved`: The signer has signed to the signing request.   - `Timeout`: The signing request has expired due to no response from the signer.   - `Rejected`: The signer has rejected the signing request. 
    """

    """
    allowed enum values
    """
    PENDING = 'Pending'
    SIGNED = 'Signed'
    TIMEOUT = 'Timeout'
    REJECTED = 'Rejected'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SwapSingingStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


