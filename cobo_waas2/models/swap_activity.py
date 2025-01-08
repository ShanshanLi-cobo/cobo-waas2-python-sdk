# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.transaction_initiator_type import TransactionInitiatorType
from typing import Optional, Set
from typing_extensions import Self


class SwapActivity(BaseModel):
    """
    SwapActivity
    """  # noqa: E501
    activity_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the swap activity.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the swap activity.")
    wallet_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the wallet.")
    pay_token_id: Optional[StrictStr] = Field(default=None, description="The token symbol to swap from.")
    receive_token_id: Optional[StrictStr] = Field(default=None, description="The token symbol to swap to.")
    pay_amount: Optional[StrictStr] = Field(default=None, description="The amount of tokens to bridge.")
    receive_amount: Optional[StrictStr] = Field(default=None, description="The amount of tokens to receive.")
    fee_amount: Optional[StrictStr] = Field(default=None, description="The amount of fee.")
    initiator: Optional[StrictStr] = Field(default=None, description="The initiator of the swap activity.")
    initiator_type: Optional[TransactionInitiatorType] = None
    created_timestamp: Optional[StrictInt] = Field(default=None, description="The time when the swap activity was created, in Unix timestamp format, measured in milliseconds.")
    updated_timestamp: Optional[StrictInt] = Field(default=None, description="The time when the swap activity was last updated, in Unix timestamp format, measured in milliseconds.")
    __properties: ClassVar[List[str]] = ["activity_id", "status", "wallet_id", "pay_token_id", "receive_token_id", "pay_amount", "receive_amount", "fee_amount", "initiator", "initiator_type", "created_timestamp", "updated_timestamp"]

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
        """Create an instance of SwapActivity from a JSON string"""
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
        # set to None if initiator (nullable) is None
        # and model_fields_set contains the field
        if self.initiator is None and "initiator" in self.model_fields_set:
            _dict['initiator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwapActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activity_id": obj.get("activity_id"),
            "status": obj.get("status"),
            "wallet_id": obj.get("wallet_id"),
            "pay_token_id": obj.get("pay_token_id"),
            "receive_token_id": obj.get("receive_token_id"),
            "pay_amount": obj.get("pay_amount"),
            "receive_amount": obj.get("receive_amount"),
            "fee_amount": obj.get("fee_amount"),
            "initiator": obj.get("initiator"),
            "initiator_type": obj.get("initiator_type"),
            "created_timestamp": obj.get("created_timestamp"),
            "updated_timestamp": obj.get("updated_timestamp")
        })
        return _obj


