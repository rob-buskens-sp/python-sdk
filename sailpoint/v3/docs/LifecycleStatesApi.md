# sailpoint.v3.LifecycleStatesApi

All URIs are relative to *https://sailpoint.api.identitynow.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lifecycle_state**](LifecycleStatesApi.md#create_lifecycle_state) | **POST** /identity-profiles/{identity-profile-id}/lifecycle-states | Create Lifecycle State
[**delete_lifecycle_state**](LifecycleStatesApi.md#delete_lifecycle_state) | **DELETE** /identity-profiles/{identity-profile-id}/lifecycle-states/{lifecycle-state-id} | Delete Lifecycle State by ID
[**get_lifecycle_state**](LifecycleStatesApi.md#get_lifecycle_state) | **GET** /identity-profiles/{identity-profile-id}/lifecycle-states/{lifecycle-state-id} | Retrieves Lifecycle State
[**list_lifecycle_states**](LifecycleStatesApi.md#list_lifecycle_states) | **GET** /identity-profiles/{identity-profile-id}/lifecycle-states | Lists LifecycleStates
[**set_lifecycle_state**](LifecycleStatesApi.md#set_lifecycle_state) | **POST** /identities/{identity-id}/set-lifecycle-state | Set Lifecycle State
[**update_lifecycle_states**](LifecycleStatesApi.md#update_lifecycle_states) | **PATCH** /identity-profiles/{identity-profile-id}/lifecycle-states/{lifecycle-state-id} | Update Lifecycle State


# **create_lifecycle_state**
> LifecycleState create_lifecycle_state(identity_profile_id, lifecycle_state)

Create Lifecycle State

This API creates a new Lifecycle State. A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.lifecycle_state import LifecycleState
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_profile_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Identity Profile ID
    lifecycle_state = sailpoint.v3.LifecycleState() # LifecycleState | Lifecycle State

    try:
        # Create Lifecycle State
        api_response = api_instance.create_lifecycle_state(identity_profile_id, lifecycle_state)
        print("The response of LifecycleStatesApi->create_lifecycle_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->create_lifecycle_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| Identity Profile ID | 
 **lifecycle_state** | [**LifecycleState**](LifecycleState.md)| Lifecycle State | 

### Return type

[**LifecycleState**](LifecycleState.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created LifecycleState object. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lifecycle_state**
> LifecyclestateDeleted delete_lifecycle_state(identity_profile_id, lifecycle_state_id)

Delete Lifecycle State by ID

This endpoint deletes the Lifecycle State using its ID. A token with API, or ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.lifecyclestate_deleted import LifecyclestateDeleted
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_profile_id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | Identity Profile ID
    lifecycle_state_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Lifecycle State ID

    try:
        # Delete Lifecycle State by ID
        api_response = api_instance.delete_lifecycle_state(identity_profile_id, lifecycle_state_id)
        print("The response of LifecycleStatesApi->delete_lifecycle_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->delete_lifecycle_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| Identity Profile ID | 
 **lifecycle_state_id** | **str**| Lifecycle State ID | 

### Return type

[**LifecyclestateDeleted**](LifecyclestateDeleted.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lifecycle_state**
> LifecycleState get_lifecycle_state(identity_profile_id, lifecycle_state_id)

Retrieves Lifecycle State

This endpoint retrieves a Lifecycle State. A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.lifecycle_state import LifecycleState
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_profile_id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | Identity Profile ID
    lifecycle_state_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Lifecycle State ID

    try:
        # Retrieves Lifecycle State
        api_response = api_instance.get_lifecycle_state(identity_profile_id, lifecycle_state_id)
        print("The response of LifecycleStatesApi->get_lifecycle_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->get_lifecycle_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| Identity Profile ID | 
 **lifecycle_state_id** | **str**| Lifecycle State ID | 

### Return type

[**LifecycleState**](LifecycleState.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested LifecycleState was successfully retrieved. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lifecycle_states**
> List[LifecycleState] list_lifecycle_states(identity_profile_id, limit=limit, offset=offset, count=count, sorters=sorters)

Lists LifecycleStates

This end-point lists all the LifecycleStates associated with IdentityProfiles. A token with API, or ORG_ADMIN authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.lifecycle_state import LifecycleState
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_profile_id = 'ef38f94347e94562b5bb8424a56397d8' # str | The IdentityProfile id
    limit = 250 # int | Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 250)
    offset = 0 # int | Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to 0)
    count = False # bool | If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. (optional) (default to False)
    sorters = 'created,modified' # str | Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** (optional)

    try:
        # Lists LifecycleStates
        api_response = api_instance.list_lifecycle_states(identity_profile_id, limit=limit, offset=offset, count=count, sorters=sorters)
        print("The response of LifecycleStatesApi->list_lifecycle_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->list_lifecycle_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| The IdentityProfile id | 
 **limit** | **int**| Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 250]
 **offset** | **int**| Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to 0]
 **count** | **bool**| If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count&#x3D;true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information. | [optional] [default to False]
 **sorters** | **str**| Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **created, modified** | [optional] 

### Return type

[**List[LifecycleState]**](LifecycleState.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of LifecycleState objects |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lifecycle_state**
> SetLifecycleState200Response set_lifecycle_state(identity_id, set_lifecycle_state_request)

Set Lifecycle State

This endpoint will set/update an identity's lifecycle state to the one provided and updates the corresponding identity profile. A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.set_lifecycle_state200_response import SetLifecycleState200Response
from sailpoint.v3.models.set_lifecycle_state_request import SetLifecycleStateRequest
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_id = '2c9180857893f1290178944561990364' # str | The ID of the identity to update.
    set_lifecycle_state_request = sailpoint.v3.SetLifecycleStateRequest() # SetLifecycleStateRequest | 

    try:
        # Set Lifecycle State
        api_response = api_instance.set_lifecycle_state(identity_id, set_lifecycle_state_request)
        print("The response of LifecycleStatesApi->set_lifecycle_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->set_lifecycle_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_id** | **str**| The ID of the identity to update. | 
 **set_lifecycle_state_request** | [**SetLifecycleStateRequest**](SetLifecycleStateRequest.md)|  | 

### Return type

[**SetLifecycleState200Response**](SetLifecycleState200Response.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successfully accepted into the system. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lifecycle_states**
> LifecycleState update_lifecycle_states(identity_profile_id, lifecycle_state_id, json_patch_operation)

Update Lifecycle State

This endpoint updates individual Lifecycle State fields using the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard. A token with ORG_ADMIN or API authority is required to call this API.

### Example

* OAuth Authentication (UserContextAuth):
* OAuth Authentication (UserContextAuth):

```python
import time
import os
import sailpoint.v3
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation
from sailpoint.v3.models.lifecycle_state import LifecycleState
from sailpoint.v3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://sailpoint.api.identitynow.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = sailpoint.v3.Configuration(
    host = "https://sailpoint.api.identitynow.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with sailpoint.v3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sailpoint.v3.LifecycleStatesApi(api_client)
    identity_profile_id = '2b838de9-db9b-abcf-e646-d4f274ad4238' # str | Identity Profile ID
    lifecycle_state_id = 'ef38f94347e94562b5bb8424a56397d8' # str | Lifecycle State ID
    json_patch_operation = [{op=replace, path=/description, value=Updated description!}, {op=replace, path=/accessProfileIds, value=[2c918087742bab150174407a80f3125e, 2c918087742bab150174407a80f3124f]}, {op=replace, path=/accountActions, value=[{action=ENABLE, sourceIds=[2c9180846a2f82fb016a481c1b1560c5, 2c9180846a2f82fb016a481c1b1560cc]}, {action=DISABLE, sourceIds=[2c91808869a0c9980169a207258513fb]}]}, {op=replace, path=/emailNotificationOption, value={notifyManagers=true, notifyAllAdmins=false, notifySpecificUsers=false, emailAddressList=[]}}] # List[JsonPatchOperation] | A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption 

    try:
        # Update Lifecycle State
        api_response = api_instance.update_lifecycle_states(identity_profile_id, lifecycle_state_id, json_patch_operation)
        print("The response of LifecycleStatesApi->update_lifecycle_states:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LifecycleStatesApi->update_lifecycle_states: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_profile_id** | **str**| Identity Profile ID | 
 **lifecycle_state_id** | **str**| Lifecycle State ID | 
 **json_patch_operation** | [**List[JsonPatchOperation]**](JsonPatchOperation.md)| A list of lifecycle state update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields can be updated: * enabled * description * accountActions * accessProfileIds * emailNotificationOption  | 

### Return type

[**LifecycleState**](LifecycleState.md)

### Authorization

[UserContextAuth](../README.md#UserContextAuth), [UserContextAuth](../README.md#UserContextAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LifecycleState was successfully updated. |  -  |
**400** | Client Error - Returned if the request body is invalid. |  -  |
**401** | Unauthorized - Returned if there is no authorization header, or if the JWT token is expired. |  -  |
**403** | Forbidden - Returned if the user you are running as, doesn&#39;t have access to this end-point. |  -  |
**404** | Not Found - returned if the request URL refers to a resource or object that does not exist |  -  |
**429** | Too Many Requests - Returned in response to too many requests in a given period of time - rate limited. The Retry-After header in the response includes how long to wait before trying again. |  -  |
**500** | Internal Server Error - Returned if there is an unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

