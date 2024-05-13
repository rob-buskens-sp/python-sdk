# Conditional


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | A comparison statement that follows the structure of &#x60;ValueA eq ValueB&#x60; where &#x60;ValueA&#x60; and &#x60;ValueB&#x60; are static strings or outputs of other transforms.   The &#x60;eq&#x60; operator is the only valid comparison | 
**positive_condition** | **str** | The output of the transform if the expression evalutes to true | 
**negative_condition** | **str** | The output of the transform if the expression evalutes to false | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.conditional import Conditional

# TODO update the JSON string below
json = "{}"
# create an instance of Conditional from a JSON string
conditional_instance = Conditional.from_json(json)
# print the JSON string representation of the object
print Conditional.to_json()

# convert the object into a dict
conditional_dict = conditional_instance.to_dict()
# create an instance of Conditional from a dict
conditional_form_dict = conditional.from_dict(conditional_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


