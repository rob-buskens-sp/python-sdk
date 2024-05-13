# NameNormalizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.name_normalizer import NameNormalizer

# TODO update the JSON string below
json = "{}"
# create an instance of NameNormalizer from a JSON string
name_normalizer_instance = NameNormalizer.from_json(json)
# print the JSON string representation of the object
print NameNormalizer.to_json()

# convert the object into a dict
name_normalizer_dict = name_normalizer_instance.to_dict()
# create an instance of NameNormalizer from a dict
name_normalizer_form_dict = name_normalizer.from_dict(name_normalizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


