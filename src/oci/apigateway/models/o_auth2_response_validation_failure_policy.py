# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501

from .validation_failure_policy import ValidationFailurePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OAuth2ResponseValidationFailurePolicy(ValidationFailurePolicy):
    """
    Policy to specify OAuth2 flow configuration.
    """

    #: A constant which can be used with the response_type property of a OAuth2ResponseValidationFailurePolicy.
    #: This constant has a value of "CODE"
    RESPONSE_TYPE_CODE = "CODE"

    def __init__(self, **kwargs):
        """
        Initializes a new OAuth2ResponseValidationFailurePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.OAuth2ResponseValidationFailurePolicy.type` attribute
        of this class is ``OAUTH2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OAuth2ResponseValidationFailurePolicy.
            Allowed values for this property are: "MODIFY_RESPONSE", "OAUTH2", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param client_details:
            The value to assign to the client_details property of this OAuth2ResponseValidationFailurePolicy.
        :type client_details: oci.apigateway.models.ClientAppDetails

        :param source_uri_details:
            The value to assign to the source_uri_details property of this OAuth2ResponseValidationFailurePolicy.
        :type source_uri_details: oci.apigateway.models.SourceUriDetails

        :param scopes:
            The value to assign to the scopes property of this OAuth2ResponseValidationFailurePolicy.
        :type scopes: list[str]

        :param max_expiry_duration_in_hours:
            The value to assign to the max_expiry_duration_in_hours property of this OAuth2ResponseValidationFailurePolicy.
        :type max_expiry_duration_in_hours: int

        :param use_cookies_for_session:
            The value to assign to the use_cookies_for_session property of this OAuth2ResponseValidationFailurePolicy.
        :type use_cookies_for_session: bool

        :param use_cookies_for_intermediate_steps:
            The value to assign to the use_cookies_for_intermediate_steps property of this OAuth2ResponseValidationFailurePolicy.
        :type use_cookies_for_intermediate_steps: bool

        :param use_pkce:
            The value to assign to the use_pkce property of this OAuth2ResponseValidationFailurePolicy.
        :type use_pkce: bool

        :param response_type:
            The value to assign to the response_type property of this OAuth2ResponseValidationFailurePolicy.
            Allowed values for this property are: "CODE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type response_type: str

        :param fallback_redirect_path:
            The value to assign to the fallback_redirect_path property of this OAuth2ResponseValidationFailurePolicy.
        :type fallback_redirect_path: str

        :param logout_path:
            The value to assign to the logout_path property of this OAuth2ResponseValidationFailurePolicy.
        :type logout_path: str

        """
        self.swagger_types = {
            'type': 'str',
            'client_details': 'ClientAppDetails',
            'source_uri_details': 'SourceUriDetails',
            'scopes': 'list[str]',
            'max_expiry_duration_in_hours': 'int',
            'use_cookies_for_session': 'bool',
            'use_cookies_for_intermediate_steps': 'bool',
            'use_pkce': 'bool',
            'response_type': 'str',
            'fallback_redirect_path': 'str',
            'logout_path': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'client_details': 'clientDetails',
            'source_uri_details': 'sourceUriDetails',
            'scopes': 'scopes',
            'max_expiry_duration_in_hours': 'maxExpiryDurationInHours',
            'use_cookies_for_session': 'useCookiesForSession',
            'use_cookies_for_intermediate_steps': 'useCookiesForIntermediateSteps',
            'use_pkce': 'usePkce',
            'response_type': 'responseType',
            'fallback_redirect_path': 'fallbackRedirectPath',
            'logout_path': 'logoutPath'
        }
        self._type = None
        self._client_details = None
        self._source_uri_details = None
        self._scopes = None
        self._max_expiry_duration_in_hours = None
        self._use_cookies_for_session = None
        self._use_cookies_for_intermediate_steps = None
        self._use_pkce = None
        self._response_type = None
        self._fallback_redirect_path = None
        self._logout_path = None
        self._type = 'OAUTH2'

    @property
    def client_details(self):
        """
        **[Required]** Gets the client_details of this OAuth2ResponseValidationFailurePolicy.

        :return: The client_details of this OAuth2ResponseValidationFailurePolicy.
        :rtype: oci.apigateway.models.ClientAppDetails
        """
        return self._client_details

    @client_details.setter
    def client_details(self, client_details):
        """
        Sets the client_details of this OAuth2ResponseValidationFailurePolicy.

        :param client_details: The client_details of this OAuth2ResponseValidationFailurePolicy.
        :type: oci.apigateway.models.ClientAppDetails
        """
        self._client_details = client_details

    @property
    def source_uri_details(self):
        """
        **[Required]** Gets the source_uri_details of this OAuth2ResponseValidationFailurePolicy.

        :return: The source_uri_details of this OAuth2ResponseValidationFailurePolicy.
        :rtype: oci.apigateway.models.SourceUriDetails
        """
        return self._source_uri_details

    @source_uri_details.setter
    def source_uri_details(self, source_uri_details):
        """
        Sets the source_uri_details of this OAuth2ResponseValidationFailurePolicy.

        :param source_uri_details: The source_uri_details of this OAuth2ResponseValidationFailurePolicy.
        :type: oci.apigateway.models.SourceUriDetails
        """
        self._source_uri_details = source_uri_details

    @property
    def scopes(self):
        """
        **[Required]** Gets the scopes of this OAuth2ResponseValidationFailurePolicy.
        List of scopes.


        :return: The scopes of this OAuth2ResponseValidationFailurePolicy.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this OAuth2ResponseValidationFailurePolicy.
        List of scopes.


        :param scopes: The scopes of this OAuth2ResponseValidationFailurePolicy.
        :type: list[str]
        """
        self._scopes = scopes

    @property
    def max_expiry_duration_in_hours(self):
        """
        Gets the max_expiry_duration_in_hours of this OAuth2ResponseValidationFailurePolicy.
        The duration for which the OAuth2 success token should be cached before it is
        fetched again.


        :return: The max_expiry_duration_in_hours of this OAuth2ResponseValidationFailurePolicy.
        :rtype: int
        """
        return self._max_expiry_duration_in_hours

    @max_expiry_duration_in_hours.setter
    def max_expiry_duration_in_hours(self, max_expiry_duration_in_hours):
        """
        Sets the max_expiry_duration_in_hours of this OAuth2ResponseValidationFailurePolicy.
        The duration for which the OAuth2 success token should be cached before it is
        fetched again.


        :param max_expiry_duration_in_hours: The max_expiry_duration_in_hours of this OAuth2ResponseValidationFailurePolicy.
        :type: int
        """
        self._max_expiry_duration_in_hours = max_expiry_duration_in_hours

    @property
    def use_cookies_for_session(self):
        """
        Gets the use_cookies_for_session of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to use cookies for session maintenance.


        :return: The use_cookies_for_session of this OAuth2ResponseValidationFailurePolicy.
        :rtype: bool
        """
        return self._use_cookies_for_session

    @use_cookies_for_session.setter
    def use_cookies_for_session(self, use_cookies_for_session):
        """
        Sets the use_cookies_for_session of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to use cookies for session maintenance.


        :param use_cookies_for_session: The use_cookies_for_session of this OAuth2ResponseValidationFailurePolicy.
        :type: bool
        """
        self._use_cookies_for_session = use_cookies_for_session

    @property
    def use_cookies_for_intermediate_steps(self):
        """
        Gets the use_cookies_for_intermediate_steps of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to use cookies for OAuth2 intermediate steps.


        :return: The use_cookies_for_intermediate_steps of this OAuth2ResponseValidationFailurePolicy.
        :rtype: bool
        """
        return self._use_cookies_for_intermediate_steps

    @use_cookies_for_intermediate_steps.setter
    def use_cookies_for_intermediate_steps(self, use_cookies_for_intermediate_steps):
        """
        Sets the use_cookies_for_intermediate_steps of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to use cookies for OAuth2 intermediate steps.


        :param use_cookies_for_intermediate_steps: The use_cookies_for_intermediate_steps of this OAuth2ResponseValidationFailurePolicy.
        :type: bool
        """
        self._use_cookies_for_intermediate_steps = use_cookies_for_intermediate_steps

    @property
    def use_pkce(self):
        """
        Gets the use_pkce of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to support PKCE.


        :return: The use_pkce of this OAuth2ResponseValidationFailurePolicy.
        :rtype: bool
        """
        return self._use_pkce

    @use_pkce.setter
    def use_pkce(self, use_pkce):
        """
        Sets the use_pkce of this OAuth2ResponseValidationFailurePolicy.
        Defines whether or not to support PKCE.


        :param use_pkce: The use_pkce of this OAuth2ResponseValidationFailurePolicy.
        :type: bool
        """
        self._use_pkce = use_pkce

    @property
    def response_type(self):
        """
        **[Required]** Gets the response_type of this OAuth2ResponseValidationFailurePolicy.
        Response Type.

        Allowed values for this property are: "CODE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The response_type of this OAuth2ResponseValidationFailurePolicy.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """
        Sets the response_type of this OAuth2ResponseValidationFailurePolicy.
        Response Type.


        :param response_type: The response_type of this OAuth2ResponseValidationFailurePolicy.
        :type: str
        """
        allowed_values = ["CODE"]
        if not value_allowed_none_or_none_sentinel(response_type, allowed_values):
            response_type = 'UNKNOWN_ENUM_VALUE'
        self._response_type = response_type

    @property
    def fallback_redirect_path(self):
        """
        Gets the fallback_redirect_path of this OAuth2ResponseValidationFailurePolicy.
        The path to be used as fallback after OAuth2.


        :return: The fallback_redirect_path of this OAuth2ResponseValidationFailurePolicy.
        :rtype: str
        """
        return self._fallback_redirect_path

    @fallback_redirect_path.setter
    def fallback_redirect_path(self, fallback_redirect_path):
        """
        Sets the fallback_redirect_path of this OAuth2ResponseValidationFailurePolicy.
        The path to be used as fallback after OAuth2.


        :param fallback_redirect_path: The fallback_redirect_path of this OAuth2ResponseValidationFailurePolicy.
        :type: str
        """
        self._fallback_redirect_path = fallback_redirect_path

    @property
    def logout_path(self):
        """
        Gets the logout_path of this OAuth2ResponseValidationFailurePolicy.
        The path to be used as logout.


        :return: The logout_path of this OAuth2ResponseValidationFailurePolicy.
        :rtype: str
        """
        return self._logout_path

    @logout_path.setter
    def logout_path(self, logout_path):
        """
        Sets the logout_path of this OAuth2ResponseValidationFailurePolicy.
        The path to be used as logout.


        :param logout_path: The logout_path of this OAuth2ResponseValidationFailurePolicy.
        :type: str
        """
        self._logout_path = logout_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
