# HoldingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s** | **str** |  | [optional] 
**d** | [**HoldingData**](HoldingData.md) |  | [optional] 

## Example

```python
from openapi_client.models.holding_response import HoldingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingResponse from a JSON string
holding_response_instance = HoldingResponse.from_json(json)
# print the JSON string representation of the object
print HoldingResponse.to_json()

# convert the object into a dict
holding_response_dict = holding_response_instance.to_dict()
# create an instance of HoldingResponse from a dict
holding_response_form_dict = holding_response.from_dict(holding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


