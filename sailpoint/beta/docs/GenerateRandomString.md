# GenerateRandomString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This must always be set to \&quot;Cloud Services Deployment Utility\&quot; | 
**operation** | **str** | The operation to perform &#x60;generateRandomString&#x60; | 
**include_numbers** | **bool** | This must be either \&quot;true\&quot; or \&quot;false\&quot; to indicate whether the generator logic should include numbers | 
**include_special_chars** | **bool** | This must be either \&quot;true\&quot; or \&quot;false\&quot; to indicate whether the generator logic should include special characters | 
**length** | **str** | This specifies how long the randomly generated string needs to be   &gt;NOTE Due to identity attribute data constraints, the maximum allowable value is 450 characters  | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] 

## Example

```python
from sailpoint.beta.models.generate_random_string import GenerateRandomString

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateRandomString from a JSON string
generate_random_string_instance = GenerateRandomString.from_json(json)
# print the JSON string representation of the object
print GenerateRandomString.to_json()

# convert the object into a dict
generate_random_string_dict = generate_random_string_instance.to_dict()
# create an instance of GenerateRandomString from a dict
generate_random_string_form_dict = generate_random_string.from_dict(generate_random_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


