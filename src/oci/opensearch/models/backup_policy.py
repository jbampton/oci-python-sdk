# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupPolicy(object):
    """
    Backup policy as optionally used for Opensearch cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this BackupPolicy.
        :type is_enabled: bool

        :param retention_in_days:
            The value to assign to the retention_in_days property of this BackupPolicy.
        :type retention_in_days: int

        :param frequency_in_hours:
            The value to assign to the frequency_in_hours property of this BackupPolicy.
        :type frequency_in_hours: int

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'retention_in_days': 'int',
            'frequency_in_hours': 'int'
        }
        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'retention_in_days': 'retentionInDays',
            'frequency_in_hours': 'frequencyInHours'
        }
        self._is_enabled = None
        self._retention_in_days = None
        self._frequency_in_hours = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this BackupPolicy.
        Specifies if automatic backups are enabled.


        :return: The is_enabled of this BackupPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this BackupPolicy.
        Specifies if automatic backups are enabled.


        :param is_enabled: The is_enabled of this BackupPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def retention_in_days(self):
        """
        Gets the retention_in_days of this BackupPolicy.
        Specifies how long backup copy should remain on Storage in days


        :return: The retention_in_days of this BackupPolicy.
        :rtype: int
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """
        Sets the retention_in_days of this BackupPolicy.
        Specifies how long backup copy should remain on Storage in days


        :param retention_in_days: The retention_in_days of this BackupPolicy.
        :type: int
        """
        self._retention_in_days = retention_in_days

    @property
    def frequency_in_hours(self):
        """
        Gets the frequency_in_hours of this BackupPolicy.
        Specifies how often backup should be performed


        :return: The frequency_in_hours of this BackupPolicy.
        :rtype: int
        """
        return self._frequency_in_hours

    @frequency_in_hours.setter
    def frequency_in_hours(self, frequency_in_hours):
        """
        Sets the frequency_in_hours of this BackupPolicy.
        Specifies how often backup should be performed


        :param frequency_in_hours: The frequency_in_hours of this BackupPolicy.
        :type: int
        """
        self._frequency_in_hours = frequency_in_hours

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
