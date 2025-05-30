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
from cobo_waas2.models.tss_curve import TSSCurve
from typing import Optional, Set
from typing_extensions import Self


class TSSKeyGenRequest(BaseModel):
    """
    TSSKeyGenRequest
    """  # noqa: E501
    threshold: Optional[StrictInt] = Field(default=None, description="The number of key share holders required to approve each operation in TSS key share group.")
    node_ids: Optional[List[StrictStr]] = None
    curve: Optional[TSSCurve] = None
    task_id: Optional[StrictStr] = Field(default=None, description="The task ID.")
    biz_task_id: Optional[StrictStr] = Field(default=None, description="The business task ID. This field contains the TSS request ID.")
    __properties: ClassVar[List[str]] = ["threshold", "node_ids", "curve", "task_id", "biz_task_id"]

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
        """Create an instance of TSSKeyGenRequest from a JSON string"""
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
        """Create an instance of TSSKeyGenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "threshold": obj.get("threshold"),
            "node_ids": obj.get("node_ids"),
            "curve": obj.get("curve"),
            "task_id": obj.get("task_id"),
            "biz_task_id": obj.get("biz_task_id")
        })
        return _obj


