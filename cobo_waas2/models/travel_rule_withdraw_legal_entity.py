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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cobo_waas2.models.selected_entity_type import SelectedEntityType
from typing import Optional, Set
from typing_extensions import Self


class TravelRuleWithdrawLegalEntity(BaseModel):
    """
    Required fields for LEGAL entities.
    """  # noqa: E501
    selected_entity_type: SelectedEntityType
    legal_name: StrictStr = Field(description="The legal name of the entity.")
    date_of_incorporation: Optional[date] = Field(default=None, description="The incorporation date of the entity.")
    place_of_incorporation: Optional[StrictStr] = Field(default=None, description="The place of incorporation of the entity.")
    __properties: ClassVar[List[str]] = ["selected_entity_type", "legal_name", "date_of_incorporation", "place_of_incorporation"]

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
        """Create an instance of TravelRuleWithdrawLegalEntity from a JSON string"""
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
        """Create an instance of TravelRuleWithdrawLegalEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "selected_entity_type": obj.get("selected_entity_type"),
            "legal_name": obj.get("legal_name"),
            "date_of_incorporation": obj.get("date_of_incorporation"),
            "place_of_incorporation": obj.get("place_of_incorporation")
        })
        return _obj


