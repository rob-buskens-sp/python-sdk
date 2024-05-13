# Substring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **int** | The index of the first character to include in the returned substring.   If &#x60;begin&#x60; is set to -1, the transform will begin at character 0 of the input data  | 
**begin_offset** | **int** | This integer value is the number of characters to add to the begin attribute when returning a substring.   This attribute is only used if begin is not -1.  | [optional] 
**end** | **int** | The index of the first character to exclude from the returned substring.  If end is -1 or not provided at all, the substring transform will return everything up to the end of the input string.  | [optional] 
**end_offset** | **int** | This integer value is the number of characters to add to the end attribute when returning a substring.   This attribute is only used if end is provided and is not -1.  | [optional] 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.substring import Substring

# TODO update the JSON string below
json = "{}"
# create an instance of Substring from a JSON string
substring_instance = Substring.from_json(json)
# print the JSON string representation of the object
print Substring.to_json()

# convert the object into a dict
substring_dict = substring_instance.to_dict()
# create an instance of Substring from a dict
substring_form_dict = substring.from_dict(substring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


