# GenericRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the Generic rule that needs to be invoked by the transform | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] 

## Example

```python
from sailpoint.v3.models.generic_rule import GenericRule

# TODO update the JSON string below
json = "{}"
# create an instance of GenericRule from a JSON string
generic_rule_instance = GenericRule.from_json(json)
# print the JSON string representation of the object
print GenericRule.to_json()

# convert the object into a dict
generic_rule_dict = generic_rule_instance.to_dict()
# create an instance of GenericRule from a dict
generic_rule_form_dict = generic_rule.from_dict(generic_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


