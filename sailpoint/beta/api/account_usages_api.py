# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictStr

from typing import List, Optional

from sailpoint.beta.models.account_usage import AccountUsage

from sailpoint.beta.api_client import ApiClient
from sailpoint.beta.api_response import ApiResponse
from sailpoint.beta.rest import RESTResponseType


class AccountUsagesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_usages_by_account_id(
        self,
        account_id: Annotated[StrictStr,
                              Field(description="ID of IDN account")],
        limit: Annotated[
            Optional[Annotated[int, Field(le=250, strict=True, ge=0)]],
            Field(
                description=
                "Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        offset: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=0)]],
            Field(
                description=
                "Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        count: Annotated[
            Optional[StrictBool],
            Field(
                description=
                "If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        sorters: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**"
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[AccountUsage]:
        """Returns account usage insights

        This API returns a summary of account usage insights for past 12 months.

        :param account_id: ID of IDN account (required)
        :type account_id: str
        :param limit: Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type limit: int
        :param offset: Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type offset: int
        :param count: If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type count: bool
        :param sorters: Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**
        :type sorters: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usages_by_account_id_serialize(
            account_id=account_id,
            limit=limit,
            offset=offset,
            count=count,
            sorters=sorters,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AccountUsage]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_usages_by_account_id_with_http_info(
        self,
        account_id: Annotated[StrictStr,
                              Field(description="ID of IDN account")],
        limit: Annotated[
            Optional[Annotated[int, Field(le=250, strict=True, ge=0)]],
            Field(
                description=
                "Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        offset: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=0)]],
            Field(
                description=
                "Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        count: Annotated[
            Optional[StrictBool],
            Field(
                description=
                "If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        sorters: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**"
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[AccountUsage]]:
        """Returns account usage insights

        This API returns a summary of account usage insights for past 12 months.

        :param account_id: ID of IDN account (required)
        :type account_id: str
        :param limit: Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type limit: int
        :param offset: Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type offset: int
        :param count: If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type count: bool
        :param sorters: Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**
        :type sorters: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usages_by_account_id_serialize(
            account_id=account_id,
            limit=limit,
            offset=offset,
            count=count,
            sorters=sorters,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AccountUsage]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_usages_by_account_id_without_preload_content(
        self,
        account_id: Annotated[StrictStr,
                              Field(description="ID of IDN account")],
        limit: Annotated[
            Optional[Annotated[int, Field(le=250, strict=True, ge=0)]],
            Field(
                description=
                "Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        offset: Annotated[
            Optional[Annotated[int, Field(strict=True, ge=0)]],
            Field(
                description=
                "Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        count: Annotated[
            Optional[StrictBool],
            Field(
                description=
                "If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information."
            )] = None,
        sorters: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**"
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Returns account usage insights

        This API returns a summary of account usage insights for past 12 months.

        :param account_id: ID of IDN account (required)
        :type account_id: str
        :param limit: Max number of results to return. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type limit: int
        :param offset: Offset into the full result set. Usually specified with *limit* to paginate through the results. See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type offset: int
        :param count: If *true* it will populate the *X-Total-Count* response header with the number of results that would be returned if *limit* and *offset* were ignored.  Since requesting a total count can have a performance impact, it is recommended not to send **count=true** if that value will not be used.  See [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters) for more information.
        :type count: bool
        :param sorters: Sort results using the standard syntax described in [V3 API Standard Collection Parameters](https://developer.sailpoint.com/idn/api/standard-collection-parameters#sorting-results)  Sorting is supported for the following fields: **date**
        :type sorters: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_usages_by_account_id_serialize(
            account_id=account_id,
            limit=limit,
            offset=offset,
            count=count,
            sorters=sorters,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AccountUsage]",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_usages_by_account_id_serialize(
        self,
        account_id,
        limit,
        offset,
        count,
        sorters,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if account_id is not None:
            _path_params['accountId'] = account_id
        # process the query parameters
        if limit is not None:

            _query_params.append(('limit', limit))

        if offset is not None:

            _query_params.append(('offset', offset))

        if count is not None:

            _query_params.append(('count', count))

        if sorters is not None:

            _query_params.append(('sorters', sorters))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['UserContextAuth', 'UserContextAuth']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/account-usages/{accountId}/summaries',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth)
