# E164phone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_region** | **str** | This is an optional attribute that can be used to define the region of the phone number to format into.   If defaultRegion is not provided, it will take US as the default country.   The format of the country code should be in [ISO 3166-1 alpha-2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)  | [optional] 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.e164phone import E164phone

# TODO update the JSON string below
json = "{}"
# create an instance of E164phone from a JSON string
e164phone_instance = E164phone.from_json(json)
# print the JSON string representation of the object
print E164phone.to_json()

# convert the object into a dict
e164phone_dict = e164phone_instance.to_dict()
# create an instance of E164phone from a dict
e164phone_form_dict = e164phone.from_dict(e164phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


