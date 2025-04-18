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
from cobo_waas2.models.babylon_stake_estimated_fee import BabylonStakeEstimatedFee
from cobo_waas2.models.eth_stake_estimated_fee import EthStakeEstimatedFee
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETSTAKINGESTIMATIONFEE201RESPONSE_ONE_OF_SCHEMAS = ["BabylonStakeEstimatedFee", "EthStakeEstimatedFee"]

class GetStakingEstimationFee201Response(BaseModel):
    """
    GetStakingEstimationFee201Response
    """
    # data type: EthStakeEstimatedFee
    oneof_schema_1_validator: Optional[EthStakeEstimatedFee] = None
    # data type: BabylonStakeEstimatedFee
    oneof_schema_2_validator: Optional[BabylonStakeEstimatedFee] = None
    actual_instance: Optional[Union[BabylonStakeEstimatedFee, EthStakeEstimatedFee]] = None
    one_of_schemas: Set[str] = { "BabylonStakeEstimatedFee", "EthStakeEstimatedFee" }

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
        instance = GetStakingEstimationFee201Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: EthStakeEstimatedFee
        if not isinstance(v, EthStakeEstimatedFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EthStakeEstimatedFee`")
        else:
            match += 1
        # validate data type: BabylonStakeEstimatedFee
        if not isinstance(v, BabylonStakeEstimatedFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BabylonStakeEstimatedFee`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetStakingEstimationFee201Response with oneOf schemas: BabylonStakeEstimatedFee, EthStakeEstimatedFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetStakingEstimationFee201Response with oneOf schemas: BabylonStakeEstimatedFee, EthStakeEstimatedFee. Details: " + ", ".join(error_messages))
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

        # check if data type is `BabylonStakeEstimatedFee`
        if _data_type == "Babylon":
            instance.actual_instance = BabylonStakeEstimatedFee.from_json(json_str)
            return instance

        # check if data type is `EthStakeEstimatedFee`
        if _data_type == "ETHBeacon":
            instance.actual_instance = EthStakeEstimatedFee.from_json(json_str)
            return instance

        # check if data type is `BabylonStakeEstimatedFee`
        if _data_type == "BabylonStakeEstimatedFee":
            instance.actual_instance = BabylonStakeEstimatedFee.from_json(json_str)
            return instance

        # check if data type is `EthStakeEstimatedFee`
        if _data_type == "EthStakeEstimatedFee":
            instance.actual_instance = EthStakeEstimatedFee.from_json(json_str)
            return instance

        return instance
        # deserialize data into EthStakeEstimatedFee
        try:
            instance.actual_instance = EthStakeEstimatedFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BabylonStakeEstimatedFee
        try:
            instance.actual_instance = BabylonStakeEstimatedFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetStakingEstimationFee201Response with oneOf schemas: BabylonStakeEstimatedFee, EthStakeEstimatedFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into GetStakingEstimationFee201Response with oneOf schemas: BabylonStakeEstimatedFee, EthStakeEstimatedFee. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BabylonStakeEstimatedFee, EthStakeEstimatedFee]]:
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


