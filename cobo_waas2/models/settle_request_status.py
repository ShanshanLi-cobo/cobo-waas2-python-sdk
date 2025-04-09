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


class SettleRequestStatus(str, Enum):
    """
    The current status of the settlement request: - `Pending`: The settlement request has been created and is awaiting processing. - `Processing`: The settlement request is currently being processed, with at least one settlement in progress. - `Completed`: All requested settlements have been completed. - `PartiallyCompleted`: Some requested settlements have been completed successfully, while others have failed. - `Failed`: All requested settlements have failed. 
    """

    """
    allowed enum values
    """
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    PARTIALLYCOMPLETED = 'PartiallyCompleted'
    FAILED = 'Failed'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SettleRequestStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


