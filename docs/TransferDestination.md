# TransferDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_type** | [**TransferDestinationType**](TransferDestinationType.md) |  | 
**account_output** | [**AddressTransferDestinationAccountOutput**](AddressTransferDestinationAccountOutput.md) |  | [optional] 
**utxo_outputs** | [**List[AddressTransferDestinationUtxoOutputsInner]**](AddressTransferDestinationUtxoOutputsInner.md) |  | [optional] 
**change_address** | **str** | The address used to receive the remaining funds or change from the transaction. | [optional] 
**change_output_type** | **str** | The position of the change output in the transaction&#39;s outputs. Possible values are: - &#x60;Last&#x60;: The change output is placed at the end of the transaction&#39;s outputs.   - &#x60;First&#x60;: The change output is placed at the beginning of the transaction&#39;s outputs.  | [optional] 
**force_internal** | **bool** | Whether the transaction request must be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - &#x60;true&#x60;: The transaction request must be executed as a Cobo Loop transfer.   - &#x60;false&#x60;: The transaction request may not be executed as a Cobo Loop transfer.    Please do not set both &#x60;force_internal&#x60; and &#x60;force_external&#x60; as &#x60;true&#x60;. If both are set to &#x60;false&#x60;, the system uses Cobo Loop by default if possible; otherwise, it proceeds with an on-chain transfer.  | [optional] 
**force_external** | **bool** | Whether the transaction request must not be executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer.   - &#x60;true&#x60;: The transaction request must not be executed as a Cobo Loop transfer.   - &#x60;false&#x60;: The transaction request can be executed as a Cobo Loop transfer.  Please do not set both &#x60;force_internal&#x60; and &#x60;force_external&#x60; as &#x60;true&#x60;. If both are set to &#x60;false&#x60;, the system uses Cobo Loop by default if possible; otherwise, it proceeds with an on-chain transfer.  | [optional] 
**wallet_id** | **str** | The wallet ID. | 
**amount** | **str** | The transfer amount. For example, if you trade 1.5 BTC, then the value is &#x60;1.5&#x60;.  | 
**trading_account_type** | **str** | The trading account type. | 

## Example

```python
from cobo_waas2.models.transfer_destination import TransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDestination from a JSON string
transfer_destination_instance = TransferDestination.from_json(json)
# print the JSON string representation of the object
print(TransferDestination.to_json())

# convert the object into a dict
transfer_destination_dict = transfer_destination_instance.to_dict()
# create an instance of TransferDestination from a dict
transfer_destination_from_dict = TransferDestination.from_dict(transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


