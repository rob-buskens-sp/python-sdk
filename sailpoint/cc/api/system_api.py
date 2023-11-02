# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import StrictStr

from typing import Any, Dict, Optional

from cc.models.refresh_identities_request import RefreshIdentitiesRequest

from cc.api_client import ApiClient
from cc.api_response import ApiResponse
from cc.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SystemApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def refresh_identities(self, content_type : Optional[StrictStr] = None, refresh_identities_request : Optional[RefreshIdentitiesRequest] = None, **kwargs) -> Dict[str, object]:  # noqa: E501
        """Refresh Identities  # noqa: E501

        This kicks off an identity refresh for a specified set of identity attributes.  This can be a long running process.  IdentityNow has pre-scheduled versions of this task at set intervals and events already, so only run this when directed by SailPoint.  _Note: If the identities specified by the filter do not exist, a full identity refresh will be run.  Use with caution._  Refresh Arguments:  | Key                   | Description                                        | |-----------------------|----------------------------------------------------| | correlateEntitlements | Analyzes entitlements, access profiles, and roles. | | promoteAttributes     | Calculates identity attributes.                    | | refreshManagerStatus  | Calculates manager correlation and manager status. | | synchronizeAttributes | Performs attribute sync provisioning.              | | pruneIdentities       | Removes any identities which don't have accounts.  | | provision             | Provisions any assigned roles or access profiles.  |  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.refresh_identities(content_type, refresh_identities_request, async_req=True)
        >>> result = thread.get()

        :param content_type:
        :type content_type: str
        :param refresh_identities_request:
        :type refresh_identities_request: RefreshIdentitiesRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Dict[str, object]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the refresh_identities_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.refresh_identities_with_http_info(content_type, refresh_identities_request, **kwargs)  # noqa: E501

    @validate_arguments
    def refresh_identities_with_http_info(self, content_type : Optional[StrictStr] = None, refresh_identities_request : Optional[RefreshIdentitiesRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Refresh Identities  # noqa: E501

        This kicks off an identity refresh for a specified set of identity attributes.  This can be a long running process.  IdentityNow has pre-scheduled versions of this task at set intervals and events already, so only run this when directed by SailPoint.  _Note: If the identities specified by the filter do not exist, a full identity refresh will be run.  Use with caution._  Refresh Arguments:  | Key                   | Description                                        | |-----------------------|----------------------------------------------------| | correlateEntitlements | Analyzes entitlements, access profiles, and roles. | | promoteAttributes     | Calculates identity attributes.                    | | refreshManagerStatus  | Calculates manager correlation and manager status. | | synchronizeAttributes | Performs attribute sync provisioning.              | | pruneIdentities       | Removes any identities which don't have accounts.  | | provision             | Provisions any assigned roles or access profiles.  |  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.refresh_identities_with_http_info(content_type, refresh_identities_request, async_req=True)
        >>> result = thread.get()

        :param content_type:
        :type content_type: str
        :param refresh_identities_request:
        :type refresh_identities_request: RefreshIdentitiesRequest
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
        :rtype: tuple(Dict[str, object], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'content_type',
            'refresh_identities_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_identities" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['refresh_identities_request'] is not None:
            _body_params = _params['refresh_identities_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "Dict[str, object]",
        }

        return self.api_client.call_api(
            '/cc/api/system/refreshIdentities', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
