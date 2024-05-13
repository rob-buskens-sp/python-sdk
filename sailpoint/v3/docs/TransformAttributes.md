# TransformAttributes

Meta-data about the transform. Values in this list are specific to the type of transform to be executed.

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
**values** | **str** | This must evaluate to a JSON string, either through a fixed value or through conditional logic using the Apache Velocity Template Language. | 
**expression** | **str** | A string value of the date and time components to operation on, along with the math operations to execute.  | 
**positive_condition** | **str** | The output of the transform if the expression evalutes to true | 
**negative_condition** | **str** | The output of the transform if the expression evalutes to false | 
**first_date** | [**DateCompareFirstDate**](DateCompareFirstDate.md) |  | 
**second_date** | [**DateCompareSecondDate**](DateCompareSecondDate.md) |  | 
**operator** | **str** | This is the comparison to perform. | Operation | Description | | --------- | ------- | | LT        | Strictly less than: firstDate &lt; secondDate | | LTE       | Less than or equal to: firstDate &lt;&#x3D; secondDate | | GT        | Strictly greater than: firstDate &gt; secondDate | | GTE       | Greater than or equal to: firstDate &gt;&#x3D; secondDate |  | 
**input_format** | [**DateFormatInputFormat**](DateFormatInputFormat.md) |  | [optional] 
**output_format** | [**DateFormatOutputFormat**](DateFormatOutputFormat.md) |  | [optional] 
**round_up** | **bool** | A boolean value to indicate whether the transform should round up or down when a rounding &#x60;/&#x60; operation is defined in the expression.    If not provided, the transform will default to &#x60;false&#x60;   &#x60;true&#x60; indicates the transform should round up (i.e., truncate the fractional date/time component indicated and then add one unit of that component)   &#x60;false&#x60; indicates the transform should round down (i.e., truncate the fractional date/time component indicated)  | [optional] [default to False]
**default_region** | **str** | This is an optional attribute that can be used to define the region of the phone number to format into.   If defaultRegion is not provided, it will take US as the default country.   The format of the country code should be in [ISO 3166-1 alpha-2 format](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)  | [optional] 
**ignore_errors** | **bool** | a true or false value representing to move on to the next option if an error (like an Null Pointer Exception) were to occur. | [optional] [default to False]
**name** | **str** | The system (camel-cased) name of the identity attribute to bring in | 
**operation** | **str** | The operation to perform &#x60;getReferenceIdentityAttribute&#x60; | 
**include_numbers** | **bool** | This must be either \&quot;true\&quot; or \&quot;false\&quot; to indicate whether the generator logic should include numbers | 
**include_special_chars** | **bool** | This must be either \&quot;true\&quot; or \&quot;false\&quot; to indicate whether the generator logic should include special characters | 
**length** | **str** | An integer value for the desired length of the final output string | 
**uid** | **str** | This is the SailPoint User Name (uid) value of the identity whose attribute is desired  As a convenience feature, you can use the &#x60;manager&#x60; keyword to dynamically look up the user&#39;s manager and then get that manager&#39;s identity attribute.  | 
**substring** | **str** | A substring to search for, searches the entire calling string, and returns the index of the first occurrence of the specified substring. | 
**format** | **str** | An optional value to denote which ISO 3166 format to return. Valid values are:   &#x60;alpha2&#x60; - Two-character country code (e.g., \&quot;US\&quot;); this is the default value if no format is supplied   &#x60;alpha3&#x60; - Three-character country code (e.g., \&quot;USA\&quot;)   &#x60;numeric&#x60; - The numeric country code (e.g., \&quot;840\&quot;)  | [optional] 
**padding** | **str** | A string value representing the character that the incoming data should be padded with to get to the desired length   If not provided, the transform will default to a single space (\&quot; \&quot;) character for padding  | [optional] 
**table** | **Dict[str, object]** | An attribute of key-value pairs. Each pair identifies the pattern to search for as its key, and the replacement string as its value. | 
**id** | **str** | This ID specifies the name of the pre-existing transform which you want to use within your current transform | 
**regex** | **str** | This can be a string or a regex pattern in which you want to replace. | 
**replacement** | **str** | This is the replacement string that should be substituded wherever the string or pattern is found. | 
**delimiter** | **str** | This can be either a single character or a regex expression, and is used by the transform to identify the break point between two substrings in the incoming data | 
**index** | **str** | An integer value for the desired array element after the incoming data has been split into a list; the array is a 0-based object, so the first array element would be index 0, the second element would be index 1, etc. | 
**throws** | **bool** | A boolean (true/false) value which indicates whether an exception should be thrown and returned as an output when an index is out of bounds with the resultant array (i.e., the provided index value is larger than the size of the array)   &#x60;true&#x60; - The transform should return \&quot;IndexOutOfBoundsException\&quot;   &#x60;false&#x60; - The transform should return null   If not provided, the transform will default to false and return a null  | [optional] [default to False]
**begin** | **int** | The index of the first character to include in the returned substring.   If &#x60;begin&#x60; is set to -1, the transform will begin at character 0 of the input data  | 
**begin_offset** | **int** | This integer value is the number of characters to add to the begin attribute when returning a substring.   This attribute is only used if begin is not -1.  | [optional] 
**end** | **int** | The index of the first character to exclude from the returned substring.  If end is -1 or not provided at all, the substring transform will return everything up to the end of the input string.  | [optional] 
**end_offset** | **int** | This integer value is the number of characters to add to the end attribute when returning a substring.   This attribute is only used if end is provided and is not -1.  | [optional] 

## Example

```python
from sailpoint.v3.models.transform_attributes import TransformAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TransformAttributes from a JSON string
transform_attributes_instance = TransformAttributes.from_json(json)
# print the JSON string representation of the object
print TransformAttributes.to_json()

# convert the object into a dict
transform_attributes_dict = transform_attributes_instance.to_dict()
# create an instance of TransformAttributes from a dict
transform_attributes_form_dict = transform_attributes.from_dict(transform_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


