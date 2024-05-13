# GetReferenceIdentityAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This must always be set to \&quot;Cloud Services Deployment Utility\&quot; | 
**operation** | **str** | The operation to perform &#x60;getReferenceIdentityAttribute&#x60; | 
**uid** | **str** | This is the SailPoint User Name (uid) value of the identity whose attribute is desired  As a convenience feature, you can use the &#x60;manager&#x60; keyword to dynamically look up the user&#39;s manager and then get that manager&#39;s identity attribute.  | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] 

## Example

```python
from sailpoint.beta.models.get_reference_identity_attribute import GetReferenceIdentityAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceIdentityAttribute from a JSON string
get_reference_identity_attribute_instance = GetReferenceIdentityAttribute.from_json(json)
# print the JSON string representation of the object
print GetReferenceIdentityAttribute.to_json()

# convert the object into a dict
get_reference_identity_attribute_dict = get_reference_identity_attribute_instance.to_dict()
# create an instance of GetReferenceIdentityAttribute from a dict
get_reference_identity_attribute_form_dict = get_reference_identity_attribute.from_dict(get_reference_identity_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


