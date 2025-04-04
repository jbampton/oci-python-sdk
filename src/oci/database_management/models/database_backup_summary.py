# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseBackupSummary(object):
    """
    The summary of the High Availability (HA) and backup for a database.
    """

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "DISK"
    BACKUP_DESTINATION_DISK = "DISK"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "TAPE"
    BACKUP_DESTINATION_TAPE = "TAPE"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "NFS"
    BACKUP_DESTINATION_NFS = "NFS"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "LOCAL"
    BACKUP_DESTINATION_LOCAL = "LOCAL"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "DBRS"
    BACKUP_DESTINATION_DBRS = "DBRS"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "OBJECT_STORE"
    BACKUP_DESTINATION_OBJECT_STORE = "OBJECT_STORE"

    #: A constant which can be used with the backup_destination property of a DatabaseBackupSummary.
    #: This constant has a value of "RECOVERY_APPLIANCE"
    BACKUP_DESTINATION_RECOVERY_APPLIANCE = "RECOVERY_APPLIANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseBackupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_status:
            The value to assign to the backup_status property of this DatabaseBackupSummary.
        :type backup_status: str

        :param time_backup_completed:
            The value to assign to the time_backup_completed property of this DatabaseBackupSummary.
        :type time_backup_completed: datetime

        :param backup_duration_in_seconds:
            The value to assign to the backup_duration_in_seconds property of this DatabaseBackupSummary.
        :type backup_duration_in_seconds: int

        :param backup_type:
            The value to assign to the backup_type property of this DatabaseBackupSummary.
        :type backup_type: str

        :param backup_destination:
            The value to assign to the backup_destination property of this DatabaseBackupSummary.
            Allowed values for this property are: "DISK", "TAPE", "NFS", "LOCAL", "DBRS", "OBJECT_STORE", "RECOVERY_APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_destination: str

        :param backup_size_in_gbs:
            The value to assign to the backup_size_in_gbs property of this DatabaseBackupSummary.
        :type backup_size_in_gbs: float

        """
        self.swagger_types = {
            'backup_status': 'str',
            'time_backup_completed': 'datetime',
            'backup_duration_in_seconds': 'int',
            'backup_type': 'str',
            'backup_destination': 'str',
            'backup_size_in_gbs': 'float'
        }
        self.attribute_map = {
            'backup_status': 'backupStatus',
            'time_backup_completed': 'timeBackupCompleted',
            'backup_duration_in_seconds': 'backupDurationInSeconds',
            'backup_type': 'backupType',
            'backup_destination': 'backupDestination',
            'backup_size_in_gbs': 'backupSizeInGBs'
        }
        self._backup_status = None
        self._time_backup_completed = None
        self._backup_duration_in_seconds = None
        self._backup_type = None
        self._backup_destination = None
        self._backup_size_in_gbs = None

    @property
    def backup_status(self):
        """
        **[Required]** Gets the backup_status of this DatabaseBackupSummary.
        The backup status of the database.


        :return: The backup_status of this DatabaseBackupSummary.
        :rtype: str
        """
        return self._backup_status

    @backup_status.setter
    def backup_status(self, backup_status):
        """
        Sets the backup_status of this DatabaseBackupSummary.
        The backup status of the database.


        :param backup_status: The backup_status of this DatabaseBackupSummary.
        :type: str
        """
        self._backup_status = backup_status

    @property
    def time_backup_completed(self):
        """
        **[Required]** Gets the time_backup_completed of this DatabaseBackupSummary.
        The database backup completion date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :return: The time_backup_completed of this DatabaseBackupSummary.
        :rtype: datetime
        """
        return self._time_backup_completed

    @time_backup_completed.setter
    def time_backup_completed(self, time_backup_completed):
        """
        Sets the time_backup_completed of this DatabaseBackupSummary.
        The database backup completion date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".


        :param time_backup_completed: The time_backup_completed of this DatabaseBackupSummary.
        :type: datetime
        """
        self._time_backup_completed = time_backup_completed

    @property
    def backup_duration_in_seconds(self):
        """
        **[Required]** Gets the backup_duration_in_seconds of this DatabaseBackupSummary.
        The backup duration of the database in seconds.


        :return: The backup_duration_in_seconds of this DatabaseBackupSummary.
        :rtype: int
        """
        return self._backup_duration_in_seconds

    @backup_duration_in_seconds.setter
    def backup_duration_in_seconds(self, backup_duration_in_seconds):
        """
        Sets the backup_duration_in_seconds of this DatabaseBackupSummary.
        The backup duration of the database in seconds.


        :param backup_duration_in_seconds: The backup_duration_in_seconds of this DatabaseBackupSummary.
        :type: int
        """
        self._backup_duration_in_seconds = backup_duration_in_seconds

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this DatabaseBackupSummary.
        The backup type of the database (FULL/INCREMENTAL).


        :return: The backup_type of this DatabaseBackupSummary.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this DatabaseBackupSummary.
        The backup type of the database (FULL/INCREMENTAL).


        :param backup_type: The backup_type of this DatabaseBackupSummary.
        :type: str
        """
        self._backup_type = backup_type

    @property
    def backup_destination(self):
        """
        **[Required]** Gets the backup_destination of this DatabaseBackupSummary.
        The backup destination of the database.

        Allowed values for this property are: "DISK", "TAPE", "NFS", "LOCAL", "DBRS", "OBJECT_STORE", "RECOVERY_APPLIANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_destination of this DatabaseBackupSummary.
        :rtype: str
        """
        return self._backup_destination

    @backup_destination.setter
    def backup_destination(self, backup_destination):
        """
        Sets the backup_destination of this DatabaseBackupSummary.
        The backup destination of the database.


        :param backup_destination: The backup_destination of this DatabaseBackupSummary.
        :type: str
        """
        allowed_values = ["DISK", "TAPE", "NFS", "LOCAL", "DBRS", "OBJECT_STORE", "RECOVERY_APPLIANCE"]
        if not value_allowed_none_or_none_sentinel(backup_destination, allowed_values):
            backup_destination = 'UNKNOWN_ENUM_VALUE'
        self._backup_destination = backup_destination

    @property
    def backup_size_in_gbs(self):
        """
        **[Required]** Gets the backup_size_in_gbs of this DatabaseBackupSummary.
        The backup size of the database.


        :return: The backup_size_in_gbs of this DatabaseBackupSummary.
        :rtype: float
        """
        return self._backup_size_in_gbs

    @backup_size_in_gbs.setter
    def backup_size_in_gbs(self, backup_size_in_gbs):
        """
        Sets the backup_size_in_gbs of this DatabaseBackupSummary.
        The backup size of the database.


        :param backup_size_in_gbs: The backup_size_in_gbs of this DatabaseBackupSummary.
        :type: float
        """
        self._backup_size_in_gbs = backup_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
