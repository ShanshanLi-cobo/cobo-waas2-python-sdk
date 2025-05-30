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


class TokenListingRequestStatus(str, Enum):
    """
    The status of the token listing request. - `Submitted`: The request has been submitted and is pending processing. - `Succeeded`: The token has been successfully listed. - `Failed`: The token listing request was rejected or failed to process. 
    """

    """
    allowed enum values
    """
    SUBMITTED = 'Submitted'
    SUCCEEDED = 'Succeeded'
    FAILED = 'Failed'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TokenListingRequestStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


