# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240102


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInfo(object):
    """
    The Host Info.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_name:
            The value to assign to the host_name property of this HostInfo.
        :type host_name: str

        :param host_cores:
            The value to assign to the host_cores property of this HostInfo.
        :type host_cores: int

        """
        self.swagger_types = {
            'host_name': 'str',
            'host_cores': 'int'
        }

        self.attribute_map = {
            'host_name': 'hostName',
            'host_cores': 'hostCores'
        }

        self._host_name = None
        self._host_cores = None

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostInfo.
        The name of the host.


        :return: The host_name of this HostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostInfo.
        The name of the host.


        :param host_name: The host_name of this HostInfo.
        :type: str
        """
        self._host_name = host_name

    @property
    def host_cores(self):
        """
        **[Required]** Gets the host_cores of this HostInfo.
        Number of host cores.


        :return: The host_cores of this HostInfo.
        :rtype: int
        """
        return self._host_cores

    @host_cores.setter
    def host_cores(self, host_cores):
        """
        Sets the host_cores of this HostInfo.
        Number of host cores.


        :param host_cores: The host_cores of this HostInfo.
        :type: int
        """
        self._host_cores = host_cores

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
