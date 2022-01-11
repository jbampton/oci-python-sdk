# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduledTask(object):
    """
    Log analytics scheduled task resource.
    """

    #: A constant which can be used with the kind property of a ScheduledTask.
    #: This constant has a value of "ACCELERATION"
    KIND_ACCELERATION = "ACCELERATION"

    #: A constant which can be used with the kind property of a ScheduledTask.
    #: This constant has a value of "STANDARD"
    KIND_STANDARD = "STANDARD"

    #: A constant which can be used with the task_type property of a ScheduledTask.
    #: This constant has a value of "SAVED_SEARCH"
    TASK_TYPE_SAVED_SEARCH = "SAVED_SEARCH"

    #: A constant which can be used with the task_type property of a ScheduledTask.
    #: This constant has a value of "ACCELERATION"
    TASK_TYPE_ACCELERATION = "ACCELERATION"

    #: A constant which can be used with the task_type property of a ScheduledTask.
    #: This constant has a value of "PURGE"
    TASK_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the task_type property of a ScheduledTask.
    #: This constant has a value of "ACCELERATION_MAINTENANCE"
    TASK_TYPE_ACCELERATION_MAINTENANCE = "ACCELERATION_MAINTENANCE"

    #: A constant which can be used with the task_status property of a ScheduledTask.
    #: This constant has a value of "READY"
    TASK_STATUS_READY = "READY"

    #: A constant which can be used with the task_status property of a ScheduledTask.
    #: This constant has a value of "PAUSED"
    TASK_STATUS_PAUSED = "PAUSED"

    #: A constant which can be used with the task_status property of a ScheduledTask.
    #: This constant has a value of "COMPLETED"
    TASK_STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the task_status property of a ScheduledTask.
    #: This constant has a value of "BLOCKED"
    TASK_STATUS_BLOCKED = "BLOCKED"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "METRIC_EXTRACTION_NOT_VALID"
    PAUSE_REASON_METRIC_EXTRACTION_NOT_VALID = "METRIC_EXTRACTION_NOT_VALID"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "SAVED_SEARCH_NOT_VALID"
    PAUSE_REASON_SAVED_SEARCH_NOT_VALID = "SAVED_SEARCH_NOT_VALID"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "SAVED_SEARCH_NOT_FOUND"
    PAUSE_REASON_SAVED_SEARCH_NOT_FOUND = "SAVED_SEARCH_NOT_FOUND"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "QUERY_STRING_NOT_VALID"
    PAUSE_REASON_QUERY_STRING_NOT_VALID = "QUERY_STRING_NOT_VALID"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "USER_ACTION"
    PAUSE_REASON_USER_ACTION = "USER_ACTION"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "TENANCY_LIFECYCLE"
    PAUSE_REASON_TENANCY_LIFECYCLE = "TENANCY_LIFECYCLE"

    #: A constant which can be used with the pause_reason property of a ScheduledTask.
    #: This constant has a value of "PURGE_RESOURCE_NOT_FOUND"
    PAUSE_REASON_PURGE_RESOURCE_NOT_FOUND = "PURGE_RESOURCE_NOT_FOUND"

    #: A constant which can be used with the lifecycle_state property of a ScheduledTask.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ScheduledTask.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduledTask object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.StandardTask`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this ScheduledTask.
            Allowed values for this property are: "ACCELERATION", "STANDARD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param id:
            The value to assign to the id property of this ScheduledTask.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ScheduledTask.
        :type display_name: str

        :param task_type:
            The value to assign to the task_type property of this ScheduledTask.
            Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_type: str

        :param schedules:
            The value to assign to the schedules property of this ScheduledTask.
        :type schedules: list[oci.log_analytics.models.Schedule]

        :param action:
            The value to assign to the action property of this ScheduledTask.
        :type action: oci.log_analytics.models.Action

        :param task_status:
            The value to assign to the task_status property of this ScheduledTask.
            Allowed values for this property are: "READY", "PAUSED", "COMPLETED", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_status: str

        :param pause_reason:
            The value to assign to the pause_reason property of this ScheduledTask.
            Allowed values for this property are: "METRIC_EXTRACTION_NOT_VALID", "SAVED_SEARCH_NOT_VALID", "SAVED_SEARCH_NOT_FOUND", "QUERY_STRING_NOT_VALID", "USER_ACTION", "TENANCY_LIFECYCLE", "PURGE_RESOURCE_NOT_FOUND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pause_reason: str

        :param work_request_id:
            The value to assign to the work_request_id property of this ScheduledTask.
        :type work_request_id: str

        :param num_occurrences:
            The value to assign to the num_occurrences property of this ScheduledTask.
        :type num_occurrences: int

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduledTask.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this ScheduledTask.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ScheduledTask.
        :type time_updated: datetime

        :param time_of_next_execution:
            The value to assign to the time_of_next_execution property of this ScheduledTask.
        :type time_of_next_execution: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ScheduledTask.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ScheduledTask.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ScheduledTask.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'kind': 'str',
            'id': 'str',
            'display_name': 'str',
            'task_type': 'str',
            'schedules': 'list[Schedule]',
            'action': 'Action',
            'task_status': 'str',
            'pause_reason': 'str',
            'work_request_id': 'str',
            'num_occurrences': 'int',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_of_next_execution': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'kind': 'kind',
            'id': 'id',
            'display_name': 'displayName',
            'task_type': 'taskType',
            'schedules': 'schedules',
            'action': 'action',
            'task_status': 'taskStatus',
            'pause_reason': 'pauseReason',
            'work_request_id': 'workRequestId',
            'num_occurrences': 'numOccurrences',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_of_next_execution': 'timeOfNextExecution',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._kind = None
        self._id = None
        self._display_name = None
        self._task_type = None
        self._schedules = None
        self._action = None
        self._task_status = None
        self._pause_reason = None
        self._work_request_id = None
        self._num_occurrences = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._time_of_next_execution = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'STANDARD':
            return 'StandardTask'
        else:
            return 'ScheduledTask'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this ScheduledTask.
        Discriminator.

        Allowed values for this property are: "ACCELERATION", "STANDARD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this ScheduledTask.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this ScheduledTask.
        Discriminator.


        :param kind: The kind of this ScheduledTask.
        :type: str
        """
        allowed_values = ["ACCELERATION", "STANDARD"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ScheduledTask.
        The `OCID`__ of the data plane resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ScheduledTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ScheduledTask.
        The `OCID`__ of the data plane resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ScheduledTask.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ScheduledTask.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :return: The display_name of this ScheduledTask.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduledTask.
        A user-friendly name that is changeable and that does not have to be unique.
        Format: a leading alphanumeric, followed by zero or more
        alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
        No trailing spaces allowed.


        :param display_name: The display_name of this ScheduledTask.
        :type: str
        """
        self._display_name = display_name

    @property
    def task_type(self):
        """
        **[Required]** Gets the task_type of this ScheduledTask.
        Task type.

        Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_type of this ScheduledTask.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this ScheduledTask.
        Task type.


        :param task_type: The task_type of this ScheduledTask.
        :type: str
        """
        allowed_values = ["SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"]
        if not value_allowed_none_or_none_sentinel(task_type, allowed_values):
            task_type = 'UNKNOWN_ENUM_VALUE'
        self._task_type = task_type

    @property
    def schedules(self):
        """
        **[Required]** Gets the schedules of this ScheduledTask.
        Schedules.


        :return: The schedules of this ScheduledTask.
        :rtype: list[oci.log_analytics.models.Schedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this ScheduledTask.
        Schedules.


        :param schedules: The schedules of this ScheduledTask.
        :type: list[oci.log_analytics.models.Schedule]
        """
        self._schedules = schedules

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ScheduledTask.

        :return: The action of this ScheduledTask.
        :rtype: oci.log_analytics.models.Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ScheduledTask.

        :param action: The action of this ScheduledTask.
        :type: oci.log_analytics.models.Action
        """
        self._action = action

    @property
    def task_status(self):
        """
        Gets the task_status of this ScheduledTask.
        Status of the scheduled task.

        Allowed values for this property are: "READY", "PAUSED", "COMPLETED", "BLOCKED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_status of this ScheduledTask.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """
        Sets the task_status of this ScheduledTask.
        Status of the scheduled task.


        :param task_status: The task_status of this ScheduledTask.
        :type: str
        """
        allowed_values = ["READY", "PAUSED", "COMPLETED", "BLOCKED"]
        if not value_allowed_none_or_none_sentinel(task_status, allowed_values):
            task_status = 'UNKNOWN_ENUM_VALUE'
        self._task_status = task_status

    @property
    def pause_reason(self):
        """
        Gets the pause_reason of this ScheduledTask.
        reason for taskStatus PAUSED.

        Allowed values for this property are: "METRIC_EXTRACTION_NOT_VALID", "SAVED_SEARCH_NOT_VALID", "SAVED_SEARCH_NOT_FOUND", "QUERY_STRING_NOT_VALID", "USER_ACTION", "TENANCY_LIFECYCLE", "PURGE_RESOURCE_NOT_FOUND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pause_reason of this ScheduledTask.
        :rtype: str
        """
        return self._pause_reason

    @pause_reason.setter
    def pause_reason(self, pause_reason):
        """
        Sets the pause_reason of this ScheduledTask.
        reason for taskStatus PAUSED.


        :param pause_reason: The pause_reason of this ScheduledTask.
        :type: str
        """
        allowed_values = ["METRIC_EXTRACTION_NOT_VALID", "SAVED_SEARCH_NOT_VALID", "SAVED_SEARCH_NOT_FOUND", "QUERY_STRING_NOT_VALID", "USER_ACTION", "TENANCY_LIFECYCLE", "PURGE_RESOURCE_NOT_FOUND"]
        if not value_allowed_none_or_none_sentinel(pause_reason, allowed_values):
            pause_reason = 'UNKNOWN_ENUM_VALUE'
        self._pause_reason = pause_reason

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this ScheduledTask.
        most recent Work Request Identifier `OCID]`__ for the asynchronous request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The work_request_id of this ScheduledTask.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this ScheduledTask.
        most recent Work Request Identifier `OCID]`__ for the asynchronous request.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param work_request_id: The work_request_id of this ScheduledTask.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def num_occurrences(self):
        """
        Gets the num_occurrences of this ScheduledTask.
        Number of execution occurrences.


        :return: The num_occurrences of this ScheduledTask.
        :rtype: int
        """
        return self._num_occurrences

    @num_occurrences.setter
    def num_occurrences(self, num_occurrences):
        """
        Sets the num_occurrences of this ScheduledTask.
        Number of execution occurrences.


        :param num_occurrences: The num_occurrences of this ScheduledTask.
        :type: int
        """
        self._num_occurrences = num_occurrences

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduledTask.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ScheduledTask.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduledTask.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ScheduledTask.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ScheduledTask.
        The date and time the scheduled task was created, in the format defined by RFC3339.


        :return: The time_created of this ScheduledTask.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ScheduledTask.
        The date and time the scheduled task was created, in the format defined by RFC3339.


        :param time_created: The time_created of this ScheduledTask.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ScheduledTask.
        The date and time the scheduled task was last updated, in the format defined by RFC3339.


        :return: The time_updated of this ScheduledTask.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ScheduledTask.
        The date and time the scheduled task was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this ScheduledTask.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_of_next_execution(self):
        """
        Gets the time_of_next_execution of this ScheduledTask.
        The date and time the scheduled task will execute next,
        in the format defined by RFC3339.


        :return: The time_of_next_execution of this ScheduledTask.
        :rtype: datetime
        """
        return self._time_of_next_execution

    @time_of_next_execution.setter
    def time_of_next_execution(self, time_of_next_execution):
        """
        Sets the time_of_next_execution of this ScheduledTask.
        The date and time the scheduled task will execute next,
        in the format defined by RFC3339.


        :param time_of_next_execution: The time_of_next_execution of this ScheduledTask.
        :type: datetime
        """
        self._time_of_next_execution = time_of_next_execution

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ScheduledTask.
        The current state of the scheduled task.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ScheduledTask.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ScheduledTask.
        The current state of the scheduled task.


        :param lifecycle_state: The lifecycle_state of this ScheduledTask.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ScheduledTask.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ScheduledTask.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ScheduledTask.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ScheduledTask.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ScheduledTask.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this ScheduledTask.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ScheduledTask.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this ScheduledTask.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
