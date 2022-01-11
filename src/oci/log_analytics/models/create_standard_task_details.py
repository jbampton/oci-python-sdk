# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_scheduled_task_details import CreateScheduledTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStandardTaskDetails(CreateScheduledTaskDetails):
    """
    Details for creating a scheduled task.
    The client must fully specify the details.
    Not supported for TaskType ACCELERATION.
    """

    #: A constant which can be used with the task_type property of a CreateStandardTaskDetails.
    #: This constant has a value of "SAVED_SEARCH"
    TASK_TYPE_SAVED_SEARCH = "SAVED_SEARCH"

    #: A constant which can be used with the task_type property of a CreateStandardTaskDetails.
    #: This constant has a value of "ACCELERATION"
    TASK_TYPE_ACCELERATION = "ACCELERATION"

    #: A constant which can be used with the task_type property of a CreateStandardTaskDetails.
    #: This constant has a value of "PURGE"
    TASK_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the task_type property of a CreateStandardTaskDetails.
    #: This constant has a value of "ACCELERATION_MAINTENANCE"
    TASK_TYPE_ACCELERATION_MAINTENANCE = "ACCELERATION_MAINTENANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStandardTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.CreateStandardTaskDetails.kind` attribute
        of this class is ``STANDARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this CreateStandardTaskDetails.
            Allowed values for this property are: "ACCELERATION", "STANDARD"
        :type kind: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateStandardTaskDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateStandardTaskDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateStandardTaskDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateStandardTaskDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param task_type:
            The value to assign to the task_type property of this CreateStandardTaskDetails.
            Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"
        :type task_type: str

        :param schedules:
            The value to assign to the schedules property of this CreateStandardTaskDetails.
        :type schedules: list[oci.log_analytics.models.Schedule]

        :param action:
            The value to assign to the action property of this CreateStandardTaskDetails.
        :type action: oci.log_analytics.models.Action

        """
        self.swagger_types = {
            'kind': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'task_type': 'str',
            'schedules': 'list[Schedule]',
            'action': 'Action'
        }

        self.attribute_map = {
            'kind': 'kind',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'task_type': 'taskType',
            'schedules': 'schedules',
            'action': 'action'
        }

        self._kind = None
        self._compartment_id = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._task_type = None
        self._schedules = None
        self._action = None
        self._kind = 'STANDARD'

    @property
    def task_type(self):
        """
        **[Required]** Gets the task_type of this CreateStandardTaskDetails.
        Task type.

        Allowed values for this property are: "SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"


        :return: The task_type of this CreateStandardTaskDetails.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this CreateStandardTaskDetails.
        Task type.


        :param task_type: The task_type of this CreateStandardTaskDetails.
        :type: str
        """
        allowed_values = ["SAVED_SEARCH", "ACCELERATION", "PURGE", "ACCELERATION_MAINTENANCE"]
        if not value_allowed_none_or_none_sentinel(task_type, allowed_values):
            raise ValueError(
                "Invalid value for `task_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._task_type = task_type

    @property
    def schedules(self):
        """
        **[Required]** Gets the schedules of this CreateStandardTaskDetails.
        Schedules, typically a single schedule.
        Note there may only be a single schedule for SAVED_SEARCH and PURGE scheduled tasks.


        :return: The schedules of this CreateStandardTaskDetails.
        :rtype: list[oci.log_analytics.models.Schedule]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """
        Sets the schedules of this CreateStandardTaskDetails.
        Schedules, typically a single schedule.
        Note there may only be a single schedule for SAVED_SEARCH and PURGE scheduled tasks.


        :param schedules: The schedules of this CreateStandardTaskDetails.
        :type: list[oci.log_analytics.models.Schedule]
        """
        self._schedules = schedules

    @property
    def action(self):
        """
        **[Required]** Gets the action of this CreateStandardTaskDetails.

        :return: The action of this CreateStandardTaskDetails.
        :rtype: oci.log_analytics.models.Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CreateStandardTaskDetails.

        :param action: The action of this CreateStandardTaskDetails.
        :type: oci.log_analytics.models.Action
        """
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
