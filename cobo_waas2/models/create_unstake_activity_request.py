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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.create_unstake_activity_extra import CreateUnstakeActivityExtra
from cobo_waas2.models.transaction_request_fee import TransactionRequestFee
from typing import Optional, Set
from typing_extensions import Self


class CreateUnstakeActivityRequest(BaseModel):
    """
    CreateUnstakeActivityRequest
    """  # noqa: E501
    request_id: Optional[StrictStr] = Field(default=None, description="The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization.")
    staking_id: StrictStr = Field(description="The ID of the corresponding staking position.")
    amount: Optional[StrictStr] = Field(default=None, description="The amount to unstake. For the Babylon protocol, this property is ignored.")
    fee: Optional[TransactionRequestFee] = None
    extra: Optional[CreateUnstakeActivityExtra] = None
    app_initiator: Optional[StrictStr] = Field(default=None, description="The initiator of the staking activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator.")
    __properties: ClassVar[List[str]] = ["request_id", "staking_id", "amount", "fee", "extra", "app_initiator"]

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
        """Create an instance of CreateUnstakeActivityRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of extra
        if self.extra:
            _dict['extra'] = self.extra.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateUnstakeActivityRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_id": obj.get("request_id"),
            "staking_id": obj.get("staking_id"),
            "amount": obj.get("amount"),
            "fee": TransactionRequestFee.from_dict(obj["fee"]) if obj.get("fee") is not None else None,
            "extra": CreateUnstakeActivityExtra.from_dict(obj["extra"]) if obj.get("extra") is not None else None,
            "app_initiator": obj.get("app_initiator")
        })
        return _obj


