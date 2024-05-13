# DecomposeDiacriticalMarks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.decompose_diacritical_marks import DecomposeDiacriticalMarks

# TODO update the JSON string below
json = "{}"
# create an instance of DecomposeDiacriticalMarks from a JSON string
decompose_diacritical_marks_instance = DecomposeDiacriticalMarks.from_json(json)
# print the JSON string representation of the object
print DecomposeDiacriticalMarks.to_json()

# convert the object into a dict
decompose_diacritical_marks_dict = decompose_diacritical_marks_instance.to_dict()
# create an instance of DecomposeDiacriticalMarks from a dict
decompose_diacritical_marks_form_dict = decompose_diacritical_marks.from_dict(decompose_diacritical_marks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


