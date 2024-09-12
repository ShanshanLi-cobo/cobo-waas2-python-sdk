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


class WebhookEndpointStatus(str, Enum):
    """
    The webhook endpoint status. Possible values include: - `STATUS_ACTIVE`: The endpoint is currently in use. - `STATUS_INACTIVE`: The endpoint has been revoked and can no longer receive webhook events. - `STATUS_PENDING_ACTIVE`: The request to create the endpoint is awaiting approval. After the approval, the endpoint will be available for use. - `STATUS_PENDING_INACTIVE`: The request to revoke the endpoint is awaiting approval. After the approval,the endpoint will no longer receive webhook events. - `STATUS_PENDING_UPDATE`: The request to update the endpoint is awaiting approval. After the approval, the endpoint will be updated. - `STATUS_REJECT_ACTIVE`: The request to create the endpoint has been rejected. 
    """

    """
    allowed enum values
    """
    STATUS_ACTIVE = 'STATUS_ACTIVE'
    STATUS_INACTIVE = 'STATUS_INACTIVE'
    STATUS_PENDING_ACTIVE = 'STATUS_PENDING_ACTIVE'
    STATUS_PENDING_INACTIVE = 'STATUS_PENDING_INACTIVE'
    STATUS_PENDING_UPDATE = 'STATUS_PENDING_UPDATE'
    STATUS_REJECT_ACTIVE = 'STATUS_REJECT_ACTIVE'

    UNKNOWN = None

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WebhookEndpointStatus from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


