# TokenizationERC20TokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standard** | [**TokenizationTokenStandard**](TokenizationTokenStandard.md) |  | 
**name** | **str** | The name of the token. | 
**symbol** | **str** | The symbol of the token. | 
**decimals** | **int** | The number of decimals for the token (0-18). | 
**allowlist_activated** | **bool** | Whether the allowlist feature is activated for the token. When activated, only addresses in the allowlist can perform token operations. | [optional] [default to False]
**permissions** | [**TokenizationTokenPermissionParams**](TokenizationTokenPermissionParams.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_erc20_token_params import TokenizationERC20TokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationERC20TokenParams from a JSON string
tokenization_erc20_token_params_instance = TokenizationERC20TokenParams.from_json(json)
# print the JSON string representation of the object
print(TokenizationERC20TokenParams.to_json())

# convert the object into a dict
tokenization_erc20_token_params_dict = tokenization_erc20_token_params_instance.to_dict()
# create an instance of TokenizationERC20TokenParams from a dict
tokenization_erc20_token_params_from_dict = TokenizationERC20TokenParams.from_dict(tokenization_erc20_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


