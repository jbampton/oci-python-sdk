# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverBundleVersion(object):
    """
    Description of rover bundle version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverBundleVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bundle_version:
            The value to assign to the bundle_version property of this RoverBundleVersion.
        :type bundle_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RoverBundleVersion.
        :type compartment_id: str

        :param bundle_name:
            The value to assign to the bundle_name property of this RoverBundleVersion.
        :type bundle_name: str

        """
        self.swagger_types = {
            'bundle_version': 'str',
            'compartment_id': 'str',
            'bundle_name': 'str'
        }

        self.attribute_map = {
            'bundle_version': 'bundleVersion',
            'compartment_id': 'compartmentId',
            'bundle_name': 'bundleName'
        }

        self._bundle_version = None
        self._compartment_id = None
        self._bundle_name = None

    @property
    def bundle_version(self):
        """
        **[Required]** Gets the bundle_version of this RoverBundleVersion.
        The version of the rover bundle.


        :return: The bundle_version of this RoverBundleVersion.
        :rtype: str
        """
        return self._bundle_version

    @bundle_version.setter
    def bundle_version(self, bundle_version):
        """
        Sets the bundle_version of this RoverBundleVersion.
        The version of the rover bundle.


        :param bundle_version: The bundle_version of this RoverBundleVersion.
        :type: str
        """
        self._bundle_version = bundle_version

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this RoverBundleVersion.
        The compartment OCID of roverNode/roverCluster that needs to be upgraded.


        :return: The compartment_id of this RoverBundleVersion.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RoverBundleVersion.
        The compartment OCID of roverNode/roverCluster that needs to be upgraded.


        :param compartment_id: The compartment_id of this RoverBundleVersion.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def bundle_name(self):
        """
        Gets the bundle_name of this RoverBundleVersion.
        The full name of the bundle.


        :return: The bundle_name of this RoverBundleVersion.
        :rtype: str
        """
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):
        """
        Sets the bundle_name of this RoverBundleVersion.
        The full name of the bundle.


        :param bundle_name: The bundle_name of this RoverBundleVersion.
        :type: str
        """
        self._bundle_name = bundle_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
