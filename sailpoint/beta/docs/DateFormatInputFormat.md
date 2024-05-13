# DateFormatInputFormat

A string value indicating either the explicit SimpleDateFormat or the built-in named format that the data is coming in as.  *If no inputFormat is provided, the transform assumes that it is in ISO8601 format*

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from sailpoint.beta.models.date_format_input_format import DateFormatInputFormat

# TODO update the JSON string below
json = "{}"
# create an instance of DateFormatInputFormat from a JSON string
date_format_input_format_instance = DateFormatInputFormat.from_json(json)
# print the JSON string representation of the object
print DateFormatInputFormat.to_json()

# convert the object into a dict
date_format_input_format_dict = date_format_input_format_instance.to_dict()
# create an instance of DateFormatInputFormat from a dict
date_format_input_format_form_dict = date_format_input_format.from_dict(date_format_input_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


