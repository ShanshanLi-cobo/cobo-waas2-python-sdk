# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TSSRequestStatus(str, Enum):
    """
    The TSS request status. Possible values include: - `PendingKeyHolderConfirmation`: The action done to the TSS request is currently pending enough key share holders to approve.  - `KeyHolderConfirmationFailed`: Key share holders failed to approve the the action to be done to the TSS request.  - `KeyGenerating`: The key share is currently being generated for the action to be done to the TSS request.  - `KeyGeneratingFailed`: The key share generation process has failed for the action to be done to the TSS request.  - `Success`: The action done to the TSS request has been completed successfully. If you see this status while running [Cancel TSS request](http://localhost:3000/v2/api-references/wallets--mpc-wallets/cancel-tss-request), this mean the specified TSS request has been successfully canceled. 
    """

    """
    allowed enum values
    """
    PENDINGKEYHOLDERCONFIRMATION = 'PendingKeyHolderConfirmation'
    KEYHOLDERCONFIRMATIONFAILED = 'KeyHolderConfirmationFailed'
    KEYGENERATING = 'KeyGenerating'
    KEYGENERATINGFAILED = 'KeyGeneratingFailed'
    SUCCESS = 'Success'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TSSRequestStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN

