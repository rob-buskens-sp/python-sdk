# UUIDGenerator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.uuid_generator import UUIDGenerator

# TODO update the JSON string below
json = "{}"
# create an instance of UUIDGenerator from a JSON string
uuid_generator_instance = UUIDGenerator.from_json(json)
# print the JSON string representation of the object
print UUIDGenerator.to_json()

# convert the object into a dict
uuid_generator_dict = uuid_generator_instance.to_dict()
# create an instance of UUIDGenerator from a dict
uuid_generator_form_dict = uuid_generator.from_dict(uuid_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


