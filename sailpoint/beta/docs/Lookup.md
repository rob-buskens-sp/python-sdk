# Lookup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table** | **Dict[str, object]** | This is a JSON object of key-value pairs. The key is the string that will attempt to be matched to the input, and the value is the output string that should be returned if the key is matched   &gt;**Note** the use of the optional default key value here; if none of the three countries in the above example match the input string, the transform will return \&quot;Unknown Region\&quot; for the attribute that is mapped to this transform.  | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.lookup import Lookup

# TODO update the JSON string below
json = "{}"
# create an instance of Lookup from a JSON string
lookup_instance = Lookup.from_json(json)
# print the JSON string representation of the object
print Lookup.to_json()

# convert the object into a dict
lookup_dict = lookup_instance.to_dict()
# create an instance of Lookup from a dict
lookup_form_dict = lookup.from_dict(lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


