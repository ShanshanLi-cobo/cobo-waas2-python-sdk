# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from cobo_waas2.models.babylon_staking_activity_detail_extra import BabylonStakingActivityDetailExtra
from cobo_waas2.models.core_staking_activity_detail_extra import CoreStakingActivityDetailExtra
from cobo_waas2.models.eth_staking_activity_detail_extra import EthStakingActivityDetailExtra
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

ACTIVITYEXTRA_ONE_OF_SCHEMAS = ["BabylonStakingActivityDetailExtra", "CoreStakingActivityDetailExtra", "EthStakingActivityDetailExtra"]

class ActivityExtra(BaseModel):
    """
    ActivityExtra
    """
    # data type: BabylonStakingActivityDetailExtra
    oneof_schema_1_validator: Optional[BabylonStakingActivityDetailExtra] = None
    # data type: EthStakingActivityDetailExtra
    oneof_schema_2_validator: Optional[EthStakingActivityDetailExtra] = None
    # data type: CoreStakingActivityDetailExtra
    oneof_schema_3_validator: Optional[CoreStakingActivityDetailExtra] = None
    actual_instance: Optional[Union[BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra]] = None
    one_of_schemas: Set[str] = { "BabylonStakingActivityDetailExtra", "CoreStakingActivityDetailExtra", "EthStakingActivityDetailExtra" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ActivityExtra.model_construct()
        error_messages = []
        match = 0
        # validate data type: BabylonStakingActivityDetailExtra
        if not isinstance(v, BabylonStakingActivityDetailExtra):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BabylonStakingActivityDetailExtra`")
        else:
            match += 1
        # validate data type: EthStakingActivityDetailExtra
        if not isinstance(v, EthStakingActivityDetailExtra):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EthStakingActivityDetailExtra`")
        else:
            match += 1
        # validate data type: CoreStakingActivityDetailExtra
        if not isinstance(v, CoreStakingActivityDetailExtra):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CoreStakingActivityDetailExtra`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ActivityExtra with oneOf schemas: BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ActivityExtra with oneOf schemas: BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("pool_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `pool_type` in the input.")

        # check if data type is `BabylonStakingActivityDetailExtra`
        if _data_type == "Babylon":
            instance.actual_instance = BabylonStakingActivityDetailExtra.from_json(json_str)
            return instance

        # check if data type is `CoreStakingActivityDetailExtra`
        if _data_type == "CoreBTC":
            instance.actual_instance = CoreStakingActivityDetailExtra.from_json(json_str)
            return instance

        # check if data type is `EthStakingActivityDetailExtra`
        if _data_type == "ETHBeacon":
            instance.actual_instance = EthStakingActivityDetailExtra.from_json(json_str)
            return instance

        # check if data type is `BabylonStakingActivityDetailExtra`
        if _data_type == "BabylonStakingActivityDetailExtra":
            instance.actual_instance = BabylonStakingActivityDetailExtra.from_json(json_str)
            return instance

        # check if data type is `CoreStakingActivityDetailExtra`
        if _data_type == "CoreStakingActivityDetailExtra":
            instance.actual_instance = CoreStakingActivityDetailExtra.from_json(json_str)
            return instance

        # check if data type is `EthStakingActivityDetailExtra`
        if _data_type == "EthStakingActivityDetailExtra":
            instance.actual_instance = EthStakingActivityDetailExtra.from_json(json_str)
            return instance

        return instance
        # deserialize data into BabylonStakingActivityDetailExtra
        try:
            instance.actual_instance = BabylonStakingActivityDetailExtra.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EthStakingActivityDetailExtra
        try:
            instance.actual_instance = EthStakingActivityDetailExtra.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CoreStakingActivityDetailExtra
        try:
            instance.actual_instance = CoreStakingActivityDetailExtra.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ActivityExtra with oneOf schemas: BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into ActivityExtra with oneOf schemas: BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BabylonStakingActivityDetailExtra, CoreStakingActivityDetailExtra, EthStakingActivityDetailExtra]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


