# TransactionApprovalDetail

The approval detail data for transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | [optional] 
**cobo_id** | **str** | The Cobo ID, which can be used to track a transaction. | [optional] 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 
**spender** | [**TransactionRoleApprovalDetail**](TransactionRoleApprovalDetail.md) |  | [optional] 
**approver** | [**TransactionRoleApprovalDetail**](TransactionRoleApprovalDetail.md) |  | [optional] 
**address_owner** | [**TransactionRoleApprovalDetail**](TransactionRoleApprovalDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.transaction_approval_detail import TransactionApprovalDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionApprovalDetail from a JSON string
transaction_approval_detail_instance = TransactionApprovalDetail.from_json(json)
# print the JSON string representation of the object
print(TransactionApprovalDetail.to_json())

# convert the object into a dict
transaction_approval_detail_dict = transaction_approval_detail_instance.to_dict()
# create an instance of TransactionApprovalDetail from a dict
transaction_approval_detail_from_dict = TransactionApprovalDetail.from_dict(transaction_approval_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


