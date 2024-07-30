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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class BabylonValidator(BaseModel):
    """
    The babylon validator information.
    """  # noqa: E501
    icon_url: StrictStr = Field(description="The URL of the validator's icon.")
    name: StrictStr = Field(description="The name of validator.")
    priority: Optional[StrictInt] = Field(default=None, description="The priority of validator.")
    public_key: StrictStr = Field(description="The public key of validator.")
    commission_rate: Union[StrictFloat, StrictInt] = Field(description="The commission rate of validator.")
    supported_pos_chains: List[StrictStr] = Field(description="The list of supported pos chains.")
    __properties: ClassVar[List[str]] = ["icon_url", "name", "priority", "public_key", "commission_rate", "supported_pos_chains"]

    @field_validator('supported_pos_chains')
    def supported_pos_chains_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['Babylon', 'Cosmos']):
                raise ValueError("each list item must be one of ('Babylon', 'Cosmos')")
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
        """Create an instance of BabylonValidator from a JSON string"""
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
        """Create an instance of BabylonValidator from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "icon_url": obj.get("icon_url"),
            "name": obj.get("name"),
            "priority": obj.get("priority"),
            "public_key": obj.get("public_key"),
            "commission_rate": obj.get("commission_rate"),
            "supported_pos_chains": obj.get("supported_pos_chains")
        })
        return _obj

