# StakingsExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**pos_chain** | **str** | The Proof-of-Stake (PoS) chain. | 
**unlock_timestamp** | **int** | The estimated time when the bitcoins will be unlocked, in Unix timestamp format, measured in milliseconds. | [optional] 
**unlock_block_height** | **int** | The block height at which the bitcoins will be unlocked. | [optional] 
**stake_address** | **str** | The address receiving the staked bitcoins. | [optional] 
**unbond_address** | **str** | The address receiving the unlocked bitcoins. | [optional] 
**beacon_validators** | [**List[EthStakingExtraAllOfBeaconValidators]**](EthStakingExtraAllOfBeaconValidators.md) | The list of validator information. | [optional] 
**staker_address** | **str** | The staker&#39;s Bitcoin address. | 
**validator_address** | **str** | The validator&#39;s EVM address. | 
**reward_address** | **str** | The EVM address to receive staking rewards. | 
**timelock** | **int** | The Unix timestamp (in seconds) when the staking position will be unlocked and available for withdrawal. | 

## Example

```python
from cobo_waas2.models.stakings_extra import StakingsExtra

# TODO update the JSON string below
json = "{}"
# create an instance of StakingsExtra from a JSON string
stakings_extra_instance = StakingsExtra.from_json(json)
# print the JSON string representation of the object
print(StakingsExtra.to_json())

# convert the object into a dict
stakings_extra_dict = stakings_extra_instance.to_dict()
# create an instance of StakingsExtra from a dict
stakings_extra_from_dict = StakingsExtra.from_dict(stakings_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


