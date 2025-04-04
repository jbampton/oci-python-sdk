# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .deploy_artifact_source import DeployArtifactSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HelmCommandSpecArtifactSource(DeployArtifactSource):
    """
    Specifies Helm command spec details
    """

    #: A constant which can be used with the helm_artifact_source_type property of a HelmCommandSpecArtifactSource.
    #: This constant has a value of "INLINE"
    HELM_ARTIFACT_SOURCE_TYPE_INLINE = "INLINE"

    def __init__(self, **kwargs):
        """
        Initializes a new HelmCommandSpecArtifactSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.HelmCommandSpecArtifactSource.deploy_artifact_source_type` attribute
        of this class is ``HELM_COMMAND_SPEC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_artifact_source_type:
            The value to assign to the deploy_artifact_source_type property of this HelmCommandSpecArtifactSource.
            Allowed values for this property are: "INLINE", "OCIR", "GENERIC_ARTIFACT", "HELM_CHART", "HELM_COMMAND_SPEC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_artifact_source_type: str

        :param base64_encoded_content:
            The value to assign to the base64_encoded_content property of this HelmCommandSpecArtifactSource.
        :type base64_encoded_content: str

        :param helm_artifact_source_type:
            The value to assign to the helm_artifact_source_type property of this HelmCommandSpecArtifactSource.
            Allowed values for this property are: "INLINE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type helm_artifact_source_type: str

        """
        self.swagger_types = {
            'deploy_artifact_source_type': 'str',
            'base64_encoded_content': 'str',
            'helm_artifact_source_type': 'str'
        }
        self.attribute_map = {
            'deploy_artifact_source_type': 'deployArtifactSourceType',
            'base64_encoded_content': 'base64EncodedContent',
            'helm_artifact_source_type': 'helmArtifactSourceType'
        }
        self._deploy_artifact_source_type = None
        self._base64_encoded_content = None
        self._helm_artifact_source_type = None
        self._deploy_artifact_source_type = 'HELM_COMMAND_SPEC'

    @property
    def base64_encoded_content(self):
        """
        **[Required]** Gets the base64_encoded_content of this HelmCommandSpecArtifactSource.
        The Helm commands to be executed, base 64 encoded


        :return: The base64_encoded_content of this HelmCommandSpecArtifactSource.
        :rtype: str
        """
        return self._base64_encoded_content

    @base64_encoded_content.setter
    def base64_encoded_content(self, base64_encoded_content):
        """
        Sets the base64_encoded_content of this HelmCommandSpecArtifactSource.
        The Helm commands to be executed, base 64 encoded


        :param base64_encoded_content: The base64_encoded_content of this HelmCommandSpecArtifactSource.
        :type: str
        """
        self._base64_encoded_content = base64_encoded_content

    @property
    def helm_artifact_source_type(self):
        """
        **[Required]** Gets the helm_artifact_source_type of this HelmCommandSpecArtifactSource.
        Specifies types of artifact sources.

        Allowed values for this property are: "INLINE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The helm_artifact_source_type of this HelmCommandSpecArtifactSource.
        :rtype: str
        """
        return self._helm_artifact_source_type

    @helm_artifact_source_type.setter
    def helm_artifact_source_type(self, helm_artifact_source_type):
        """
        Sets the helm_artifact_source_type of this HelmCommandSpecArtifactSource.
        Specifies types of artifact sources.


        :param helm_artifact_source_type: The helm_artifact_source_type of this HelmCommandSpecArtifactSource.
        :type: str
        """
        allowed_values = ["INLINE"]
        if not value_allowed_none_or_none_sentinel(helm_artifact_source_type, allowed_values):
            helm_artifact_source_type = 'UNKNOWN_ENUM_VALUE'
        self._helm_artifact_source_type = helm_artifact_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
