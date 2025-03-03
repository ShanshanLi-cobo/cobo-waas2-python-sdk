# GetTransactionLimitation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vasp_list** | [**List[Vasp]**](Vasp.md) | A list of virtual asset service providers (VASP) you can select as the transaction source or destination. | [optional] 
**is_threshold_reached** | **bool** | Indicates whether the transaction amount exceeds a predefined threshold. If exceeded, additional information is required when filling Travel Rule details. - &#x60;true&#x60;: Threshold exceeded. - &#x60;false&#x60;: Threshold not exceeded.  | [optional] 
**self_custody_wallet_challenge** | **str** | A human-readable, time-sensitive message to be signed by the wallet owner. The message contains key information including the wallet address, a unique nonce, and a timestamp. Signing this message confirms ownership of the wallet and allows the operation to proceed.  | [optional] 
**connect_wallet_list** | **List[str]** | A list of self-custody wallet providers you can select as the transaction source or destination. | [optional] 

## Example

```python
from cobo_waas2.models.get_transaction_limitation200_response import GetTransactionLimitation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransactionLimitation200Response from a JSON string
get_transaction_limitation200_response_instance = GetTransactionLimitation200Response.from_json(json)
# print the JSON string representation of the object
print(GetTransactionLimitation200Response.to_json())

# convert the object into a dict
get_transaction_limitation200_response_dict = get_transaction_limitation200_response_instance.to_dict()
# create an instance of GetTransactionLimitation200Response from a dict
get_transaction_limitation200_response_from_dict = GetTransactionLimitation200Response.from_dict(get_transaction_limitation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


