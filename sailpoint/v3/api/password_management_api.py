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
from pydantic import Field, StrictStr

from sailpoint.v3.models.password_change_request import PasswordChangeRequest
from sailpoint.v3.models.password_change_response import PasswordChangeResponse
from sailpoint.v3.models.password_info import PasswordInfo
from sailpoint.v3.models.password_info_query_dto import PasswordInfoQueryDTO
from sailpoint.v3.models.password_status import PasswordStatus

from sailpoint.v3.api_client import ApiClient
from sailpoint.v3.api_response import ApiResponse
from sailpoint.v3.exceptions import (  # noqa: F401
    ApiTypeError, ApiValueError)


class PasswordManagementApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_password_change_status(self, id: Annotated[
        StrictStr,
        Field(..., description="Password change request ID")],
                                   **kwargs) -> PasswordStatus:  # noqa: E501
        """Get Password Change Request Status  # noqa: E501

        This API returns the status of a password change request. A token with identity owner or trusted API client application authority is required to call this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_password_change_status(id, async_req=True)
        >>> result = thread.get()

        :param id: Password change request ID (required)
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
        :rtype: PasswordStatus
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_password_change_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_password_change_status_with_http_info(
            id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_password_change_status_with_http_info(
            self, id: Annotated[
                StrictStr,
                Field(..., description="Password change request ID")],
            **kwargs) -> ApiResponse:  # noqa: E501
        """Get Password Change Request Status  # noqa: E501

        This API returns the status of a password change request. A token with identity owner or trusted API client application authority is required to call this API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_password_change_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: Password change request ID (required)
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
        :rtype: tuple(PasswordStatus, status_code(int), headers(HTTPHeaderDict))
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
                                   " to method get_password_change_status" %
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

        _response_types_map = {
            '200': "PasswordStatus",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '404': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/password-change-status/{id}',
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
    def query_password_info(self,
                            password_info_query_dto: PasswordInfoQueryDTO,
                            **kwargs) -> PasswordInfo:  # noqa: E501
        """Query Password Info  # noqa: E501

        This API is used to query password related information.   A token with [API authority](https://developer.sailpoint.com/idn/api/authentication#client-credentials-grant-flow)  is required to call this API.  \"API authority\" refers to a token that only has the \"client_credentials\"  grant type, and therefore no user context. A [personal access token](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens)  or a token generated with the [authorization_code](https://developer.sailpoint.com/idn/api/authentication#authorization-code-grant-flow)  grant type will **NOT** work on this endpoint, and a `403 Forbidden` response  will be returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_password_info(password_info_query_dto, async_req=True)
        >>> result = thread.get()

        :param password_info_query_dto: (required)
        :type password_info_query_dto: PasswordInfoQueryDTO
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PasswordInfo
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the query_password_info_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.query_password_info_with_http_info(password_info_query_dto,
                                                       **kwargs)  # noqa: E501

    @validate_arguments
    def query_password_info_with_http_info(
            self, password_info_query_dto: PasswordInfoQueryDTO,
            **kwargs) -> ApiResponse:  # noqa: E501
        """Query Password Info  # noqa: E501

        This API is used to query password related information.   A token with [API authority](https://developer.sailpoint.com/idn/api/authentication#client-credentials-grant-flow)  is required to call this API.  \"API authority\" refers to a token that only has the \"client_credentials\"  grant type, and therefore no user context. A [personal access token](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens)  or a token generated with the [authorization_code](https://developer.sailpoint.com/idn/api/authentication#authorization-code-grant-flow)  grant type will **NOT** work on this endpoint, and a `403 Forbidden` response  will be returned.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_password_info_with_http_info(password_info_query_dto, async_req=True)
        >>> result = thread.get()

        :param password_info_query_dto: (required)
        :type password_info_query_dto: PasswordInfoQueryDTO
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
        :rtype: tuple(PasswordInfo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['password_info_query_dto']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method query_password_info" % _key)
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
        if _params['password_info_query_dto'] is not None:
            _body_params = _params['password_info_query_dto']

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
            '200': "PasswordInfo",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/query-password-info',
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
    def set_password(self, password_change_request: PasswordChangeRequest,
                     **kwargs) -> PasswordChangeResponse:  # noqa: E501
        """Set Identity's Password  # noqa: E501

        This API is used to set a password for an identity.   An identity can change their own password (as well as any of their accounts' passwords) if they use a token generated by their IDN user, such as a [personal access token](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens) or [\"authorization_code\" derived OAuth token](https://developer.sailpoint.com/idn/api/authentication#authorization-code-grant-flow).  A token with [API authority](https://developer.sailpoint.com/idn/api/authentication#client-credentials-grant-flow) can be used to change **any** identity's password or the password of any of the identity's accounts.  \"API authority\" refers to a token that only has the \"client_credentials\" grant type.  You can use this endpoint to generate an `encryptedPassword` (RSA encrypted using publicKey).  To do so, follow these steps:  1. Use [Query Password Info](https://developer.sailpoint.com/idn/api/v3/query-password-info) to get the following information: `identityId`, `sourceId`, `publicKeyId`, `publicKey`, `accounts`, and `policies`.   2. Choose an account from the previous response that you will provide as an `accountId` in your request to set an encrypted password.   3. Use [Set Identity's Password](https://developer.sailpoint.com/idn/api/v3/set-password) and provide the information you got from your earlier query. Then add this code to your request to get the encrypted password:  ```java import javax.crypto.Cipher; import java.security.KeyFactory; import java.security.PublicKey; import java.security.spec.X509EncodedKeySpec; import java util.Base64;  String encrypt(String publicKey, String toEncrypt) throws Exception {   byte[] publicKeyBytes = Base64.getDecoder().decode(publicKey);   byte[] encryptedBytes = encryptRsa(publicKeyBytes, toEncrypt.getBytes(\"UTF-8\"));   return Base64.getEncoder().encodeToString(encryptedBytes); }  private byte[] encryptRsa(byte[] publicKeyBytes, byte[] toEncryptBytes) throws Exception {   PublicKey key = KeyFactory.getInstance(\"RSA\").generatePublic(new X509EncodedKeySpec(publicKeyBytes));   String transformation = \"RSA/ECB/PKCS1Padding\";   Cipher cipher = Cipher.getInstance(transformation);   cipher.init(1, key);   return cipher.doFinal(toEncryptBytes); } ```      In this example, `toEncrypt` refers to the plain text password you are setting and then encrypting, and the `publicKey` refers to the publicKey you got from the first request you sent.   You can then use [Get Password Change Request Status](https://developer.sailpoint.com/idn/api/v3/get-password-change-status) to check the password change request status. To do so, you must provide the `requestId` from your earlier request to set the password.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_password(password_change_request, async_req=True)
        >>> result = thread.get()

        :param password_change_request: (required)
        :type password_change_request: PasswordChangeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PasswordChangeResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the set_password_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.set_password_with_http_info(password_change_request,
                                                **kwargs)  # noqa: E501

    @validate_arguments
    def set_password_with_http_info(
            self, password_change_request: PasswordChangeRequest,
            **kwargs) -> ApiResponse:  # noqa: E501
        """Set Identity's Password  # noqa: E501

        This API is used to set a password for an identity.   An identity can change their own password (as well as any of their accounts' passwords) if they use a token generated by their IDN user, such as a [personal access token](https://developer.sailpoint.com/idn/api/authentication#personal-access-tokens) or [\"authorization_code\" derived OAuth token](https://developer.sailpoint.com/idn/api/authentication#authorization-code-grant-flow).  A token with [API authority](https://developer.sailpoint.com/idn/api/authentication#client-credentials-grant-flow) can be used to change **any** identity's password or the password of any of the identity's accounts.  \"API authority\" refers to a token that only has the \"client_credentials\" grant type.  You can use this endpoint to generate an `encryptedPassword` (RSA encrypted using publicKey).  To do so, follow these steps:  1. Use [Query Password Info](https://developer.sailpoint.com/idn/api/v3/query-password-info) to get the following information: `identityId`, `sourceId`, `publicKeyId`, `publicKey`, `accounts`, and `policies`.   2. Choose an account from the previous response that you will provide as an `accountId` in your request to set an encrypted password.   3. Use [Set Identity's Password](https://developer.sailpoint.com/idn/api/v3/set-password) and provide the information you got from your earlier query. Then add this code to your request to get the encrypted password:  ```java import javax.crypto.Cipher; import java.security.KeyFactory; import java.security.PublicKey; import java.security.spec.X509EncodedKeySpec; import java util.Base64;  String encrypt(String publicKey, String toEncrypt) throws Exception {   byte[] publicKeyBytes = Base64.getDecoder().decode(publicKey);   byte[] encryptedBytes = encryptRsa(publicKeyBytes, toEncrypt.getBytes(\"UTF-8\"));   return Base64.getEncoder().encodeToString(encryptedBytes); }  private byte[] encryptRsa(byte[] publicKeyBytes, byte[] toEncryptBytes) throws Exception {   PublicKey key = KeyFactory.getInstance(\"RSA\").generatePublic(new X509EncodedKeySpec(publicKeyBytes));   String transformation = \"RSA/ECB/PKCS1Padding\";   Cipher cipher = Cipher.getInstance(transformation);   cipher.init(1, key);   return cipher.doFinal(toEncryptBytes); } ```      In this example, `toEncrypt` refers to the plain text password you are setting and then encrypting, and the `publicKey` refers to the publicKey you got from the first request you sent.   You can then use [Get Password Change Request Status](https://developer.sailpoint.com/idn/api/v3/get-password-change-status) to check the password change request status. To do so, you must provide the `requestId` from your earlier request to set the password.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_password_with_http_info(password_change_request, async_req=True)
        >>> result = thread.get()

        :param password_change_request: (required)
        :type password_change_request: PasswordChangeRequest
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
        :rtype: tuple(PasswordChangeResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['password_change_request']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method set_password" % _key)
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
        if _params['password_change_request'] is not None:
            _body_params = _params['password_change_request']

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
            '202': "PasswordChangeResponse",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/set-password',
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
