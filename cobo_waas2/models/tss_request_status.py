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


class TSSRequestStatus(str, Enum):
    """
    The TSS request status. Possible values include: - `PendingKeyHolderConfirmation`: The action done to the TSS request is currently pending enough key share holders to approve.  - `KeyHolderConfirmationFailed`: Key share holders failed to approve the the action to be done to the TSS request.  - `KeyGenerating`: The key share is currently being generated for the action to be done to the TSS request.  - `MPCProcessing`: The TSS request approval is waiting to be started.    - For [MPC Wallets (User-Controlled Wallets)](https://manuals.cobo.com/en/portal/mpc-wallets/ucw/introduction), you need to use the Client App and call the UCW SDK to start the TSS request approval process.   - For [MPC Wallets (Organization-Controlled Wallets)](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/introduction):     - If you are using the [API co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#create-a-main-group), this status indicates that the TSS Node will soon request the callback server to start the [risk controls](https://manuals.cobo.com/en/portal/risk-controls/introduction) check. No further action is required from you at this stage.     - If you are using the [mobile co-signer](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#create-a-main-group), key share holders need to use their [Cobo Guard](https://manuals.cobo.com/en/guard/introduction) to approve the TSS request and participate in the signing process.  - `KeyGeneratingFailed`: The key share generation process has failed for the action to be done to the TSS request.  - `Success`: The action done to the TSS request has been completed successfully. If you see this status while running [Cancel TSS request](/v2/api-references/wallets--mpc-wallets/cancel-tss-request), this mean the specified TSS request has been successfully canceled. 
    """

    """
    allowed enum values
    """
    PENDINGKEYHOLDERCONFIRMATION = 'PendingKeyHolderConfirmation'
    KEYHOLDERCONFIRMATIONFAILED = 'KeyHolderConfirmationFailed'
    KEYGENERATING = 'KeyGenerating'
    MPCPROCESSING = 'MPCProcessing'
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


