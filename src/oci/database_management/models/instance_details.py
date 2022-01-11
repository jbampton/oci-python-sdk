# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceDetails(object):
    """
    The details of the Oracle Real Application Clusters (Oracle RAC) database instance.
    """

    #: A constant which can be used with the status property of a InstanceDetails.
    #: This constant has a value of "UP"
    STATUS_UP = "UP"

    #: A constant which can be used with the status property of a InstanceDetails.
    #: This constant has a value of "DOWN"
    STATUS_DOWN = "DOWN"

    #: A constant which can be used with the status property of a InstanceDetails.
    #: This constant has a value of "UNKNOWN"
    STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this InstanceDetails.
        :type id: int

        :param name:
            The value to assign to the name property of this InstanceDetails.
        :type name: str

        :param host_name:
            The value to assign to the host_name property of this InstanceDetails.
        :type host_name: str

        :param status:
            The value to assign to the status property of this InstanceDetails.
            Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'host_name': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'host_name': 'hostName',
            'status': 'status'
        }

        self._id = None
        self._name = None
        self._host_name = None
        self._status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this InstanceDetails.
        The ID of the Oracle RAC database instance.


        :return: The id of this InstanceDetails.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceDetails.
        The ID of the Oracle RAC database instance.


        :param id: The id of this InstanceDetails.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this InstanceDetails.
        The name of the Oracle RAC database instance.


        :return: The name of this InstanceDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstanceDetails.
        The name of the Oracle RAC database instance.


        :param name: The name of this InstanceDetails.
        :type: str
        """
        self._name = name

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this InstanceDetails.
        The name of the host of the Oracle RAC database instance.


        :return: The host_name of this InstanceDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this InstanceDetails.
        The name of the host of the Oracle RAC database instance.


        :param host_name: The host_name of this InstanceDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this InstanceDetails.
        The status of the Oracle RAC database instance.

        Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this InstanceDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InstanceDetails.
        The status of the Oracle RAC database instance.


        :param status: The status of this InstanceDetails.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
