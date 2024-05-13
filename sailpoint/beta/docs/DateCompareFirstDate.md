# DateCompareFirstDate

This is the first date to consider (The date that would be on the left hand side of the comparison operation).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | A reference to the source to search for the account | 
**attribute_name** | **str** | The name of the attribute on the account to return. This should match the name of the account attribute name visible in the user interface, or on the source schema. | 
**account_sort_attribute** | **str** | The value of this configuration is a string name of the attribute to use when determining the ordering of returned accounts when there are multiple entries | [optional] [default to 'created']
**account_sort_descending** | **bool** | The value of this configuration is a boolean (true/false). Controls the order of the sort when there are multiple accounts. If not defined, the transform will default to false (ascending order) | [optional] [default to False]
**account_return_first_link** | **bool** | The value of this configuration is a boolean (true/false). Controls which account to source a value from for an attribute.  If this flag is set to true, the transform returns the value from the first account in the list, even if it is null. If it is set to false, the transform returns the first non-null value. If not defined, the transform will default to false | [optional] [default to False]
**account_filter** | **str** | This expression queries the database to narrow search results. The value of this configuration is a sailpoint.object.Filter expression and used when searching against the database.  The default filter will always include the source and identity, and any subsequent expressions will be combined in an AND operation to the existing search criteria. Only certain searchable attributes are available:  - &#x60;nativeIdentity&#x60; - the Account ID  - &#x60;displayName&#x60; - the Account Name  - &#x60;entitlements&#x60; - a boolean value to determine if the account has entitlements | [optional] 
**account_property_filter** | **str** | This expression is used to search and filter accounts in memory. The value of this configuration is a sailpoint.object.Filter expression and used when searching against the returned resultset.  All account attributes are available for filtering as this operation is performed in memory. | [optional] 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 
**input_format** | [**DateFormatInputFormat**](DateFormatInputFormat.md) |  | [optional] 
**output_format** | [**DateFormatOutputFormat**](DateFormatOutputFormat.md) |  | [optional] 

## Example

```python
from sailpoint.beta.models.date_compare_first_date import DateCompareFirstDate

# TODO update the JSON string below
json = "{}"
# create an instance of DateCompareFirstDate from a JSON string
date_compare_first_date_instance = DateCompareFirstDate.from_json(json)
# print the JSON string representation of the object
print DateCompareFirstDate.to_json()

# convert the object into a dict
date_compare_first_date_dict = date_compare_first_date_instance.to_dict()
# create an instance of DateCompareFirstDate from a dict
date_compare_first_date_form_dict = date_compare_first_date.from_dict(date_compare_first_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


