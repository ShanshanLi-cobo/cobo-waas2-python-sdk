# TransactionRequestEvmEip1559Fee

The preset properties to limit transaction fee.  In the EIP-1559 fee model, the transaction fee is calculated by multiplying the gas price and the gas units used by the transaction. This can be expressed as: Transaction fee = gas price * gas units used. For more information about the EIP-1559 fee model, refer to [Fee models](https://www.cobo.com/developers/v2/guides/transactions/estimate-fees#fee-models).  You can specify the maximum gas fee per gas unit, maximum priority fee per gas unit, and the gas limit to limit the gas price, priority fee per gas unit, gas units used in the transaction.   Switch between the tabs to display the properties for different transaction fee models. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_fee_per_gas** | **str** | The maximum gas fee per gas unit used on the chain, in wei. | 
**max_priority_fee_per_gas** | **str** | The maximum priority fee per gas unit used, in wei. The maximum priority fee represents the highest amount of miner tips that you are willing to pay for your transaction. | 
**fee_type** | [**FeeType**](FeeType.md) |  | 
**token_id** | **str** | The token used to pay the transaction fee. | 
**gas_limit** | **str** | The gas limit. It represents the maximum number of gas units that you are willing to pay for the execution of a transaction or Ethereum Virtual Machine (EVM) operation. The gas unit cost of each operation varies. | [optional] 

## Example

```python
from cobo_waas2.models.transaction_request_evm_eip1559_fee import TransactionRequestEvmEip1559Fee

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRequestEvmEip1559Fee from a JSON string
transaction_request_evm_eip1559_fee_instance = TransactionRequestEvmEip1559Fee.from_json(json)
# print the JSON string representation of the object
print(TransactionRequestEvmEip1559Fee.to_json())

# convert the object into a dict
transaction_request_evm_eip1559_fee_dict = transaction_request_evm_eip1559_fee_instance.to_dict()
# create an instance of TransactionRequestEvmEip1559Fee from a dict
transaction_request_evm_eip1559_fee_from_dict = TransactionRequestEvmEip1559Fee.from_dict(transaction_request_evm_eip1559_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


