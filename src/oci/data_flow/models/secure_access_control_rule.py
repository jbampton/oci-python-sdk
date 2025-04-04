# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecureAccessControlRule(object):
    """
    The access control rule for SECURE_ACCESS network type selection.
    """

    #: A constant which can be used with the ip_notation property of a SecureAccessControlRule.
    #: This constant has a value of "IP_ADDRESS"
    IP_NOTATION_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the ip_notation property of a SecureAccessControlRule.
    #: This constant has a value of "CIDR"
    IP_NOTATION_CIDR = "CIDR"

    #: A constant which can be used with the ip_notation property of a SecureAccessControlRule.
    #: This constant has a value of "VCN"
    IP_NOTATION_VCN = "VCN"

    #: A constant which can be used with the ip_notation property of a SecureAccessControlRule.
    #: This constant has a value of "VCN_OCID"
    IP_NOTATION_VCN_OCID = "VCN_OCID"

    def __init__(self, **kwargs):
        """
        Initializes a new SecureAccessControlRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_notation:
            The value to assign to the ip_notation property of this SecureAccessControlRule.
            Allowed values for this property are: "IP_ADDRESS", "CIDR", "VCN", "VCN_OCID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ip_notation: str

        :param value:
            The value to assign to the value property of this SecureAccessControlRule.
        :type value: str

        :param vcn_ips:
            The value to assign to the vcn_ips property of this SecureAccessControlRule.
        :type vcn_ips: str

        """
        self.swagger_types = {
            'ip_notation': 'str',
            'value': 'str',
            'vcn_ips': 'str'
        }
        self.attribute_map = {
            'ip_notation': 'ipNotation',
            'value': 'value',
            'vcn_ips': 'vcnIps'
        }
        self._ip_notation = None
        self._value = None
        self._vcn_ips = None

    @property
    def ip_notation(self):
        """
        **[Required]** Gets the ip_notation of this SecureAccessControlRule.
        The type of IP notation.

        Allowed values for this property are: "IP_ADDRESS", "CIDR", "VCN", "VCN_OCID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ip_notation of this SecureAccessControlRule.
        :rtype: str
        """
        return self._ip_notation

    @ip_notation.setter
    def ip_notation(self, ip_notation):
        """
        Sets the ip_notation of this SecureAccessControlRule.
        The type of IP notation.


        :param ip_notation: The ip_notation of this SecureAccessControlRule.
        :type: str
        """
        allowed_values = ["IP_ADDRESS", "CIDR", "VCN", "VCN_OCID"]
        if not value_allowed_none_or_none_sentinel(ip_notation, allowed_values):
            ip_notation = 'UNKNOWN_ENUM_VALUE'
        self._ip_notation = ip_notation

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SecureAccessControlRule.
        The associated value of the selected IP notation.


        :return: The value of this SecureAccessControlRule.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SecureAccessControlRule.
        The associated value of the selected IP notation.


        :param value: The value of this SecureAccessControlRule.
        :type: str
        """
        self._value = value

    @property
    def vcn_ips(self):
        """
        Gets the vcn_ips of this SecureAccessControlRule.
        A comma-separated IP or CIDR address for VCN OCID IP notation selection.


        :return: The vcn_ips of this SecureAccessControlRule.
        :rtype: str
        """
        return self._vcn_ips

    @vcn_ips.setter
    def vcn_ips(self, vcn_ips):
        """
        Sets the vcn_ips of this SecureAccessControlRule.
        A comma-separated IP or CIDR address for VCN OCID IP notation selection.


        :param vcn_ips: The vcn_ips of this SecureAccessControlRule.
        :type: str
        """
        self._vcn_ips = vcn_ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
