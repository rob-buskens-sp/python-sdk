# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

from typing import List, Optional

from sailpoint.v3.models.create_personal_access_token_request import CreatePersonalAccessTokenRequest
from sailpoint.v3.models.create_personal_access_token_response import CreatePersonalAccessTokenResponse
from sailpoint.v3.models.get_personal_access_token_response import GetPersonalAccessTokenResponse
from sailpoint.v3.models.json_patch_operation import JsonPatchOperation

from sailpoint.v3.api_client import ApiClient
from sailpoint.v3.api_response import ApiResponse
from sailpoint.v3.exceptions import (  # noqa: F401
    ApiTypeError, ApiValueError)


class PersonalAccessTokensApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_personal_access_token(
            self, create_personal_access_token_request: Annotated[
                CreatePersonalAccessTokenRequest,
                Field(...,
                      description="Name and scope of personal access token.")],
            **kwargs) -> CreatePersonalAccessTokenResponse:  # noqa: E501
        """Create Personal Access Token  # noqa: E501

        This creates a personal access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_personal_access_token(create_personal_access_token_request, async_req=True)
        >>> result = thread.get()

        :param create_personal_access_token_request: Name and scope of personal access token. (required)
        :type create_personal_access_token_request: CreatePersonalAccessTokenRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreatePersonalAccessTokenResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_personal_access_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_personal_access_token_with_http_info(
            create_personal_access_token_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_personal_access_token_with_http_info(
            self, create_personal_access_token_request: Annotated[
                CreatePersonalAccessTokenRequest,
                Field(...,
                      description="Name and scope of personal access token.")],
            **kwargs) -> ApiResponse:  # noqa: E501
        """Create Personal Access Token  # noqa: E501

        This creates a personal access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_personal_access_token_with_http_info(create_personal_access_token_request, async_req=True)
        >>> result = thread.get()

        :param create_personal_access_token_request: Name and scope of personal access token. (required)
        :type create_personal_access_token_request: CreatePersonalAccessTokenRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreatePersonalAccessTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['create_personal_access_token_request']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method create_personal_access_token" %
                                   _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_personal_access_token_request'] is not None:
            _body_params = _params['create_personal_access_token_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            '_content_type',
            self.api_client.select_header_content_type(['application/json']))
        if _content_types_list:
            _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "CreatePersonalAccessTokenResponse",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/personal-access-tokens',
            'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_personal_access_token(self, id: Annotated[
        StrictStr,
        Field(..., description="The personal access token id")],
                                     **kwargs) -> None:  # noqa: E501
        """Delete Personal Access Token  # noqa: E501

        This deletes a personal access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_personal_access_token(id, async_req=True)
        >>> result = thread.get()

        :param id: The personal access token id (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_personal_access_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_personal_access_token_with_http_info(
            id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_personal_access_token_with_http_info(
            self, id: Annotated[
                StrictStr,
                Field(..., description="The personal access token id")],
            **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Personal Access Token  # noqa: E501

        This deletes a personal access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_personal_access_token_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The personal access token id (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ['id']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method delete_personal_access_token" %
                                   _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/personal-access-tokens/{id}',
            'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_personal_access_tokens(
            self,
            owner_id:
        Annotated[
            Optional[StrictStr],
            Field(
                description=
                "The identity ID of the owner whose personal access tokens should be listed.  If \"me\", the caller should have the following right: 'idn:my-personal-access-tokens:read' If an actual owner ID or if the `owner-id` parameter is omitted in the request,  the caller should have the following right: 'idn:all-personal-access-tokens:read'.  If the caller has the following right, then managed personal access tokens associated with `owner-id`  will be retrieved: 'idn:managed-personal-access-tokens:read'"
            )] = None,
            filters:
        Annotated[
            Optional[StrictStr],
            Field(
                description=
                "Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull*"
            )] = None,
            **kwargs) -> List[GetPersonalAccessTokenResponse]:  # noqa: E501
        """List Personal Access Tokens  # noqa: E501

        This gets a collection of personal access tokens associated with the optional `owner-id`.  query parameter. If the `owner-id` query parameter is omitted, all personal access tokens  for a tenant will be retrieved, but the caller must have the 'idn:all-personal-access-tokens:read' right.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_personal_access_tokens(owner_id, filters, async_req=True)
        >>> result = thread.get()

        :param owner_id: The identity ID of the owner whose personal access tokens should be listed.  If \"me\", the caller should have the following right: 'idn:my-personal-access-tokens:read' If an actual owner ID or if the `owner-id` parameter is omitted in the request,  the caller should have the following right: 'idn:all-personal-access-tokens:read'.  If the caller has the following right, then managed personal access tokens associated with `owner-id`  will be retrieved: 'idn:managed-personal-access-tokens:read'
        :type owner_id: str
        :param filters: Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull*
        :type filters: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[GetPersonalAccessTokenResponse]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_personal_access_tokens_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_personal_access_tokens_with_http_info(
            owner_id, filters, **kwargs)  # noqa: E501

    @validate_arguments
    def list_personal_access_tokens_with_http_info(
            self,
            owner_id:
        Annotated[
            Optional[StrictStr],
            Field(
                description=
                "The identity ID of the owner whose personal access tokens should be listed.  If \"me\", the caller should have the following right: 'idn:my-personal-access-tokens:read' If an actual owner ID or if the `owner-id` parameter is omitted in the request,  the caller should have the following right: 'idn:all-personal-access-tokens:read'.  If the caller has the following right, then managed personal access tokens associated with `owner-id`  will be retrieved: 'idn:managed-personal-access-tokens:read'"
            )] = None,
            filters:
        Annotated[
            Optional[StrictStr],
            Field(
                description=
                "Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull*"
            )] = None,
            **kwargs) -> ApiResponse:  # noqa: E501
        """List Personal Access Tokens  # noqa: E501

        This gets a collection of personal access tokens associated with the optional `owner-id`.  query parameter. If the `owner-id` query parameter is omitted, all personal access tokens  for a tenant will be retrieved, but the caller must have the 'idn:all-personal-access-tokens:read' right.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_personal_access_tokens_with_http_info(owner_id, filters, async_req=True)
        >>> result = thread.get()

        :param owner_id: The identity ID of the owner whose personal access tokens should be listed.  If \"me\", the caller should have the following right: 'idn:my-personal-access-tokens:read' If an actual owner ID or if the `owner-id` parameter is omitted in the request,  the caller should have the following right: 'idn:all-personal-access-tokens:read'.  If the caller has the following right, then managed personal access tokens associated with `owner-id`  will be retrieved: 'idn:managed-personal-access-tokens:read'
        :type owner_id: str
        :param filters: Filter results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#filtering-results)  Filtering is supported for the following fields and operators:  **lastUsed**: *le, isnull*
        :type filters: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[GetPersonalAccessTokenResponse], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['owner_id', 'filters']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method list_personal_access_tokens" %
                                   _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('owner_id') is not None:  # noqa: E501
            _query_params.append(('owner-id', _params['owner_id']))

        if _params.get('filters') is not None:  # noqa: E501
            _query_params.append(('filters', _params['filters']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "List[GetPersonalAccessTokenResponse]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/personal-access-tokens',
            'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def patch_personal_access_token(self, id: Annotated[
        StrictStr,
        Field(
            ..., description="The Personal Access Token id"
        )], json_patch_operation: Annotated[
            conlist(JsonPatchOperation),
            Field(
                ...,
                description=
                "A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope "
            )], **kwargs) -> GetPersonalAccessTokenResponse:  # noqa: E501
        """Patch Personal Access Token  # noqa: E501

        This performs a targeted update to the field(s) of a Personal Access Token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_personal_access_token(id, json_patch_operation, async_req=True)
        >>> result = thread.get()

        :param id: The Personal Access Token id (required)
        :type id: str
        :param json_patch_operation: A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope  (required)
        :type json_patch_operation: List[JsonPatchOperation]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetPersonalAccessTokenResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the patch_personal_access_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.patch_personal_access_token_with_http_info(
            id, json_patch_operation, **kwargs)  # noqa: E501

    @validate_arguments
    def patch_personal_access_token_with_http_info(self, id: Annotated[
        StrictStr,
        Field(
            ..., description="The Personal Access Token id"
        )], json_patch_operation: Annotated[
            conlist(JsonPatchOperation),
            Field(
                ...,
                description=
                "A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope "
            )], **kwargs) -> ApiResponse:  # noqa: E501
        """Patch Personal Access Token  # noqa: E501

        This performs a targeted update to the field(s) of a Personal Access Token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_personal_access_token_with_http_info(id, json_patch_operation, async_req=True)
        >>> result = thread.get()

        :param id: The Personal Access Token id (required)
        :type id: str
        :param json_patch_operation: A list of OAuth client update operations according to the [JSON Patch](https://tools.ietf.org/html/rfc6902) standard.  The following fields are patchable: * name * scope  (required)
        :type json_patch_operation: List[JsonPatchOperation]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetPersonalAccessTokenResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['id', 'json_patch_operation']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method patch_personal_access_token" %
                                   _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['json_patch_operation'] is not None:
            _body_params = _params['json_patch_operation']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            '_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json']))
        if _content_types_list:
            _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetPersonalAccessTokenResponse",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '404': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/personal-access-tokens/{id}',
            'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
