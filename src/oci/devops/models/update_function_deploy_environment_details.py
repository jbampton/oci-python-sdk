# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_environment_details import UpdateDeployEnvironmentDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFunctionDeployEnvironmentDetails(UpdateDeployEnvironmentDetails):
    """
    Specifies the Function environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFunctionDeployEnvironmentDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateFunctionDeployEnvironmentDetails.deploy_environment_type` attribute
        of this class is ``FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateFunctionDeployEnvironmentDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateFunctionDeployEnvironmentDetails.
        :type display_name: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this UpdateFunctionDeployEnvironmentDetails.
        :type deploy_environment_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateFunctionDeployEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateFunctionDeployEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param function_id:
            The value to assign to the function_id property of this UpdateFunctionDeployEnvironmentDetails.
        :type function_id: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_environment_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'function_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_environment_type': 'deployEnvironmentType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'function_id': 'functionId'
        }

        self._description = None
        self._display_name = None
        self._deploy_environment_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._function_id = None
        self._deploy_environment_type = 'FUNCTION'

    @property
    def function_id(self):
        """
        Gets the function_id of this UpdateFunctionDeployEnvironmentDetails.
        The OCID of the Function.


        :return: The function_id of this UpdateFunctionDeployEnvironmentDetails.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """
        Sets the function_id of this UpdateFunctionDeployEnvironmentDetails.
        The OCID of the Function.


        :param function_id: The function_id of this UpdateFunctionDeployEnvironmentDetails.
        :type: str
        """
        self._function_id = function_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
