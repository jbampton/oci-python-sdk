# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningTaskCredentialDetails(object):
    """
    The credential to be used to connect to the database.
    """

    #: A constant which can be used with the sql_tuning_task_credential_type property of a SqlTuningTaskCredentialDetails.
    #: This constant has a value of "SECRET"
    SQL_TUNING_TASK_CREDENTIAL_TYPE_SECRET = "SECRET"

    #: A constant which can be used with the sql_tuning_task_credential_type property of a SqlTuningTaskCredentialDetails.
    #: This constant has a value of "PASSWORD"
    SQL_TUNING_TASK_CREDENTIAL_TYPE_PASSWORD = "PASSWORD"

    #: A constant which can be used with the role property of a SqlTuningTaskCredentialDetails.
    #: This constant has a value of "NORMAL"
    ROLE_NORMAL = "NORMAL"

    #: A constant which can be used with the role property of a SqlTuningTaskCredentialDetails.
    #: This constant has a value of "SYSDBA"
    ROLE_SYSDBA = "SYSDBA"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningTaskCredentialDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.SqlTuningTaskSecretCredentialDetails`
        * :class:`~oci.database_management.models.SqlTuningTaskPasswordCredentialDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_task_credential_type:
            The value to assign to the sql_tuning_task_credential_type property of this SqlTuningTaskCredentialDetails.
            Allowed values for this property are: "SECRET", "PASSWORD"
        :type sql_tuning_task_credential_type: str

        :param username:
            The value to assign to the username property of this SqlTuningTaskCredentialDetails.
        :type username: str

        :param role:
            The value to assign to the role property of this SqlTuningTaskCredentialDetails.
            Allowed values for this property are: "NORMAL", "SYSDBA"
        :type role: str

        """
        self.swagger_types = {
            'sql_tuning_task_credential_type': 'str',
            'username': 'str',
            'role': 'str'
        }

        self.attribute_map = {
            'sql_tuning_task_credential_type': 'sqlTuningTaskCredentialType',
            'username': 'username',
            'role': 'role'
        }

        self._sql_tuning_task_credential_type = None
        self._username = None
        self._role = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['sqlTuningTaskCredentialType']

        if type == 'SECRET':
            return 'SqlTuningTaskSecretCredentialDetails'

        if type == 'PASSWORD':
            return 'SqlTuningTaskPasswordCredentialDetails'
        else:
            return 'SqlTuningTaskCredentialDetails'

    @property
    def sql_tuning_task_credential_type(self):
        """
        **[Required]** Gets the sql_tuning_task_credential_type of this SqlTuningTaskCredentialDetails.
        The type pf the credential for SQL tuning task.

        Allowed values for this property are: "SECRET", "PASSWORD"


        :return: The sql_tuning_task_credential_type of this SqlTuningTaskCredentialDetails.
        :rtype: str
        """
        return self._sql_tuning_task_credential_type

    @sql_tuning_task_credential_type.setter
    def sql_tuning_task_credential_type(self, sql_tuning_task_credential_type):
        """
        Sets the sql_tuning_task_credential_type of this SqlTuningTaskCredentialDetails.
        The type pf the credential for SQL tuning task.


        :param sql_tuning_task_credential_type: The sql_tuning_task_credential_type of this SqlTuningTaskCredentialDetails.
        :type: str
        """
        allowed_values = ["SECRET", "PASSWORD"]
        if not value_allowed_none_or_none_sentinel(sql_tuning_task_credential_type, allowed_values):
            raise ValueError(
                "Invalid value for `sql_tuning_task_credential_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sql_tuning_task_credential_type = sql_tuning_task_credential_type

    @property
    def username(self):
        """
        **[Required]** Gets the username of this SqlTuningTaskCredentialDetails.
        The user to connect to the database.


        :return: The username of this SqlTuningTaskCredentialDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SqlTuningTaskCredentialDetails.
        The user to connect to the database.


        :param username: The username of this SqlTuningTaskCredentialDetails.
        :type: str
        """
        self._username = username

    @property
    def role(self):
        """
        **[Required]** Gets the role of this SqlTuningTaskCredentialDetails.
        The role of the database user.

        Allowed values for this property are: "NORMAL", "SYSDBA"


        :return: The role of this SqlTuningTaskCredentialDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this SqlTuningTaskCredentialDetails.
        The role of the database user.


        :param role: The role of this SqlTuningTaskCredentialDetails.
        :type: str
        """
        allowed_values = ["NORMAL", "SYSDBA"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                "Invalid value for `role`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
