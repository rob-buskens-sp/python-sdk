# RightPad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **str** | An integer value for the desired length of the final output string | 
**padding** | **str** | A string value representing the character that the incoming data should be padded with to get to the desired length   If not provided, the transform will default to a single space (\&quot; \&quot;) character for padding  | [optional] 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.right_pad import RightPad

# TODO update the JSON string below
json = "{}"
# create an instance of RightPad from a JSON string
right_pad_instance = RightPad.from_json(json)
# print the JSON string representation of the object
print RightPad.to_json()

# convert the object into a dict
right_pad_dict = right_pad_instance.to_dict()
# create an instance of RightPad from a dict
right_pad_form_dict = right_pad.from_dict(right_pad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


