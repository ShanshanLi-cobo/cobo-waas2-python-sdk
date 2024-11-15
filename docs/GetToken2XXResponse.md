# GetToken2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The Org Access Token. | [optional] 
**token_type** | **str** | The type of the tokens, which is Bearer. | [optional] 
**scope** | **str** | The scope of the Org Access Token to limit the app&#39;s access to the organization&#39;s resources.  **Note**: Currently this property value is empty. The scope of the Org Access Token is based on the permissions granted when the app user installs the app.  | [optional] 
**expires_in** | **int** | The time in seconds in which the Org Access Token expires. | [optional] 
**refresh_token** | **str** | The Refresh Token, used to obtain a new Org Access Token when the current Org Access Token expires. The expiration time for Refresh Tokens is currently set to 30 days and is subject to change. | [optional] 

## Example

```python
from cobo_waas2.models.get_token2_xx_response import GetToken2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetToken2XXResponse from a JSON string
get_token2_xx_response_instance = GetToken2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetToken2XXResponse.to_json())

# convert the object into a dict
get_token2_xx_response_dict = get_token2_xx_response_instance.to_dict()
# create an instance of GetToken2XXResponse from a dict
get_token2_xx_response_from_dict = GetToken2XXResponse.from_dict(get_token2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


