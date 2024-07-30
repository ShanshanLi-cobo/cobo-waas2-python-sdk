# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    The version of the OpenAPI document: 1.0.0
    Contact: support@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.webhook_event_type import WebhookEventType
from typing import Optional, Set
from typing_extensions import Self


class UpdateWebhookEndpointByIdRequest(BaseModel):
    """
    UpdateWebhookEndpointByIdRequest
    """  # noqa: E501
    subscribed_events: Optional[List[WebhookEventType]] = Field(default=None, description="The new event types you want to subscribe to for this webhook endpoint. You can call [Get webhook event types](/v2/api-references/developers--webhooks/get-webhook-event-types) to retrieve all available event types.")
    status: Optional[StrictStr] = Field(default=None, description="The new status you want to set the webhook endpoint to. If you set `status` to `STATUS_INACTIVE`, the endpoint will be revoked, meaning it will no longer receive any webhook events.")
    description: Optional[StrictStr] = Field(default=None, description="The webhook endpoint description.")
    __properties: ClassVar[List[str]] = ["subscribed_events", "status", "description"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STATUS_INACTIVE']):
            raise ValueError("must be one of enum values ('STATUS_INACTIVE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UpdateWebhookEndpointByIdRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateWebhookEndpointByIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscribed_events": obj.get("subscribed_events"),
            "status": obj.get("status"),
            "description": obj.get("description")
        })
        return _obj

