# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
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

from pydantic import StrictBool, StrictBytes, StrictStr

from typing import Any, Dict, Optional, Union

from sailpoint.cc.api_client import ApiClient
from sailpoint.cc.api_response import ApiResponse
from sailpoint.cc.rest import RESTResponseType


class SourcesAggregationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def load_accounts(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        disable_optimization: Optional[StrictBool] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> Dict[str, object]:
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param disable_optimization:
        :type disable_optimization: bool
        :param file:
        :type file: bytearray
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

        _param = self._load_accounts_serialize(
            id=id,
            content_type=content_type,
            disable_optimization=disable_optimization,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def load_accounts_with_http_info(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        disable_optimization: Optional[StrictBool] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> ApiResponse[Dict[str, object]]:
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param disable_optimization:
        :type disable_optimization: bool
        :param file:
        :type file: bytearray
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

        _param = self._load_accounts_serialize(
            id=id,
            content_type=content_type,
            disable_optimization=disable_optimization,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def load_accounts_without_preload_content(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        disable_optimization: Optional[StrictBool] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param disable_optimization:
        :type disable_optimization: bool
        :param file:
        :type file: bytearray
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

        _param = self._load_accounts_serialize(
            id=id,
            content_type=content_type,
            disable_optimization=disable_optimization,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        return response_data.response

    def _load_accounts_serialize(
        self,
        id,
        content_type,
        disable_optimization,
        file,
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if content_type is not None:
            _header_params['Content-Type'] = content_type
        # process the form parameters
        if disable_optimization is not None:
            _form_params.append(('disableOptimization', disable_optimization))
        if file is not None:
            _files['file'] = file
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    ['multipart/form-data']))
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ['UserContextAuth', 'UserContextAuth']

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/cc/api/source/loadAccounts/{id}',
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

    @validate_call
    def load_entitlements(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> Dict[str, object]:
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param file:
        :type file: bytearray
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

        _param = self._load_entitlements_serialize(id=id,
                                                   content_type=content_type,
                                                   file=file,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def load_entitlements_with_http_info(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
    ) -> ApiResponse[Dict[str, object]]:
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param file:
        :type file: bytearray
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

        _param = self._load_entitlements_serialize(id=id,
                                                   content_type=content_type,
                                                   file=file,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def load_entitlements_without_preload_content(
        self,
        id: StrictStr,
        content_type: Optional[StrictStr] = None,
        file: Optional[Union[StrictBytes, StrictStr]] = None,
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
        """Account Aggregation (File)

        Aggregates a delimited file for the given source.  This only works for file-based sources.

        :param id: (required)
        :type id: str
        :param content_type:
        :type content_type: str
        :param file:
        :type file: bytearray
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

        _param = self._load_entitlements_serialize(id=id,
                                                   content_type=content_type,
                                                   file=file,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Dict[str, object]"
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        return response_data.response

    def _load_entitlements_serialize(
        self,
        id,
        content_type,
        file,
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        if content_type is not None:
            _header_params['Content-Type'] = content_type
        # process the form parameters
        if file is not None:
            _files['file'] = file
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    ['multipart/form-data']))
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ['UserContextAuth', 'UserContextAuth']

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/cc/api/source/loadEntitlements/{id}',
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
