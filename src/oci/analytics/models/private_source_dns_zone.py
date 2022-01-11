# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateSourceDnsZone(object):
    """
    Private source DNS Zone model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateSourceDnsZone object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dns_zone:
            The value to assign to the dns_zone property of this PrivateSourceDnsZone.
        :type dns_zone: str

        :param description:
            The value to assign to the description property of this PrivateSourceDnsZone.
        :type description: str

        """
        self.swagger_types = {
            'dns_zone': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'dns_zone': 'dnsZone',
            'description': 'description'
        }

        self._dns_zone = None
        self._description = None

    @property
    def dns_zone(self):
        """
        **[Required]** Gets the dns_zone of this PrivateSourceDnsZone.
        Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com.


        :return: The dns_zone of this PrivateSourceDnsZone.
        :rtype: str
        """
        return self._dns_zone

    @dns_zone.setter
    def dns_zone(self, dns_zone):
        """
        Sets the dns_zone of this PrivateSourceDnsZone.
        Private Source DNS Zone. Ex: example-vcn.oraclevcn.com, corp.example.com.


        :param dns_zone: The dns_zone of this PrivateSourceDnsZone.
        :type: str
        """
        self._dns_zone = dns_zone

    @property
    def description(self):
        """
        Gets the description of this PrivateSourceDnsZone.
        Description of private source dns zone.


        :return: The description of this PrivateSourceDnsZone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrivateSourceDnsZone.
        Description of private source dns zone.


        :param description: The description of this PrivateSourceDnsZone.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
