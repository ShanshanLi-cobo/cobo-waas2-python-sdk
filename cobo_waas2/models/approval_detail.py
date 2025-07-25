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
from cobo_waas2.models.role_detail import RoleDetail
from typing import Optional, Set
from typing_extensions import Self


class ApprovalDetail(BaseModel):
    """
    The approval detail data for transaction.
    """  # noqa: E501
    transaction_id: Optional[StrictStr] = Field(default=None, description="The transaction ID.")
    cobo_id: Optional[StrictStr] = Field(default=None, description="The Cobo ID, which can be used to track a transaction.")
    request_id: Optional[StrictStr] = Field(default=None, description="The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization.")
    broker_user: Optional[RoleDetail] = None
    spender: Optional[RoleDetail] = None
    approver: Optional[RoleDetail] = None
    __properties: ClassVar[List[str]] = ["transaction_id", "cobo_id", "request_id", "broker_user", "spender", "approver"]

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
        """Create an instance of ApprovalDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of broker_user
        if self.broker_user:
            _dict['broker_user'] = self.broker_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spender
        if self.spender:
            _dict['spender'] = self.spender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of approver
        if self.approver:
            _dict['approver'] = self.approver.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApprovalDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transaction_id": obj.get("transaction_id"),
            "cobo_id": obj.get("cobo_id"),
            "request_id": obj.get("request_id"),
            "broker_user": RoleDetail.from_dict(obj["broker_user"]) if obj.get("broker_user") is not None else None,
            "spender": RoleDetail.from_dict(obj["spender"]) if obj.get("spender") is not None else None,
            "approver": RoleDetail.from_dict(obj["approver"]) if obj.get("approver") is not None else None
        })
        return _obj


