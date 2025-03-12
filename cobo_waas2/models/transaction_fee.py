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
from cobo_waas2.models.transaction_evm_eip1559_fee import TransactionEvmEip1559Fee
from cobo_waas2.models.transaction_evm_legacy_fee import TransactionEvmLegacyFee
from cobo_waas2.models.transaction_fixed_fee import TransactionFixedFee
from cobo_waas2.models.transaction_utxo_fee import TransactionUtxoFee
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSACTIONFEE_ONE_OF_SCHEMAS = ["TransactionEvmEip1559Fee", "TransactionEvmLegacyFee", "TransactionFixedFee", "TransactionUtxoFee"]

class TransactionFee(BaseModel):
    """
    TransactionFee
    """
    # data type: TransactionEvmEip1559Fee
    oneof_schema_1_validator: Optional[TransactionEvmEip1559Fee] = None
    # data type: TransactionEvmLegacyFee
    oneof_schema_2_validator: Optional[TransactionEvmLegacyFee] = None
    # data type: TransactionUtxoFee
    oneof_schema_3_validator: Optional[TransactionUtxoFee] = None
    # data type: TransactionFixedFee
    oneof_schema_4_validator: Optional[TransactionFixedFee] = None
    actual_instance: Optional[Union[TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee]] = None
    one_of_schemas: Set[str] = { "TransactionEvmEip1559Fee", "TransactionEvmLegacyFee", "TransactionFixedFee", "TransactionUtxoFee" }

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
        instance = TransactionFee.model_construct()
        error_messages = []
        match = 0
        # validate data type: TransactionEvmEip1559Fee
        if not isinstance(v, TransactionEvmEip1559Fee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionEvmEip1559Fee`")
        else:
            match += 1
        # validate data type: TransactionEvmLegacyFee
        if not isinstance(v, TransactionEvmLegacyFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionEvmLegacyFee`")
        else:
            match += 1
        # validate data type: TransactionUtxoFee
        if not isinstance(v, TransactionUtxoFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionUtxoFee`")
        else:
            match += 1
        # validate data type: TransactionFixedFee
        if not isinstance(v, TransactionFixedFee):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionFixedFee`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransactionFee with oneOf schemas: TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransactionFee with oneOf schemas: TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee. Details: " + ", ".join(error_messages))
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
        _data_type = json.loads(json_str).get("fee_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `fee_type` in the input.")

        # check if data type is `TransactionEvmEip1559Fee`
        if _data_type == "EVM_EIP_1559":
            instance.actual_instance = TransactionEvmEip1559Fee.from_json(json_str)
            return instance

        # check if data type is `TransactionEvmLegacyFee`
        if _data_type == "EVM_Legacy":
            instance.actual_instance = TransactionEvmLegacyFee.from_json(json_str)
            return instance

        # check if data type is `TransactionFixedFee`
        if _data_type == "Fixed":
            instance.actual_instance = TransactionFixedFee.from_json(json_str)
            return instance

        # check if data type is `TransactionUtxoFee`
        if _data_type == "UTXO":
            instance.actual_instance = TransactionUtxoFee.from_json(json_str)
            return instance

        # check if data type is `TransactionEvmEip1559Fee`
        if _data_type == "TransactionEvmEip1559Fee":
            instance.actual_instance = TransactionEvmEip1559Fee.from_json(json_str)
            return instance

        # check if data type is `TransactionEvmLegacyFee`
        if _data_type == "TransactionEvmLegacyFee":
            instance.actual_instance = TransactionEvmLegacyFee.from_json(json_str)
            return instance

        # check if data type is `TransactionFixedFee`
        if _data_type == "TransactionFixedFee":
            instance.actual_instance = TransactionFixedFee.from_json(json_str)
            return instance

        # check if data type is `TransactionUtxoFee`
        if _data_type == "TransactionUtxoFee":
            instance.actual_instance = TransactionUtxoFee.from_json(json_str)
            return instance

        return instance
        # deserialize data into TransactionEvmEip1559Fee
        try:
            instance.actual_instance = TransactionEvmEip1559Fee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionEvmLegacyFee
        try:
            instance.actual_instance = TransactionEvmLegacyFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionUtxoFee
        try:
            instance.actual_instance = TransactionUtxoFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionFixedFee
        try:
            instance.actual_instance = TransactionFixedFee.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionFee with oneOf schemas: TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            return instance
            # raise ValueError("No match found when deserializing the JSON string into TransactionFee with oneOf schemas: TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionEvmEip1559Fee, TransactionEvmLegacyFee, TransactionFixedFee, TransactionUtxoFee]]:
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


