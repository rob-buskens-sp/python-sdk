# ReplaceAll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **Dict[str, object]** | An attribute of key-value pairs. Each pair identifies the pattern to search for as its key, and the replacement string as its value. | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.replace_all import ReplaceAll

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceAll from a JSON string
replace_all_instance = ReplaceAll.from_json(json)
# print the JSON string representation of the object
print ReplaceAll.to_json()

# convert the object into a dict
replace_all_dict = replace_all_instance.to_dict()
# create an instance of ReplaceAll from a dict
replace_all_form_dict = replace_all.from_dict(replace_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


