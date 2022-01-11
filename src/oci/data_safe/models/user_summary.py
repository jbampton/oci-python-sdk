# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserSummary(object):
    """
    The summary of information about the database user. It includes details such as user type, account status,
    last login time, user creation time, authentication type, user profile, and time and date of the last password change.
    It also contains the user category derived from these user details, as well as granted privileges.
    """

    #: A constant which can be used with the user_category property of a UserSummary.
    #: This constant has a value of "CRITICAL"
    USER_CATEGORY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the user_category property of a UserSummary.
    #: This constant has a value of "HIGH"
    USER_CATEGORY_HIGH = "HIGH"

    #: A constant which can be used with the user_category property of a UserSummary.
    #: This constant has a value of "MEDIUM"
    USER_CATEGORY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the user_category property of a UserSummary.
    #: This constant has a value of "LOW"
    USER_CATEGORY_LOW = "LOW"

    #: A constant which can be used with the account_status property of a UserSummary.
    #: This constant has a value of "OPEN"
    ACCOUNT_STATUS_OPEN = "OPEN"

    #: A constant which can be used with the account_status property of a UserSummary.
    #: This constant has a value of "LOCKED"
    ACCOUNT_STATUS_LOCKED = "LOCKED"

    #: A constant which can be used with the account_status property of a UserSummary.
    #: This constant has a value of "EXPIRED"
    ACCOUNT_STATUS_EXPIRED = "EXPIRED"

    #: A constant which can be used with the account_status property of a UserSummary.
    #: This constant has a value of "EXPIRED_AND_LOCKED"
    ACCOUNT_STATUS_EXPIRED_AND_LOCKED = "EXPIRED_AND_LOCKED"

    #: A constant which can be used with the account_status property of a UserSummary.
    #: This constant has a value of "NONE"
    ACCOUNT_STATUS_NONE = "NONE"

    #: A constant which can be used with the authentication_type property of a UserSummary.
    #: This constant has a value of "PASSWORD"
    AUTHENTICATION_TYPE_PASSWORD = "PASSWORD"

    #: A constant which can be used with the authentication_type property of a UserSummary.
    #: This constant has a value of "NONE"
    AUTHENTICATION_TYPE_NONE = "NONE"

    #: A constant which can be used with the user_types property of a UserSummary.
    #: This constant has a value of "ADMIN_PRIVILEGED"
    USER_TYPES_ADMIN_PRIVILEGED = "ADMIN_PRIVILEGED"

    #: A constant which can be used with the user_types property of a UserSummary.
    #: This constant has a value of "APPLICATION"
    USER_TYPES_APPLICATION = "APPLICATION"

    #: A constant which can be used with the user_types property of a UserSummary.
    #: This constant has a value of "PRIVILEGED"
    USER_TYPES_PRIVILEGED = "PRIVILEGED"

    #: A constant which can be used with the user_types property of a UserSummary.
    #: This constant has a value of "SCHEMA"
    USER_TYPES_SCHEMA = "SCHEMA"

    #: A constant which can be used with the user_types property of a UserSummary.
    #: This constant has a value of "NON_PRIVILEGED"
    USER_TYPES_NON_PRIVILEGED = "NON_PRIVILEGED"

    #: A constant which can be used with the admin_roles property of a UserSummary.
    #: This constant has a value of "PDB_DBA"
    ADMIN_ROLES_PDB_DBA = "PDB_DBA"

    #: A constant which can be used with the admin_roles property of a UserSummary.
    #: This constant has a value of "DBA"
    ADMIN_ROLES_DBA = "DBA"

    #: A constant which can be used with the admin_roles property of a UserSummary.
    #: This constant has a value of "DV_ADMIN"
    ADMIN_ROLES_DV_ADMIN = "DV_ADMIN"

    #: A constant which can be used with the admin_roles property of a UserSummary.
    #: This constant has a value of "AUDIT_ADMIN"
    ADMIN_ROLES_AUDIT_ADMIN = "AUDIT_ADMIN"

    def __init__(self, **kwargs):
        """
        Initializes a new UserSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this UserSummary.
        :type key: str

        :param user_name:
            The value to assign to the user_name property of this UserSummary.
        :type user_name: str

        :param user_category:
            The value to assign to the user_category property of this UserSummary.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type user_category: str

        :param account_status:
            The value to assign to the account_status property of this UserSummary.
            Allowed values for this property are: "OPEN", "LOCKED", "EXPIRED", "EXPIRED_AND_LOCKED", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type account_status: str

        :param target_id:
            The value to assign to the target_id property of this UserSummary.
        :type target_id: str

        :param time_last_login:
            The value to assign to the time_last_login property of this UserSummary.
        :type time_last_login: datetime

        :param time_user_created:
            The value to assign to the time_user_created property of this UserSummary.
        :type time_user_created: datetime

        :param authentication_type:
            The value to assign to the authentication_type property of this UserSummary.
            Allowed values for this property are: "PASSWORD", "NONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type authentication_type: str

        :param user_profile:
            The value to assign to the user_profile property of this UserSummary.
        :type user_profile: str

        :param time_password_changed:
            The value to assign to the time_password_changed property of this UserSummary.
        :type time_password_changed: datetime

        :param user_types:
            The value to assign to the user_types property of this UserSummary.
            Allowed values for items in this list are: "ADMIN_PRIVILEGED", "APPLICATION", "PRIVILEGED", "SCHEMA", "NON_PRIVILEGED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type user_types: list[str]

        :param admin_roles:
            The value to assign to the admin_roles property of this UserSummary.
            Allowed values for items in this list are: "PDB_DBA", "DBA", "DV_ADMIN", "AUDIT_ADMIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type admin_roles: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'user_name': 'str',
            'user_category': 'str',
            'account_status': 'str',
            'target_id': 'str',
            'time_last_login': 'datetime',
            'time_user_created': 'datetime',
            'authentication_type': 'str',
            'user_profile': 'str',
            'time_password_changed': 'datetime',
            'user_types': 'list[str]',
            'admin_roles': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'user_name': 'userName',
            'user_category': 'userCategory',
            'account_status': 'accountStatus',
            'target_id': 'targetId',
            'time_last_login': 'timeLastLogin',
            'time_user_created': 'timeUserCreated',
            'authentication_type': 'authenticationType',
            'user_profile': 'userProfile',
            'time_password_changed': 'timePasswordChanged',
            'user_types': 'userTypes',
            'admin_roles': 'adminRoles'
        }

        self._key = None
        self._user_name = None
        self._user_category = None
        self._account_status = None
        self._target_id = None
        self._time_last_login = None
        self._time_user_created = None
        self._authentication_type = None
        self._user_profile = None
        self._time_password_changed = None
        self._user_types = None
        self._admin_roles = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this UserSummary.
        The unique user key. This is a system-generated identifier. Use ListUsers to get the user key for a user.


        :return: The key of this UserSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UserSummary.
        The unique user key. This is a system-generated identifier. Use ListUsers to get the user key for a user.


        :param key: The key of this UserSummary.
        :type: str
        """
        self._key = key

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this UserSummary.
        The database user name.


        :return: The user_name of this UserSummary.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UserSummary.
        The database user name.


        :param user_name: The user_name of this UserSummary.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_category(self):
        """
        Gets the user_category of this UserSummary.
        The user category based on the privileges and other details of the user.

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The user_category of this UserSummary.
        :rtype: str
        """
        return self._user_category

    @user_category.setter
    def user_category(self, user_category):
        """
        Sets the user_category of this UserSummary.
        The user category based on the privileges and other details of the user.


        :param user_category: The user_category of this UserSummary.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if not value_allowed_none_or_none_sentinel(user_category, allowed_values):
            user_category = 'UNKNOWN_ENUM_VALUE'
        self._user_category = user_category

    @property
    def account_status(self):
        """
        Gets the account_status of this UserSummary.
        The user account status.

        Allowed values for this property are: "OPEN", "LOCKED", "EXPIRED", "EXPIRED_AND_LOCKED", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The account_status of this UserSummary.
        :rtype: str
        """
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        """
        Sets the account_status of this UserSummary.
        The user account status.


        :param account_status: The account_status of this UserSummary.
        :type: str
        """
        allowed_values = ["OPEN", "LOCKED", "EXPIRED", "EXPIRED_AND_LOCKED", "NONE"]
        if not value_allowed_none_or_none_sentinel(account_status, allowed_values):
            account_status = 'UNKNOWN_ENUM_VALUE'
        self._account_status = account_status

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this UserSummary.
        The OCID of the target database.


        :return: The target_id of this UserSummary.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this UserSummary.
        The OCID of the target database.


        :param target_id: The target_id of this UserSummary.
        :type: str
        """
        self._target_id = target_id

    @property
    def time_last_login(self):
        """
        Gets the time_last_login of this UserSummary.
        The date and time when the user last logged in, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_last_login of this UserSummary.
        :rtype: datetime
        """
        return self._time_last_login

    @time_last_login.setter
    def time_last_login(self, time_last_login):
        """
        Sets the time_last_login of this UserSummary.
        The date and time when the user last logged in, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_last_login: The time_last_login of this UserSummary.
        :type: datetime
        """
        self._time_last_login = time_last_login

    @property
    def time_user_created(self):
        """
        Gets the time_user_created of this UserSummary.
        The date and time when the user was created in the database, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_user_created of this UserSummary.
        :rtype: datetime
        """
        return self._time_user_created

    @time_user_created.setter
    def time_user_created(self, time_user_created):
        """
        Sets the time_user_created of this UserSummary.
        The date and time when the user was created in the database, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_user_created: The time_user_created of this UserSummary.
        :type: datetime
        """
        self._time_user_created = time_user_created

    @property
    def authentication_type(self):
        """
        Gets the authentication_type of this UserSummary.
        The user authentication method.

        Allowed values for this property are: "PASSWORD", "NONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The authentication_type of this UserSummary.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """
        Sets the authentication_type of this UserSummary.
        The user authentication method.


        :param authentication_type: The authentication_type of this UserSummary.
        :type: str
        """
        allowed_values = ["PASSWORD", "NONE"]
        if not value_allowed_none_or_none_sentinel(authentication_type, allowed_values):
            authentication_type = 'UNKNOWN_ENUM_VALUE'
        self._authentication_type = authentication_type

    @property
    def user_profile(self):
        """
        Gets the user_profile of this UserSummary.
        The user profile name.


        :return: The user_profile of this UserSummary.
        :rtype: str
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        """
        Sets the user_profile of this UserSummary.
        The user profile name.


        :param user_profile: The user_profile of this UserSummary.
        :type: str
        """
        self._user_profile = user_profile

    @property
    def time_password_changed(self):
        """
        Gets the time_password_changed of this UserSummary.
        The date and time when the user password was last changed, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_password_changed of this UserSummary.
        :rtype: datetime
        """
        return self._time_password_changed

    @time_password_changed.setter
    def time_password_changed(self, time_password_changed):
        """
        Sets the time_password_changed of this UserSummary.
        The date and time when the user password was last changed, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_password_changed: The time_password_changed of this UserSummary.
        :type: datetime
        """
        self._time_password_changed = time_password_changed

    @property
    def user_types(self):
        """
        Gets the user_types of this UserSummary.
        The user type, which can be a combination of the following:

        'Admin Privileged': The user has administrative privileges.
        'Application': The user is an Oracle E-Business Suite Applications (EBS) or Fusion Applications (FA) user.
        'Privileged': The user is a privileged user.
        'Schema': The user is EXPIRED & LOCKED / EXPIRED / LOCKED, or a schema-only account (authentication type is NONE).
        'Non-privileged': The user is a non-privileged user.

        Allowed values for items in this list are: "ADMIN_PRIVILEGED", "APPLICATION", "PRIVILEGED", "SCHEMA", "NON_PRIVILEGED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The user_types of this UserSummary.
        :rtype: list[str]
        """
        return self._user_types

    @user_types.setter
    def user_types(self, user_types):
        """
        Sets the user_types of this UserSummary.
        The user type, which can be a combination of the following:

        'Admin Privileged': The user has administrative privileges.
        'Application': The user is an Oracle E-Business Suite Applications (EBS) or Fusion Applications (FA) user.
        'Privileged': The user is a privileged user.
        'Schema': The user is EXPIRED & LOCKED / EXPIRED / LOCKED, or a schema-only account (authentication type is NONE).
        'Non-privileged': The user is a non-privileged user.


        :param user_types: The user_types of this UserSummary.
        :type: list[str]
        """
        allowed_values = ["ADMIN_PRIVILEGED", "APPLICATION", "PRIVILEGED", "SCHEMA", "NON_PRIVILEGED"]
        if user_types:
            user_types[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in user_types]
        self._user_types = user_types

    @property
    def admin_roles(self):
        """
        Gets the admin_roles of this UserSummary.
        The admin roles granted to the user.

        Allowed values for items in this list are: "PDB_DBA", "DBA", "DV_ADMIN", "AUDIT_ADMIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The admin_roles of this UserSummary.
        :rtype: list[str]
        """
        return self._admin_roles

    @admin_roles.setter
    def admin_roles(self, admin_roles):
        """
        Sets the admin_roles of this UserSummary.
        The admin roles granted to the user.


        :param admin_roles: The admin_roles of this UserSummary.
        :type: list[str]
        """
        allowed_values = ["PDB_DBA", "DBA", "DV_ADMIN", "AUDIT_ADMIN"]
        if admin_roles:
            admin_roles[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in admin_roles]
        self._admin_roles = admin_roles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
