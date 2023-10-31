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
from pydantic import Field, StrictBool, StrictStr, conint

from typing import List, Optional

from v3.models.campaign_filter_details import CampaignFilterDetails

from v3.api_client import ApiClient
from v3.api_response import ApiResponse
from v3.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CertificationCampaignFiltersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_campaign_filter(self, campaign_filter_details : CampaignFilterDetails, **kwargs) -> CampaignFilterDetails:  # noqa: E501
        """Create a Campaign Filter  # noqa: E501

        Create a campaign Filter based on filter details and criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_campaign_filter(campaign_filter_details, async_req=True)
        >>> result = thread.get()

        :param campaign_filter_details: (required)
        :type campaign_filter_details: CampaignFilterDetails
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CampaignFilterDetails
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_campaign_filter_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_campaign_filter_with_http_info(campaign_filter_details, **kwargs)  # noqa: E501

    @validate_arguments
    def create_campaign_filter_with_http_info(self, campaign_filter_details : CampaignFilterDetails, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a Campaign Filter  # noqa: E501

        Create a campaign Filter based on filter details and criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_campaign_filter_with_http_info(campaign_filter_details, async_req=True)
        >>> result = thread.get()

        :param campaign_filter_details: (required)
        :type campaign_filter_details: CampaignFilterDetails
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
        :rtype: tuple(CampaignFilterDetails, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'campaign_filter_details'
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
                    " to method create_campaign_filter" % _key
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
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['campaign_filter_details'] is not None:
            _body_params = _params['campaign_filter_details']

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
            '200': "CampaignFilterDetails",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/campaign-filters', 'POST',
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

    @validate_arguments
    def get_campaign_filter_by_id(self, filter_id : Annotated[StrictStr, Field(..., description="The ID of the campaign filter to be retrieved.")], **kwargs) -> List[CampaignFilterDetails]:  # noqa: E501
        """Get Campaign Filter by ID  # noqa: E501

        Retrieves information for an existing campaign filter using the filter's ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_campaign_filter_by_id(filter_id, async_req=True)
        >>> result = thread.get()

        :param filter_id: The ID of the campaign filter to be retrieved. (required)
        :type filter_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[CampaignFilterDetails]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_campaign_filter_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_campaign_filter_by_id_with_http_info(filter_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_campaign_filter_by_id_with_http_info(self, filter_id : Annotated[StrictStr, Field(..., description="The ID of the campaign filter to be retrieved.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Campaign Filter by ID  # noqa: E501

        Retrieves information for an existing campaign filter using the filter's ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_campaign_filter_by_id_with_http_info(filter_id, async_req=True)
        >>> result = thread.get()

        :param filter_id: The ID of the campaign filter to be retrieved. (required)
        :type filter_id: str
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
        :rtype: tuple(List[CampaignFilterDetails], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter_id'
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
                    " to method get_campaign_filter_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['filter_id']:
            _path_params['filterId'] = _params['filter_id']


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
            '200': "List[CampaignFilterDetails]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '404': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/campaign-filters/{id}', 'GET',
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

    @validate_arguments
    def list_campaign_filters(self, limit : Annotated[Optional[conint(strict=True, le=250, ge=0)], Field(description="Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.")] = None, include_system_filters : Annotated[Optional[StrictBool], Field(description="If true, include system filters in the count and results, exclude them otherwise. If not provided any value for it then by default it is true.")] = None, **kwargs) -> List[CampaignFilterDetails]:  # noqa: E501
        """List Campaign Filters  # noqa: E501

        Lists all Campaign Filters. Scope can be reduced via standard V3 query params.  All Campaign Filters matching the query params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_campaign_filters(limit, start, include_system_filters, async_req=True)
        >>> result = thread.get()

        :param limit: Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type limit: int
        :param start: Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type start: int
        :param include_system_filters: If true, include system filters in the count and results, exclude them otherwise. If not provided any value for it then by default it is true.
        :type include_system_filters: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[CampaignFilterDetails]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_campaign_filters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_campaign_filters_with_http_info(limit, start, include_system_filters, **kwargs)  # noqa: E501

    @validate_arguments
    def list_campaign_filters_with_http_info(self, limit : Annotated[Optional[conint(strict=True, le=250, ge=0)], Field(description="Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.")] = None, include_system_filters : Annotated[Optional[StrictBool], Field(description="If true, include system filters in the count and results, exclude them otherwise. If not provided any value for it then by default it is true.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Campaign Filters  # noqa: E501

        Lists all Campaign Filters. Scope can be reduced via standard V3 query params.  All Campaign Filters matching the query params  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_campaign_filters_with_http_info(limit, start, include_system_filters, async_req=True)
        >>> result = thread.get()

        :param limit: Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type limit: int
        :param start: Start/Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type start: int
        :param include_system_filters: If true, include system filters in the count and results, exclude them otherwise. If not provided any value for it then by default it is true.
        :type include_system_filters: bool
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
        :rtype: tuple(List[CampaignFilterDetails], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'start',
            'include_system_filters'
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
                    " to method list_campaign_filters" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('include_system_filters') is not None:  # noqa: E501
            _query_params.append(('includeSystemFilters', _params['include_system_filters']))

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
            '200': "List[CampaignFilterDetails]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/campaign-filters', 'GET',
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

    @validate_arguments
    def update_campaign_filter(self, filter_id : Annotated[StrictStr, Field(..., description="The ID of the campaign filter being modified.")], campaign_filter_details : Annotated[CampaignFilterDetails, Field(..., description="A campaign filter details with updated field values.")], **kwargs) -> CampaignFilterDetails:  # noqa: E501
        """Updates a Campaign Filter  # noqa: E501

        Updates an existing campaign filter using the filter's ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_campaign_filter(filter_id, campaign_filter_details, async_req=True)
        >>> result = thread.get()

        :param filter_id: The ID of the campaign filter being modified. (required)
        :type filter_id: str
        :param campaign_filter_details: A campaign filter details with updated field values. (required)
        :type campaign_filter_details: CampaignFilterDetails
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CampaignFilterDetails
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the update_campaign_filter_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.update_campaign_filter_with_http_info(filter_id, campaign_filter_details, **kwargs)  # noqa: E501

    @validate_arguments
    def update_campaign_filter_with_http_info(self, filter_id : Annotated[StrictStr, Field(..., description="The ID of the campaign filter being modified.")], campaign_filter_details : Annotated[CampaignFilterDetails, Field(..., description="A campaign filter details with updated field values.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Updates a Campaign Filter  # noqa: E501

        Updates an existing campaign filter using the filter's ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_campaign_filter_with_http_info(filter_id, campaign_filter_details, async_req=True)
        >>> result = thread.get()

        :param filter_id: The ID of the campaign filter being modified. (required)
        :type filter_id: str
        :param campaign_filter_details: A campaign filter details with updated field values. (required)
        :type campaign_filter_details: CampaignFilterDetails
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
        :rtype: tuple(CampaignFilterDetails, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter_id',
            'campaign_filter_details'
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
                    " to method update_campaign_filter" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['filter_id']:
            _path_params['filterId'] = _params['filter_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['campaign_filter_details'] is not None:
            _body_params = _params['campaign_filter_details']

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
            '200': "CampaignFilterDetails",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/campaign-filters/{id}', 'POST',
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
