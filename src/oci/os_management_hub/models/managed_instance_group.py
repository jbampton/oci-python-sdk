# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroup(object):
    """
    An object that defines the managed instance group.
    """

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagedInstanceGroup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a ManagedInstanceGroup.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the arch_type property of a ManagedInstanceGroup.
    #: This constant has a value of "I386"
    ARCH_TYPE_I386 = "I386"

    #: A constant which can be used with the vendor_name property of a ManagedInstanceGroup.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the vendor_name property of a ManagedInstanceGroup.
    #: This constant has a value of "MICROSOFT"
    VENDOR_NAME_MICROSOFT = "MICROSOFT"

    #: A constant which can be used with the location property of a ManagedInstanceGroup.
    #: This constant has a value of "ON_PREMISE"
    LOCATION_ON_PREMISE = "ON_PREMISE"

    #: A constant which can be used with the location property of a ManagedInstanceGroup.
    #: This constant has a value of "OCI_COMPUTE"
    LOCATION_OCI_COMPUTE = "OCI_COMPUTE"

    #: A constant which can be used with the location property of a ManagedInstanceGroup.
    #: This constant has a value of "AZURE"
    LOCATION_AZURE = "AZURE"

    #: A constant which can be used with the location property of a ManagedInstanceGroup.
    #: This constant has a value of "EC2"
    LOCATION_EC2 = "EC2"

    #: A constant which can be used with the location property of a ManagedInstanceGroup.
    #: This constant has a value of "GCP"
    LOCATION_GCP = "GCP"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedInstanceGroup.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedInstanceGroup.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ManagedInstanceGroup.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagedInstanceGroup.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this ManagedInstanceGroup.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this ManagedInstanceGroup.
        :type time_modified: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagedInstanceGroup.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param os_family:
            The value to assign to the os_family property of this ManagedInstanceGroup.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this ManagedInstanceGroup.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this ManagedInstanceGroup.
            Allowed values for this property are: "ORACLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        :param software_source_ids:
            The value to assign to the software_source_ids property of this ManagedInstanceGroup.
        :type software_source_ids: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param software_sources:
            The value to assign to the software_sources property of this ManagedInstanceGroup.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param managed_instance_ids:
            The value to assign to the managed_instance_ids property of this ManagedInstanceGroup.
        :type managed_instance_ids: list[str]

        :param managed_instance_count:
            The value to assign to the managed_instance_count property of this ManagedInstanceGroup.
        :type managed_instance_count: int

        :param location:
            The value to assign to the location property of this ManagedInstanceGroup.
            Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type location: str

        :param pending_job_count:
            The value to assign to the pending_job_count property of this ManagedInstanceGroup.
        :type pending_job_count: int

        :param notification_topic_id:
            The value to assign to the notification_topic_id property of this ManagedInstanceGroup.
        :type notification_topic_id: str

        :param autonomous_settings:
            The value to assign to the autonomous_settings property of this ManagedInstanceGroup.
        :type autonomous_settings: oci.os_management_hub.models.AutonomousSettings

        :param is_managed_by_autonomous_linux:
            The value to assign to the is_managed_by_autonomous_linux property of this ManagedInstanceGroup.
        :type is_managed_by_autonomous_linux: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ManagedInstanceGroup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ManagedInstanceGroup.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ManagedInstanceGroup.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'lifecycle_state': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'vendor_name': 'str',
            'software_source_ids': 'list[SoftwareSourceDetails]',
            'software_sources': 'list[SoftwareSourceDetails]',
            'managed_instance_ids': 'list[str]',
            'managed_instance_count': 'int',
            'location': 'str',
            'pending_job_count': 'int',
            'notification_topic_id': 'str',
            'autonomous_settings': 'AutonomousSettings',
            'is_managed_by_autonomous_linux': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'lifecycle_state': 'lifecycleState',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'vendor_name': 'vendorName',
            'software_source_ids': 'softwareSourceIds',
            'software_sources': 'softwareSources',
            'managed_instance_ids': 'managedInstanceIds',
            'managed_instance_count': 'managedInstanceCount',
            'location': 'location',
            'pending_job_count': 'pendingJobCount',
            'notification_topic_id': 'notificationTopicId',
            'autonomous_settings': 'autonomousSettings',
            'is_managed_by_autonomous_linux': 'isManagedByAutonomousLinux',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._time_modified = None
        self._lifecycle_state = None
        self._os_family = None
        self._arch_type = None
        self._vendor_name = None
        self._software_source_ids = None
        self._software_sources = None
        self._managed_instance_ids = None
        self._managed_instance_count = None
        self._location = None
        self._pending_job_count = None
        self._notification_topic_id = None
        self._autonomous_settings = None
        self._is_managed_by_autonomous_linux = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedInstanceGroup.
        The `OCID`__ of the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedInstanceGroup.
        The `OCID`__ of the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ManagedInstanceGroup.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedInstanceGroup.
        The `OCID`__ of the compartment that contains the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedInstanceGroup.
        The `OCID`__ of the compartment that contains the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ManagedInstanceGroup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this ManagedInstanceGroup.
        A user-friendly name for the managed instance group.


        :return: The display_name of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagedInstanceGroup.
        A user-friendly name for the managed instance group.


        :param display_name: The display_name of this ManagedInstanceGroup.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagedInstanceGroup.
        User-specified information about the managed instance group.


        :return: The description of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagedInstanceGroup.
        User-specified information about the managed instance group.


        :param description: The description of this ManagedInstanceGroup.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this ManagedInstanceGroup.
        The time the managed instance group was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ManagedInstanceGroup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedInstanceGroup.
        The time the managed instance group was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ManagedInstanceGroup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ManagedInstanceGroup.
        The time the managed instance group was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this ManagedInstanceGroup.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ManagedInstanceGroup.
        The time the managed instance group was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this ManagedInstanceGroup.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ManagedInstanceGroup.
        The current state of the managed instance group.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagedInstanceGroup.
        The current state of the managed instance group.


        :param lifecycle_state: The lifecycle_state of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def os_family(self):
        """
        Gets the os_family of this ManagedInstanceGroup.
        The operating system type of the instances in the managed instance group.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ManagedInstanceGroup.
        The operating system type of the instances in the managed instance group.


        :param os_family: The os_family of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        Gets the arch_type of this ManagedInstanceGroup.
        The CPU architecture of the instances in the managed instance group.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this ManagedInstanceGroup.
        The CPU architecture of the instances in the managed instance group.


        :param arch_type: The arch_type of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this ManagedInstanceGroup.
        The vendor of the operating system used by the managed instances in the group.

        Allowed values for this property are: "ORACLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this ManagedInstanceGroup.
        The vendor of the operating system used by the managed instances in the group.


        :param vendor_name: The vendor_name of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["ORACLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    @property
    def software_source_ids(self):
        """
        Gets the software_source_ids of this ManagedInstanceGroup.
        The list of software source `OCIDs`__ that the managed instance group will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_ids of this ManagedInstanceGroup.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_source_ids

    @software_source_ids.setter
    def software_source_ids(self, software_source_ids):
        """
        Sets the software_source_ids of this ManagedInstanceGroup.
        The list of software source `OCIDs`__ that the managed instance group will use.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_ids: The software_source_ids of this ManagedInstanceGroup.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_source_ids = software_source_ids

    @property
    def software_sources(self):
        """
        Gets the software_sources of this ManagedInstanceGroup.
        The list of software sources that the managed instance group will use.


        :return: The software_sources of this ManagedInstanceGroup.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this ManagedInstanceGroup.
        The list of software sources that the managed instance group will use.


        :param software_sources: The software_sources of this ManagedInstanceGroup.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def managed_instance_ids(self):
        """
        Gets the managed_instance_ids of this ManagedInstanceGroup.
        The list of managed instance `OCIDs`__ attached to the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The managed_instance_ids of this ManagedInstanceGroup.
        :rtype: list[str]
        """
        return self._managed_instance_ids

    @managed_instance_ids.setter
    def managed_instance_ids(self, managed_instance_ids):
        """
        Sets the managed_instance_ids of this ManagedInstanceGroup.
        The list of managed instance `OCIDs`__ attached to the managed instance group.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param managed_instance_ids: The managed_instance_ids of this ManagedInstanceGroup.
        :type: list[str]
        """
        self._managed_instance_ids = managed_instance_ids

    @property
    def managed_instance_count(self):
        """
        Gets the managed_instance_count of this ManagedInstanceGroup.
        The number of managed instances in the group.


        :return: The managed_instance_count of this ManagedInstanceGroup.
        :rtype: int
        """
        return self._managed_instance_count

    @managed_instance_count.setter
    def managed_instance_count(self, managed_instance_count):
        """
        Sets the managed_instance_count of this ManagedInstanceGroup.
        The number of managed instances in the group.


        :param managed_instance_count: The managed_instance_count of this ManagedInstanceGroup.
        :type: int
        """
        self._managed_instance_count = managed_instance_count

    @property
    def location(self):
        """
        Gets the location of this ManagedInstanceGroup.
        The location of managed instances attached to the group.

        Allowed values for this property are: "ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The location of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this ManagedInstanceGroup.
        The location of managed instances attached to the group.


        :param location: The location of this ManagedInstanceGroup.
        :type: str
        """
        allowed_values = ["ON_PREMISE", "OCI_COMPUTE", "AZURE", "EC2", "GCP"]
        if not value_allowed_none_or_none_sentinel(location, allowed_values):
            location = 'UNKNOWN_ENUM_VALUE'
        self._location = location

    @property
    def pending_job_count(self):
        """
        Gets the pending_job_count of this ManagedInstanceGroup.
        The number of scheduled jobs pending against the managed instance group.


        :return: The pending_job_count of this ManagedInstanceGroup.
        :rtype: int
        """
        return self._pending_job_count

    @pending_job_count.setter
    def pending_job_count(self, pending_job_count):
        """
        Sets the pending_job_count of this ManagedInstanceGroup.
        The number of scheduled jobs pending against the managed instance group.


        :param pending_job_count: The pending_job_count of this ManagedInstanceGroup.
        :type: int
        """
        self._pending_job_count = pending_job_count

    @property
    def notification_topic_id(self):
        """
        Gets the notification_topic_id of this ManagedInstanceGroup.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The notification_topic_id of this ManagedInstanceGroup.
        :rtype: str
        """
        return self._notification_topic_id

    @notification_topic_id.setter
    def notification_topic_id(self, notification_topic_id):
        """
        Sets the notification_topic_id of this ManagedInstanceGroup.
        The `OCID`__ for the Oracle Notifications service (ONS) topic. ONS is the channel used to send notifications to the customer.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param notification_topic_id: The notification_topic_id of this ManagedInstanceGroup.
        :type: str
        """
        self._notification_topic_id = notification_topic_id

    @property
    def autonomous_settings(self):
        """
        Gets the autonomous_settings of this ManagedInstanceGroup.

        :return: The autonomous_settings of this ManagedInstanceGroup.
        :rtype: oci.os_management_hub.models.AutonomousSettings
        """
        return self._autonomous_settings

    @autonomous_settings.setter
    def autonomous_settings(self, autonomous_settings):
        """
        Sets the autonomous_settings of this ManagedInstanceGroup.

        :param autonomous_settings: The autonomous_settings of this ManagedInstanceGroup.
        :type: oci.os_management_hub.models.AutonomousSettings
        """
        self._autonomous_settings = autonomous_settings

    @property
    def is_managed_by_autonomous_linux(self):
        """
        Gets the is_managed_by_autonomous_linux of this ManagedInstanceGroup.
        Indicates whether the Autonomous Linux service manages the group.


        :return: The is_managed_by_autonomous_linux of this ManagedInstanceGroup.
        :rtype: bool
        """
        return self._is_managed_by_autonomous_linux

    @is_managed_by_autonomous_linux.setter
    def is_managed_by_autonomous_linux(self, is_managed_by_autonomous_linux):
        """
        Sets the is_managed_by_autonomous_linux of this ManagedInstanceGroup.
        Indicates whether the Autonomous Linux service manages the group.


        :param is_managed_by_autonomous_linux: The is_managed_by_autonomous_linux of this ManagedInstanceGroup.
        :type: bool
        """
        self._is_managed_by_autonomous_linux = is_managed_by_autonomous_linux

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ManagedInstanceGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ManagedInstanceGroup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ManagedInstanceGroup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ManagedInstanceGroup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ManagedInstanceGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ManagedInstanceGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ManagedInstanceGroup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ManagedInstanceGroup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ManagedInstanceGroup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this ManagedInstanceGroup.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ManagedInstanceGroup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this ManagedInstanceGroup.
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
