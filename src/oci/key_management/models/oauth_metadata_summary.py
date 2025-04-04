# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: release


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OauthMetadataSummary(object):
    """
    Summary about authorization to be returned to the customer as a response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OauthMetadataSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idcs_account_name_url:
            The value to assign to the idcs_account_name_url property of this OauthMetadataSummary.
        :type idcs_account_name_url: str

        :param client_app_id:
            The value to assign to the client_app_id property of this OauthMetadataSummary.
        :type client_app_id: str

        """
        self.swagger_types = {
            'idcs_account_name_url': 'str',
            'client_app_id': 'str'
        }
        self.attribute_map = {
            'idcs_account_name_url': 'idcsAccountNameUrl',
            'client_app_id': 'clientAppId'
        }
        self._idcs_account_name_url = None
        self._client_app_id = None

    @property
    def idcs_account_name_url(self):
        """
        **[Required]** Gets the idcs_account_name_url of this OauthMetadataSummary.
        Base URL of the IDCS account where confidential client app is created.


        :return: The idcs_account_name_url of this OauthMetadataSummary.
        :rtype: str
        """
        return self._idcs_account_name_url

    @idcs_account_name_url.setter
    def idcs_account_name_url(self, idcs_account_name_url):
        """
        Sets the idcs_account_name_url of this OauthMetadataSummary.
        Base URL of the IDCS account where confidential client app is created.


        :param idcs_account_name_url: The idcs_account_name_url of this OauthMetadataSummary.
        :type: str
        """
        self._idcs_account_name_url = idcs_account_name_url

    @property
    def client_app_id(self):
        """
        **[Required]** Gets the client_app_id of this OauthMetadataSummary.
        ID of the client app created in IDP.


        :return: The client_app_id of this OauthMetadataSummary.
        :rtype: str
        """
        return self._client_app_id

    @client_app_id.setter
    def client_app_id(self, client_app_id):
        """
        Sets the client_app_id of this OauthMetadataSummary.
        ID of the client app created in IDP.


        :param client_app_id: The client_app_id of this OauthMetadataSummary.
        :type: str
        """
        self._client_app_id = client_app_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
