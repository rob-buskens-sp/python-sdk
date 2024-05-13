# FirstValid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[object]** | An array of attributes to evaluate for existence. | 
**ignore_errors** | **bool** | a true or false value representing to move on to the next option if an error (like an Null Pointer Exception) were to occur. | [optional] [default to False]
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.first_valid import FirstValid

# TODO update the JSON string below
json = "{}"
# create an instance of FirstValid from a JSON string
first_valid_instance = FirstValid.from_json(json)
# print the JSON string representation of the object
print FirstValid.to_json()

# convert the object into a dict
first_valid_dict = first_valid_instance.to_dict()
# create an instance of FirstValid from a dict
first_valid_form_dict = first_valid.from_dict(first_valid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


