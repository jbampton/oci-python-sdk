# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SaasAdminUserStatus(object):
    """
    SaaS administrative user status.
    """

    #: A constant which can be used with the access_type property of a SaasAdminUserStatus.
    #: This constant has a value of "READ_ONLY"
    ACCESS_TYPE_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the access_type property of a SaasAdminUserStatus.
    #: This constant has a value of "READ_WRITE"
    ACCESS_TYPE_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the access_type property of a SaasAdminUserStatus.
    #: This constant has a value of "ADMIN"
    ACCESS_TYPE_ADMIN = "ADMIN"

    def __init__(self, **kwargs):
        """
        Initializes a new SaasAdminUserStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this SaasAdminUserStatus.
        :type is_enabled: bool

        :param access_type:
            The value to assign to the access_type property of this SaasAdminUserStatus.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE", "ADMIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type access_type: str

        :param time_saas_admin_user_enabled:
            The value to assign to the time_saas_admin_user_enabled property of this SaasAdminUserStatus.
        :type time_saas_admin_user_enabled: datetime

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'access_type': 'str',
            'time_saas_admin_user_enabled': 'datetime'
        }
        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'access_type': 'accessType',
            'time_saas_admin_user_enabled': 'timeSaasAdminUserEnabled'
        }
        self._is_enabled = None
        self._access_type = None
        self._time_saas_admin_user_enabled = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this SaasAdminUserStatus.
        Indicates if the SaaS administrative user is enabled for the Autonomous Database.


        :return: The is_enabled of this SaasAdminUserStatus.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this SaasAdminUserStatus.
        Indicates if the SaaS administrative user is enabled for the Autonomous Database.


        :param is_enabled: The is_enabled of this SaasAdminUserStatus.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def access_type(self):
        """
        Gets the access_type of this SaasAdminUserStatus.
        The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE", "ADMIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The access_type of this SaasAdminUserStatus.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """
        Sets the access_type of this SaasAdminUserStatus.
        The access type for the SaaS administrative user. If no access type is specified, the READ_ONLY access type is used.


        :param access_type: The access_type of this SaasAdminUserStatus.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE", "ADMIN"]
        if not value_allowed_none_or_none_sentinel(access_type, allowed_values):
            access_type = 'UNKNOWN_ENUM_VALUE'
        self._access_type = access_type

    @property
    def time_saas_admin_user_enabled(self):
        """
        Gets the time_saas_admin_user_enabled of this SaasAdminUserStatus.
        The date and time the SaaS administrative user was enabled at, for the Autonomous Database.


        :return: The time_saas_admin_user_enabled of this SaasAdminUserStatus.
        :rtype: datetime
        """
        return self._time_saas_admin_user_enabled

    @time_saas_admin_user_enabled.setter
    def time_saas_admin_user_enabled(self, time_saas_admin_user_enabled):
        """
        Sets the time_saas_admin_user_enabled of this SaasAdminUserStatus.
        The date and time the SaaS administrative user was enabled at, for the Autonomous Database.


        :param time_saas_admin_user_enabled: The time_saas_admin_user_enabled of this SaasAdminUserStatus.
        :type: datetime
        """
        self._time_saas_admin_user_enabled = time_saas_admin_user_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
