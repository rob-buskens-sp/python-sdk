# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from beta.models.account_aggregation_status import AccountAggregationStatus

from beta.api_client import ApiClient
from beta.api_response import ApiResponse
from beta.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AccountAggregationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_account_aggregation_status(self, id : Annotated[StrictStr, Field(..., description="The account aggregation id")], **kwargs) -> AccountAggregationStatus:  # noqa: E501
        """In-progress Account Aggregation status  # noqa: E501

        This API returns the status of an *in-progress* account aggregation, along with the total number of **NEW**, **CHANGED** and **DELETED** accounts found since the previous aggregation, and the number of those accounts that have been processed so far.  Accounts that have not changed since the previous aggregation are not included in **totalAccounts** and **processedAccounts** counts returned by this API. This is distinct from **Accounts Scanned** shown in the Aggregation UI, which indicates total accounts scanned regardless of whether they changed or not.  Since this endpoint reports on the status of an *in-progress* account aggregation, totalAccounts and processedAccounts may change between calls to this endpoint.  *Only available up to an hour after the aggregation completes. May respond with *404 Not Found* after that.*  A token with ORG_ADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN or DASHBOARD authority is required to call this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_aggregation_status(id, async_req=True)
        >>> result = thread.get()

        :param id: The account aggregation id (required)
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
        :rtype: AccountAggregationStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_account_aggregation_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_account_aggregation_status_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_account_aggregation_status_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The account aggregation id")], **kwargs) -> ApiResponse:  # noqa: E501
        """In-progress Account Aggregation status  # noqa: E501

        This API returns the status of an *in-progress* account aggregation, along with the total number of **NEW**, **CHANGED** and **DELETED** accounts found since the previous aggregation, and the number of those accounts that have been processed so far.  Accounts that have not changed since the previous aggregation are not included in **totalAccounts** and **processedAccounts** counts returned by this API. This is distinct from **Accounts Scanned** shown in the Aggregation UI, which indicates total accounts scanned regardless of whether they changed or not.  Since this endpoint reports on the status of an *in-progress* account aggregation, totalAccounts and processedAccounts may change between calls to this endpoint.  *Only available up to an hour after the aggregation completes. May respond with *404 Not Found* after that.*  A token with ORG_ADMIN, SOURCE_ADMIN, SOURCE_SUBADMIN or DASHBOARD authority is required to call this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_aggregation_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The account aggregation id (required)
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
        :rtype: tuple(AccountAggregationStatus, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method get_account_aggregation_status" % _key
                )
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

        _response_types_map = {
            '200': "AccountAggregationStatus",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '404': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/account-aggregations/{id}/status', 'GET',
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
