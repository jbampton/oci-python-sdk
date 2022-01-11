# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FaultDomain(object):
    """
    A Fault Domain is a logical grouping of hardware and infrastructure within an Availability Domain that can become
    unavailable in its entirety either due to hardware failure such as Top-of-rack (TOR) switch failure or due to
    planned software maintenance such as security updates that reboot your instances.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FaultDomain object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FaultDomain.
        :type name: str

        :param id:
            The value to assign to the id property of this FaultDomain.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this FaultDomain.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this FaultDomain.
        :type availability_domain: str

        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain'
        }

        self._name = None
        self._id = None
        self._compartment_id = None
        self._availability_domain = None

    @property
    def name(self):
        """
        Gets the name of this FaultDomain.
        The name of the Fault Domain.


        :return: The name of this FaultDomain.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FaultDomain.
        The name of the Fault Domain.


        :param name: The name of this FaultDomain.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this FaultDomain.
        The OCID of the Fault Domain.


        :return: The id of this FaultDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FaultDomain.
        The OCID of the Fault Domain.


        :param id: The id of this FaultDomain.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this FaultDomain.
        The OCID of the compartment. Currently only tenancy (root) compartment can be provided.


        :return: The compartment_id of this FaultDomain.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FaultDomain.
        The OCID of the compartment. Currently only tenancy (root) compartment can be provided.


        :param compartment_id: The compartment_id of this FaultDomain.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this FaultDomain.
        The name of the availabilityDomain where the Fault Domain belongs.


        :return: The availability_domain of this FaultDomain.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this FaultDomain.
        The name of the availabilityDomain where the Fault Domain belongs.


        :param availability_domain: The availability_domain of this FaultDomain.
        :type: str
        """
        self._availability_domain = availability_domain

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
