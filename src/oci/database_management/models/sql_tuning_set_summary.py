# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningSetSummary(object):
    """
    The summary information of a SQL tuning set.
    """

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "RETRY_SCHEDULED"
    STATUS_RETRY_SCHEDULED = "RETRY_SCHEDULED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "SCHEDULED"
    STATUS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "BLOCKED"
    STATUS_BLOCKED = "BLOCKED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "RUNNING"
    STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "BROKEN"
    STATUS_BROKEN = "BROKEN"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "REMOTE"
    STATUS_REMOTE = "REMOTE"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "RESOURCE_UNAVAILABLE"
    STATUS_RESOURCE_UNAVAILABLE = "RESOURCE_UNAVAILABLE"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a SqlTuningSetSummary.
    #: This constant has a value of "CHAIN_STALLED"
    STATUS_CHAIN_STALLED = "CHAIN_STALLED"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningSetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SqlTuningSetSummary.
        :type name: str

        :param owner:
            The value to assign to the owner property of this SqlTuningSetSummary.
        :type owner: str

        :param description:
            The value to assign to the description property of this SqlTuningSetSummary.
        :type description: str

        :param statement_counts:
            The value to assign to the statement_counts property of this SqlTuningSetSummary.
        :type statement_counts: int

        :param id:
            The value to assign to the id property of this SqlTuningSetSummary.
        :type id: int

        :param time_created:
            The value to assign to the time_created property of this SqlTuningSetSummary.
        :type time_created: datetime

        :param time_last_modified:
            The value to assign to the time_last_modified property of this SqlTuningSetSummary.
        :type time_last_modified: datetime

        :param status:
            The value to assign to the status property of this SqlTuningSetSummary.
            Allowed values for this property are: "DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param scheduled_job_name:
            The value to assign to the scheduled_job_name property of this SqlTuningSetSummary.
        :type scheduled_job_name: str

        :param error_message:
            The value to assign to the error_message property of this SqlTuningSetSummary.
        :type error_message: str

        """
        self.swagger_types = {
            'name': 'str',
            'owner': 'str',
            'description': 'str',
            'statement_counts': 'int',
            'id': 'int',
            'time_created': 'datetime',
            'time_last_modified': 'datetime',
            'status': 'str',
            'scheduled_job_name': 'str',
            'error_message': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'owner': 'owner',
            'description': 'description',
            'statement_counts': 'statementCounts',
            'id': 'id',
            'time_created': 'timeCreated',
            'time_last_modified': 'timeLastModified',
            'status': 'status',
            'scheduled_job_name': 'scheduledJobName',
            'error_message': 'errorMessage'
        }
        self._name = None
        self._owner = None
        self._description = None
        self._statement_counts = None
        self._id = None
        self._time_created = None
        self._time_last_modified = None
        self._status = None
        self._scheduled_job_name = None
        self._error_message = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SqlTuningSetSummary.
        The name of the SQL tuning set.


        :return: The name of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningSetSummary.
        The name of the SQL tuning set.


        :param name: The name of this SqlTuningSetSummary.
        :type: str
        """
        self._name = name

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this SqlTuningSetSummary.
        The owner of the SQL tuning set.


        :return: The owner of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningSetSummary.
        The owner of the SQL tuning set.


        :param owner: The owner of this SqlTuningSetSummary.
        :type: str
        """
        self._owner = owner

    @property
    def description(self):
        """
        Gets the description of this SqlTuningSetSummary.
        The description of the SQL tuning set.


        :return: The description of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlTuningSetSummary.
        The description of the SQL tuning set.


        :param description: The description of this SqlTuningSetSummary.
        :type: str
        """
        self._description = description

    @property
    def statement_counts(self):
        """
        Gets the statement_counts of this SqlTuningSetSummary.
        The number of SQL statements in the SQL tuning set.


        :return: The statement_counts of this SqlTuningSetSummary.
        :rtype: int
        """
        return self._statement_counts

    @statement_counts.setter
    def statement_counts(self, statement_counts):
        """
        Sets the statement_counts of this SqlTuningSetSummary.
        The number of SQL statements in the SQL tuning set.


        :param statement_counts: The statement_counts of this SqlTuningSetSummary.
        :type: int
        """
        self._statement_counts = statement_counts

    @property
    def id(self):
        """
        Gets the id of this SqlTuningSetSummary.
        The unique Sql tuning set identifier. This is not OCID.


        :return: The id of this SqlTuningSetSummary.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlTuningSetSummary.
        The unique Sql tuning set identifier. This is not OCID.


        :param id: The id of this SqlTuningSetSummary.
        :type: int
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this SqlTuningSetSummary.
        The created time of the Sql tuning set.


        :return: The time_created of this SqlTuningSetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlTuningSetSummary.
        The created time of the Sql tuning set.


        :param time_created: The time_created of this SqlTuningSetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_modified(self):
        """
        Gets the time_last_modified of this SqlTuningSetSummary.
        Last modified time of the Sql tuning set.


        :return: The time_last_modified of this SqlTuningSetSummary.
        :rtype: datetime
        """
        return self._time_last_modified

    @time_last_modified.setter
    def time_last_modified(self, time_last_modified):
        """
        Sets the time_last_modified of this SqlTuningSetSummary.
        Last modified time of the Sql tuning set.


        :param time_last_modified: The time_last_modified of this SqlTuningSetSummary.
        :type: datetime
        """
        self._time_last_modified = time_last_modified

    @property
    def status(self):
        """
        Gets the status of this SqlTuningSetSummary.
        Current status of the Sql tuning set.

        Allowed values for this property are: "DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SqlTuningSetSummary.
        Current status of the Sql tuning set.


        :param status: The status of this SqlTuningSetSummary.
        :type: str
        """
        allowed_values = ["DISABLED", "RETRY_SCHEDULED", "SCHEDULED", "BLOCKED", "RUNNING", "COMPLETED", "BROKEN", "FAILED", "REMOTE", "RESOURCE_UNAVAILABLE", "SUCCEEDED", "CHAIN_STALLED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def scheduled_job_name(self):
        """
        Gets the scheduled_job_name of this SqlTuningSetSummary.
        Name of the Sql tuning set scheduler job.


        :return: The scheduled_job_name of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._scheduled_job_name

    @scheduled_job_name.setter
    def scheduled_job_name(self, scheduled_job_name):
        """
        Sets the scheduled_job_name of this SqlTuningSetSummary.
        Name of the Sql tuning set scheduler job.


        :param scheduled_job_name: The scheduled_job_name of this SqlTuningSetSummary.
        :type: str
        """
        self._scheduled_job_name = scheduled_job_name

    @property
    def error_message(self):
        """
        Gets the error_message of this SqlTuningSetSummary.
        Latest execution error of the plsql that was submitted as a scheduler job.


        :return: The error_message of this SqlTuningSetSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this SqlTuningSetSummary.
        Latest execution error of the plsql that was submitted as a scheduler job.


        :param error_message: The error_message of this SqlTuningSetSummary.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
