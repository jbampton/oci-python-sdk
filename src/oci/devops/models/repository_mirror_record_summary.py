# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryMirrorRecordSummary(object):
    """
    Object containing information about a mirror record.
    """

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecordSummary.
    #: This constant has a value of "NONE"
    MIRROR_STATUS_NONE = "NONE"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecordSummary.
    #: This constant has a value of "QUEUED"
    MIRROR_STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecordSummary.
    #: This constant has a value of "RUNNING"
    MIRROR_STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecordSummary.
    #: This constant has a value of "PASSED"
    MIRROR_STATUS_PASSED = "PASSED"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecordSummary.
    #: This constant has a value of "FAILED"
    MIRROR_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryMirrorRecordSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mirror_status:
            The value to assign to the mirror_status property of this RepositoryMirrorRecordSummary.
            Allowed values for this property are: "NONE", "QUEUED", "RUNNING", "PASSED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mirror_status: str

        :param work_request_id:
            The value to assign to the work_request_id property of this RepositoryMirrorRecordSummary.
        :type work_request_id: str

        :param time_enqueued:
            The value to assign to the time_enqueued property of this RepositoryMirrorRecordSummary.
        :type time_enqueued: datetime

        :param time_started:
            The value to assign to the time_started property of this RepositoryMirrorRecordSummary.
        :type time_started: datetime

        :param time_completed:
            The value to assign to the time_completed property of this RepositoryMirrorRecordSummary.
        :type time_completed: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryMirrorRecordSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryMirrorRecordSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RepositoryMirrorRecordSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'mirror_status': 'str',
            'work_request_id': 'str',
            'time_enqueued': 'datetime',
            'time_started': 'datetime',
            'time_completed': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'mirror_status': 'mirrorStatus',
            'work_request_id': 'workRequestId',
            'time_enqueued': 'timeEnqueued',
            'time_started': 'timeStarted',
            'time_completed': 'timeCompleted',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._mirror_status = None
        self._work_request_id = None
        self._time_enqueued = None
        self._time_started = None
        self._time_completed = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def mirror_status(self):
        """
        **[Required]** Gets the mirror_status of this RepositoryMirrorRecordSummary.
        Mirror status of current mirror entry.
        QUEUED - Mirroring Queued
        RUNNING - Mirroring is Running
        PASSED - Mirroring Passed
        FAILED - Mirroring Failed

        Allowed values for this property are: "NONE", "QUEUED", "RUNNING", "PASSED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mirror_status of this RepositoryMirrorRecordSummary.
        :rtype: str
        """
        return self._mirror_status

    @mirror_status.setter
    def mirror_status(self, mirror_status):
        """
        Sets the mirror_status of this RepositoryMirrorRecordSummary.
        Mirror status of current mirror entry.
        QUEUED - Mirroring Queued
        RUNNING - Mirroring is Running
        PASSED - Mirroring Passed
        FAILED - Mirroring Failed


        :param mirror_status: The mirror_status of this RepositoryMirrorRecordSummary.
        :type: str
        """
        allowed_values = ["NONE", "QUEUED", "RUNNING", "PASSED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(mirror_status, allowed_values):
            mirror_status = 'UNKNOWN_ENUM_VALUE'
        self._mirror_status = mirror_status

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this RepositoryMirrorRecordSummary.
        Workrequest ID to track current mirror operation.


        :return: The work_request_id of this RepositoryMirrorRecordSummary.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this RepositoryMirrorRecordSummary.
        Workrequest ID to track current mirror operation.


        :param work_request_id: The work_request_id of this RepositoryMirrorRecordSummary.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def time_enqueued(self):
        """
        Gets the time_enqueued of this RepositoryMirrorRecordSummary.
        The time to enqueue a mirror operation.


        :return: The time_enqueued of this RepositoryMirrorRecordSummary.
        :rtype: datetime
        """
        return self._time_enqueued

    @time_enqueued.setter
    def time_enqueued(self, time_enqueued):
        """
        Sets the time_enqueued of this RepositoryMirrorRecordSummary.
        The time to enqueue a mirror operation.


        :param time_enqueued: The time_enqueued of this RepositoryMirrorRecordSummary.
        :type: datetime
        """
        self._time_enqueued = time_enqueued

    @property
    def time_started(self):
        """
        Gets the time_started of this RepositoryMirrorRecordSummary.
        The time to start a mirror operation.


        :return: The time_started of this RepositoryMirrorRecordSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RepositoryMirrorRecordSummary.
        The time to start a mirror operation.


        :param time_started: The time_started of this RepositoryMirrorRecordSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this RepositoryMirrorRecordSummary.
        The time to complete a mirror operation.


        :return: The time_completed of this RepositoryMirrorRecordSummary.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this RepositoryMirrorRecordSummary.
        The time to complete a mirror operation.


        :param time_completed: The time_completed of this RepositoryMirrorRecordSummary.
        :type: datetime
        """
        self._time_completed = time_completed

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositoryMirrorRecordSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositoryMirrorRecordSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositoryMirrorRecordSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositoryMirrorRecordSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositoryMirrorRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositoryMirrorRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositoryMirrorRecordSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositoryMirrorRecordSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RepositoryMirrorRecordSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this RepositoryMirrorRecordSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RepositoryMirrorRecordSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this RepositoryMirrorRecordSummary.
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
