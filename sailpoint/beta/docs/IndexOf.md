# IndexOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**substring** | **str** | A substring to search for, searches the entire calling string, and returns the index of the first occurrence of the specified substring. | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.index_of import IndexOf

# TODO update the JSON string below
json = "{}"
# create an instance of IndexOf from a JSON string
index_of_instance = IndexOf.from_json(json)
# print the JSON string representation of the object
print IndexOf.to_json()

# convert the object into a dict
index_of_dict = index_of_instance.to_dict()
# create an instance of IndexOf from a dict
index_of_form_dict = index_of.from_dict(index_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


