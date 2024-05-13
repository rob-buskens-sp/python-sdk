# RandomAlphaNumeric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **str** | This is an integer value specifying the size/number of characters the random string must contain   * This value must be a positive number and cannot be blank   * If no length is provided, the transform will default to a value of &#x60;32&#x60;   * Due to identity attribute data constraints, the maximum allowable value is &#x60;450&#x60; characters  | [optional] 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.random_alpha_numeric import RandomAlphaNumeric

# TODO update the JSON string below
json = "{}"
# create an instance of RandomAlphaNumeric from a JSON string
random_alpha_numeric_instance = RandomAlphaNumeric.from_json(json)
# print the JSON string representation of the object
print RandomAlphaNumeric.to_json()

# convert the object into a dict
random_alpha_numeric_dict = random_alpha_numeric_instance.to_dict()
# create an instance of RandomAlphaNumeric from a dict
random_alpha_numeric_form_dict = random_alpha_numeric.from_dict(random_alpha_numeric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


