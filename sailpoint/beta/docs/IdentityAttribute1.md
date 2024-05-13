# IdentityAttribute1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The system (camel-cased) name of the identity attribute to bring in | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.identity_attribute1 import IdentityAttribute1

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityAttribute1 from a JSON string
identity_attribute1_instance = IdentityAttribute1.from_json(json)
# print the JSON string representation of the object
print IdentityAttribute1.to_json()

# convert the object into a dict
identity_attribute1_dict = identity_attribute1_instance.to_dict()
# create an instance of IdentityAttribute1 from a dict
identity_attribute1_form_dict = identity_attribute1.from_dict(identity_attribute1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


