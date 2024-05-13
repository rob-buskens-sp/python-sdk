# DateCompare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_date** | [**DateCompareFirstDate**](DateCompareFirstDate.md) |  | 
**second_date** | [**DateCompareSecondDate**](DateCompareSecondDate.md) |  | 
**operator** | **str** | This is the comparison to perform. | Operation | Description | | --------- | ------- | | LT        | Strictly less than: firstDate &lt; secondDate | | LTE       | Less than or equal to: firstDate &lt;&#x3D; secondDate | | GT        | Strictly greater than: firstDate &gt; secondDate | | GTE       | Greater than or equal to: firstDate &gt;&#x3D; secondDate |  | 
**positive_condition** | **str** | The output of the transform if the expression evalutes to true | 
**negative_condition** | **str** | The output of the transform if the expression evalutes to false | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.date_compare import DateCompare

# TODO update the JSON string below
json = "{}"
# create an instance of DateCompare from a JSON string
date_compare_instance = DateCompare.from_json(json)
# print the JSON string representation of the object
print DateCompare.to_json()

# convert the object into a dict
date_compare_dict = date_compare_instance.to_dict()
# create an instance of DateCompare from a dict
date_compare_form_dict = date_compare.from_dict(date_compare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


