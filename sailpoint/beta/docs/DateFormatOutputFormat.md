# DateFormatOutputFormat

A string value indicating either the explicit SimpleDateFormat or the built-in named format that the data should be formatted into.  *If no inputFormat is provided, the transform assumes that it is in ISO8601 format*

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.beta.models.date_format_output_format import DateFormatOutputFormat

# TODO update the JSON string below
json = "{}"
# create an instance of DateFormatOutputFormat from a JSON string
date_format_output_format_instance = DateFormatOutputFormat.from_json(json)
# print the JSON string representation of the object
print DateFormatOutputFormat.to_json()

# convert the object into a dict
date_format_output_format_dict = date_format_output_format_instance.to_dict()
# create an instance of DateFormatOutputFormat from a dict
date_format_output_format_form_dict = date_format_output_format.from_dict(date_format_output_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


