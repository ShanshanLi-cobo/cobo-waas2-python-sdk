# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WebhookEventType(str, Enum):
    """
    The event type. To learn the trigger condition of each event type, refer to [Webhook event types and event data](/v2/guides/webhooks-callbacks/webhook-event-type).
    """

    """
    allowed enum values
    """
    WALLETS_DOT_TRANSACTION_DOT_CREATED = 'wallets.transaction.created'
    WALLETS_DOT_TRANSACTION_DOT_UPDATED = 'wallets.transaction.updated'
    WALLETS_DOT_TRANSACTION_DOT_FAILED = 'wallets.transaction.failed'
    WALLETS_DOT_TRANSACTION_DOT_SUCCEEDED = 'wallets.transaction.succeeded'
    WALLETS_DOT_MPC_DOT_TSS_REQUEST_DOT_CREATED = 'wallets.mpc.tss_request.created'
    WALLETS_DOT_MPC_DOT_TSS_REQUEST_DOT_UPDATED = 'wallets.mpc.tss_request.updated'
    WALLETS_DOT_MPC_DOT_TSS_REQUEST_DOT_FAILED = 'wallets.mpc.tss_request.failed'
    WALLETS_DOT_MPC_DOT_TSS_REQUEST_DOT_SUCCEEDED = 'wallets.mpc.tss_request.succeeded'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookEventType from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


