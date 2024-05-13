# Replace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regex** | **str** | This can be a string or a regex pattern in which you want to replace. | 
**replacement** | **str** | This is the replacement string that should be substituded wherever the string or pattern is found. | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.replace import Replace

# TODO update the JSON string below
json = "{}"
# create an instance of Replace from a JSON string
replace_instance = Replace.from_json(json)
# print the JSON string representation of the object
print Replace.to_json()

# convert the object into a dict
replace_dict = replace_instance.to_dict()
# create an instance of Replace from a dict
replace_form_dict = replace.from_dict(replace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


