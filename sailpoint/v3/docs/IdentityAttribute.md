# IdentityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The system (camel-cased) name of the identity attribute to bring in | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.identity_attribute import IdentityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttribute from a JSON string
identity_attribute_instance = IdentityAttribute.from_json(json)
# print the JSON string representation of the object
print IdentityAttribute.to_json()

# convert the object into a dict
identity_attribute_dict = identity_attribute_instance.to_dict()
# create an instance of IdentityAttribute from a dict
identity_attribute_form_dict = identity_attribute.from_dict(identity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


