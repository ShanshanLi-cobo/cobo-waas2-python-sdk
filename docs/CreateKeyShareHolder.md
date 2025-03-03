# CreateKeyShareHolder

When creating MainKeyGroup and SigningKeyGroup, the Cobo key share holder will be added automatically.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Key share holder&#39;s name. | [optional] 
**type** | [**KeyShareHolderType**](KeyShareHolderType.md) |  | [optional] 
**tss_node_id** | **str** | Key share holder&#39;s TSS Node ID. You can obtain the TSS Node ID using either mobile co-signer or server co-signer. See the \&quot;Primary Purposes\&quot; row on the table in [Create a Main Group](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/create-key-share-groups#create-a-main-group). | [optional] 
**signer** | **bool** | Whether the key share holder has been selected as the designated transaction signer. For example, in a 2-3 [Threshold Signature Scheme (TSS)](https://manuals.cobo.com/en/portal/mpc-wallets/introduction#threshold-signature-scheme-tss), Cobo will serve as one signer, and you can choose one of the other two key share holders to act as the second transaction signer. - &#x60;true&#x60;: The key share holder is a designated transaction signer.  - &#x60;false&#x60;: The key share holder is not a designated transaction signer.  | [optional] 

## Example

```python
from cobo_waas2.models.create_key_share_holder import CreateKeyShareHolder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyShareHolder from a JSON string
create_key_share_holder_instance = CreateKeyShareHolder.from_json(json)
# print the JSON string representation of the object
print(CreateKeyShareHolder.to_json())

# convert the object into a dict
create_key_share_holder_dict = create_key_share_holder_instance.to_dict()
# create an instance of CreateKeyShareHolder from a dict
create_key_share_holder_from_dict = CreateKeyShareHolder.from_dict(create_key_share_holder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


