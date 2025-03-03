# BabylonStakingRegistration

The details of aBabylon Phase-2 registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The registration ID, a unique identifier for tracking the staking registration. | [optional] 
**staking_id** | **str** | The ID of the Phase-1 BTC staking position. | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**btc_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**status** | [**BabylonRegistrationRequestStatus**](BabylonRegistrationRequestStatus.md) |  | [optional] 
**staked_amount** | **str** | The amount of BTC that is staked. | [optional] 
**error_message** | **str** | The error message if the Babylon Phase-2 registration request failed. | [optional] 
**created_timestamp** | **int** | The time when the registration was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**updated_timestamp** | **int** | The time when the registration was updated, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.babylon_staking_registration import BabylonStakingRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonStakingRegistration from a JSON string
babylon_staking_registration_instance = BabylonStakingRegistration.from_json(json)
# print the JSON string representation of the object
print(BabylonStakingRegistration.to_json())

# convert the object into a dict
babylon_staking_registration_dict = babylon_staking_registration_instance.to_dict()
# create an instance of BabylonStakingRegistration from a dict
babylon_staking_registration_from_dict = BabylonStakingRegistration.from_dict(babylon_staking_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


