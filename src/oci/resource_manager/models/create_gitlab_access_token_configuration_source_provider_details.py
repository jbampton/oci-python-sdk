# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_configuration_source_provider_details import CreateConfigurationSourceProviderDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateGitlabAccessTokenConfigurationSourceProviderDetails(CreateConfigurationSourceProviderDetails):
    """
    The details for creating a configuration source provider of the type `GITLAB_ACCESS_TOKEN`.
    This type corresponds to a configuration source provider in GitLab that is authenticated with a personal access token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateGitlabAccessTokenConfigurationSourceProviderDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateGitlabAccessTokenConfigurationSourceProviderDetails.config_source_provider_type` attribute
        of this class is ``GITLAB_ACCESS_TOKEN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type description: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type config_source_provider_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param api_endpoint:
            The value to assign to the api_endpoint property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type api_endpoint: str

        :param access_token:
            The value to assign to the access_token property of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type access_token: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'config_source_provider_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'api_endpoint': 'str',
            'access_token': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'config_source_provider_type': 'configSourceProviderType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'api_endpoint': 'apiEndpoint',
            'access_token': 'accessToken'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._config_source_provider_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._api_endpoint = None
        self._access_token = None
        self._config_source_provider_type = 'GITLAB_ACCESS_TOKEN'

    @property
    def api_endpoint(self):
        """
        **[Required]** Gets the api_endpoint of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        The Git service endpoint.
        Example: `https://gitlab.com`


        :return: The api_endpoint of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """
        Sets the api_endpoint of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        The Git service endpoint.
        Example: `https://gitlab.com`


        :param api_endpoint: The api_endpoint of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type: str
        """
        self._api_endpoint = api_endpoint

    @property
    def access_token(self):
        """
        **[Required]** Gets the access_token of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        The personal access token to be configured on the GitLab repository. Avoid entering confidential information.


        :return: The access_token of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        The personal access token to be configured on the GitLab repository. Avoid entering confidential information.


        :param access_token: The access_token of this CreateGitlabAccessTokenConfigurationSourceProviderDetails.
        :type: str
        """
        self._access_token = access_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
