# DateMath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | A string value of the date and time components to operation on, along with the math operations to execute.  | 
**round_up** | **bool** | A boolean value to indicate whether the transform should round up or down when a rounding &#x60;/&#x60; operation is defined in the expression.    If not provided, the transform will default to &#x60;false&#x60;   &#x60;true&#x60; indicates the transform should round up (i.e., truncate the fractional date/time component indicated and then add one unit of that component)   &#x60;false&#x60; indicates the transform should round down (i.e., truncate the fractional date/time component indicated)  | [optional] [default to False]
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.date_math import DateMath

# TODO update the JSON string below
json = "{}"
# create an instance of DateMath from a JSON string
date_math_instance = DateMath.from_json(json)
# print the JSON string representation of the object
print DateMath.to_json()

# convert the object into a dict
date_math_dict = date_math_instance.to_dict()
# create an instance of DateMath from a dict
date_math_form_dict = date_math.from_dict(date_math_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


