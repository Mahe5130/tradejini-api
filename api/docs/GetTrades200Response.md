# GetTrades200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] 
**d** | [**List[TradeRecord]**](TradeRecord.md) |  | [optional] 
**msg** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_trades200_response import GetTrades200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrades200Response from a JSON string
get_trades200_response_instance = GetTrades200Response.from_json(json)
# print the JSON string representation of the object
print GetTrades200Response.to_json()

# convert the object into a dict
get_trades200_response_dict = get_trades200_response_instance.to_dict()
# create an instance of GetTrades200Response from a dict
get_trades200_response_form_dict = get_trades200_response.from_dict(get_trades200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


