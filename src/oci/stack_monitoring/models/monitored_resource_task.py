# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceTask(object):
    """
    The request details for importing resources from Telemetry.
    """

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceTask.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceTask object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MonitoredResourceTask.
        :type id: str

        :param name:
            The value to assign to the name property of this MonitoredResourceTask.
        :type name: str

        :param type:
            The value to assign to the type property of this MonitoredResourceTask.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredResourceTask.
        :type compartment_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MonitoredResourceTask.
        :type tenant_id: str

        :param task_details:
            The value to assign to the task_details property of this MonitoredResourceTask.
        :type task_details: oci.stack_monitoring.models.MonitoredResourceTaskDetails

        :param work_request_ids:
            The value to assign to the work_request_ids property of this MonitoredResourceTask.
        :type work_request_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this MonitoredResourceTask.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoredResourceTask.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredResourceTask.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResourceTask.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResourceTask.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResourceTask.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'tenant_id': 'str',
            'task_details': 'MonitoredResourceTaskDetails',
            'work_request_ids': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'tenant_id': 'tenantId',
            'task_details': 'taskDetails',
            'work_request_ids': 'workRequestIds',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._name = None
        self._type = None
        self._compartment_id = None
        self._tenant_id = None
        self._task_details = None
        self._work_request_ids = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MonitoredResourceTask.
        Task identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MonitoredResourceTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MonitoredResourceTask.
        Task identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MonitoredResourceTask.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MonitoredResourceTask.
        Name of the task.


        :return: The name of this MonitoredResourceTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResourceTask.
        Name of the task.


        :param name: The name of this MonitoredResourceTask.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this MonitoredResourceTask.
        Type of the task.


        :return: The type of this MonitoredResourceTask.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MonitoredResourceTask.
        Type of the task.


        :param type: The type of this MonitoredResourceTask.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredResourceTask.
        The `OCID`__ of the compartment identifier.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredResourceTask.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredResourceTask.
        The `OCID`__ of the compartment identifier.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredResourceTask.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this MonitoredResourceTask.
        The `OCID`__ of the tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this MonitoredResourceTask.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MonitoredResourceTask.
        The `OCID`__ of the tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this MonitoredResourceTask.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def task_details(self):
        """
        **[Required]** Gets the task_details of this MonitoredResourceTask.

        :return: The task_details of this MonitoredResourceTask.
        :rtype: oci.stack_monitoring.models.MonitoredResourceTaskDetails
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        """
        Sets the task_details of this MonitoredResourceTask.

        :param task_details: The task_details of this MonitoredResourceTask.
        :type: oci.stack_monitoring.models.MonitoredResourceTaskDetails
        """
        self._task_details = task_details

    @property
    def work_request_ids(self):
        """
        Gets the work_request_ids of this MonitoredResourceTask.
        Identifiers `OCID`__ for work requests submitted for this task.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The work_request_ids of this MonitoredResourceTask.
        :rtype: list[str]
        """
        return self._work_request_ids

    @work_request_ids.setter
    def work_request_ids(self, work_request_ids):
        """
        Sets the work_request_ids of this MonitoredResourceTask.
        Identifiers `OCID`__ for work requests submitted for this task.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param work_request_ids: The work_request_ids of this MonitoredResourceTask.
        :type: list[str]
        """
        self._work_request_ids = work_request_ids

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredResourceTask.
        The date and time when the stack monitoring resource task was created, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this MonitoredResourceTask.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredResourceTask.
        The date and time when the stack monitoring resource task was created, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this MonitoredResourceTask.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MonitoredResourceTask.
        The date and time when the stack monitoring resource task was last updated, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this MonitoredResourceTask.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoredResourceTask.
        The date and time when the stack monitoring resource task was last updated, expressed in
        `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this MonitoredResourceTask.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredResourceTask.
        The current state of the stack monitoring resource task.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredResourceTask.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredResourceTask.
        The current state of the stack monitoring resource task.


        :param lifecycle_state: The lifecycle_state of this MonitoredResourceTask.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResourceTask.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResourceTask.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResourceTask.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResourceTask.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResourceTask.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResourceTask.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResourceTask.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResourceTask.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResourceTask.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResourceTask.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResourceTask.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResourceTask.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
