# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileVersion(object):
    """
    Represents a specific version of a registration profile.
    """

    #: A constant which can be used with the profile_type property of a ProfileVersion.
    #: This constant has a value of "SOFTWARESOURCE"
    PROFILE_TYPE_SOFTWARESOURCE = "SOFTWARESOURCE"

    #: A constant which can be used with the profile_type property of a ProfileVersion.
    #: This constant has a value of "GROUP"
    PROFILE_TYPE_GROUP = "GROUP"

    #: A constant which can be used with the profile_type property of a ProfileVersion.
    #: This constant has a value of "LIFECYCLE"
    PROFILE_TYPE_LIFECYCLE = "LIFECYCLE"

    #: A constant which can be used with the profile_type property of a ProfileVersion.
    #: This constant has a value of "STATION"
    PROFILE_TYPE_STATION = "STATION"

    #: A constant which can be used with the profile_type property of a ProfileVersion.
    #: This constant has a value of "WINDOWS_STANDALONE"
    PROFILE_TYPE_WINDOWS_STANDALONE = "WINDOWS_STANDALONE"

    #: A constant which can be used with the vendor_name property of a ProfileVersion.
    #: This constant has a value of "ORACLE"
    VENDOR_NAME_ORACLE = "ORACLE"

    #: A constant which can be used with the vendor_name property of a ProfileVersion.
    #: This constant has a value of "MICROSOFT"
    VENDOR_NAME_MICROSOFT = "MICROSOFT"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "ORACLE_LINUX_9"
    OS_FAMILY_ORACLE_LINUX_9 = "ORACLE_LINUX_9"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "ORACLE_LINUX_8"
    OS_FAMILY_ORACLE_LINUX_8 = "ORACLE_LINUX_8"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "ORACLE_LINUX_7"
    OS_FAMILY_ORACLE_LINUX_7 = "ORACLE_LINUX_7"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "ORACLE_LINUX_6"
    OS_FAMILY_ORACLE_LINUX_6 = "ORACLE_LINUX_6"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "WINDOWS_SERVER_2016"
    OS_FAMILY_WINDOWS_SERVER_2016 = "WINDOWS_SERVER_2016"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "WINDOWS_SERVER_2019"
    OS_FAMILY_WINDOWS_SERVER_2019 = "WINDOWS_SERVER_2019"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "WINDOWS_SERVER_2022"
    OS_FAMILY_WINDOWS_SERVER_2022 = "WINDOWS_SERVER_2022"

    #: A constant which can be used with the os_family property of a ProfileVersion.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the arch_type property of a ProfileVersion.
    #: This constant has a value of "I386"
    ARCH_TYPE_I386 = "I386"

    #: A constant which can be used with the registration_type property of a ProfileVersion.
    #: This constant has a value of "OCI_LINUX"
    REGISTRATION_TYPE_OCI_LINUX = "OCI_LINUX"

    #: A constant which can be used with the registration_type property of a ProfileVersion.
    #: This constant has a value of "NON_OCI_LINUX"
    REGISTRATION_TYPE_NON_OCI_LINUX = "NON_OCI_LINUX"

    #: A constant which can be used with the registration_type property of a ProfileVersion.
    #: This constant has a value of "OCI_WINDOWS"
    REGISTRATION_TYPE_OCI_WINDOWS = "OCI_WINDOWS"

    #: A constant which can be used with the registration_type property of a ProfileVersion.
    #: This constant has a value of "AUTONOMOUS_LINUX"
    REGISTRATION_TYPE_AUTONOMOUS_LINUX = "AUTONOMOUS_LINUX"

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileVersion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProfileVersion.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProfileVersion.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ProfileVersion.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ProfileVersion.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this ProfileVersion.
        :type management_station_id: str

        :param software_sources:
            The value to assign to the software_sources property of this ProfileVersion.
        :type software_sources: list[oci.os_management_hub.models.SoftwareSourceDetails]

        :param managed_instance_group:
            The value to assign to the managed_instance_group property of this ProfileVersion.
        :type managed_instance_group: oci.os_management_hub.models.ManagedInstanceGroupDetails

        :param lifecycle_environment:
            The value to assign to the lifecycle_environment property of this ProfileVersion.
        :type lifecycle_environment: oci.os_management_hub.models.LifecycleEnvironmentDetails

        :param lifecycle_stage:
            The value to assign to the lifecycle_stage property of this ProfileVersion.
        :type lifecycle_stage: oci.os_management_hub.models.LifecycleStageDetails

        :param profile_type:
            The value to assign to the profile_type property of this ProfileVersion.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION", "WINDOWS_STANDALONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type profile_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this ProfileVersion.
            Allowed values for this property are: "ORACLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type vendor_name: str

        :param os_family:
            The value to assign to the os_family property of this ProfileVersion.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this ProfileVersion.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param time_created:
            The value to assign to the time_created property of this ProfileVersion.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this ProfileVersion.
        :type time_modified: datetime

        :param profile_version:
            The value to assign to the profile_version property of this ProfileVersion.
        :type profile_version: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProfileVersion.
        :type lifecycle_state: str

        :param registration_type:
            The value to assign to the registration_type property of this ProfileVersion.
            Allowed values for this property are: "OCI_LINUX", "NON_OCI_LINUX", "OCI_WINDOWS", "AUTONOMOUS_LINUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type registration_type: str

        :param is_default_profile:
            The value to assign to the is_default_profile property of this ProfileVersion.
        :type is_default_profile: bool

        :param is_service_provided_profile:
            The value to assign to the is_service_provided_profile property of this ProfileVersion.
        :type is_service_provided_profile: bool

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'software_sources': 'list[SoftwareSourceDetails]',
            'managed_instance_group': 'ManagedInstanceGroupDetails',
            'lifecycle_environment': 'LifecycleEnvironmentDetails',
            'lifecycle_stage': 'LifecycleStageDetails',
            'profile_type': 'str',
            'vendor_name': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'profile_version': 'str',
            'lifecycle_state': 'str',
            'registration_type': 'str',
            'is_default_profile': 'bool',
            'is_service_provided_profile': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'software_sources': 'softwareSources',
            'managed_instance_group': 'managedInstanceGroup',
            'lifecycle_environment': 'lifecycleEnvironment',
            'lifecycle_stage': 'lifecycleStage',
            'profile_type': 'profileType',
            'vendor_name': 'vendorName',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'profile_version': 'profileVersion',
            'lifecycle_state': 'lifecycleState',
            'registration_type': 'registrationType',
            'is_default_profile': 'isDefaultProfile',
            'is_service_provided_profile': 'isServiceProvidedProfile'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._management_station_id = None
        self._software_sources = None
        self._managed_instance_group = None
        self._lifecycle_environment = None
        self._lifecycle_stage = None
        self._profile_type = None
        self._vendor_name = None
        self._os_family = None
        self._arch_type = None
        self._time_created = None
        self._time_modified = None
        self._profile_version = None
        self._lifecycle_state = None
        self._registration_type = None
        self._is_default_profile = None
        self._is_service_provided_profile = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProfileVersion.
        The `OCID`__ of the registration profile.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ProfileVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProfileVersion.
        The `OCID`__ of the registration profile.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ProfileVersion.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProfileVersion.
        The `OCID`__ of the compartment that contains the registration profile.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ProfileVersion.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProfileVersion.
        The `OCID`__ of the compartment that contains the registration profile.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ProfileVersion.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ProfileVersion.
        A user-friendly name for the profile.


        :return: The display_name of this ProfileVersion.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProfileVersion.
        A user-friendly name for the profile.


        :param display_name: The display_name of this ProfileVersion.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ProfileVersion.
        The description of the registration profile.


        :return: The description of this ProfileVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProfileVersion.
        The description of the registration profile.


        :param description: The description of this ProfileVersion.
        :type: str
        """
        self._description = description

    @property
    def management_station_id(self):
        """
        Gets the management_station_id of this ProfileVersion.
        The `OCID`__ of the management station to associate with an
        instance once registered. Management stations are only used with non-OCI instances.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The management_station_id of this ProfileVersion.
        :rtype: str
        """
        return self._management_station_id

    @management_station_id.setter
    def management_station_id(self, management_station_id):
        """
        Sets the management_station_id of this ProfileVersion.
        The `OCID`__ of the management station to associate with an
        instance once registered. Management stations are only used with non-OCI instances.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param management_station_id: The management_station_id of this ProfileVersion.
        :type: str
        """
        self._management_station_id = management_station_id

    @property
    def software_sources(self):
        """
        Gets the software_sources of this ProfileVersion.
        The list of software sources that the registration profile will use.


        :return: The software_sources of this ProfileVersion.
        :rtype: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this ProfileVersion.
        The list of software sources that the registration profile will use.


        :param software_sources: The software_sources of this ProfileVersion.
        :type: list[oci.os_management_hub.models.SoftwareSourceDetails]
        """
        self._software_sources = software_sources

    @property
    def managed_instance_group(self):
        """
        Gets the managed_instance_group of this ProfileVersion.

        :return: The managed_instance_group of this ProfileVersion.
        :rtype: oci.os_management_hub.models.ManagedInstanceGroupDetails
        """
        return self._managed_instance_group

    @managed_instance_group.setter
    def managed_instance_group(self, managed_instance_group):
        """
        Sets the managed_instance_group of this ProfileVersion.

        :param managed_instance_group: The managed_instance_group of this ProfileVersion.
        :type: oci.os_management_hub.models.ManagedInstanceGroupDetails
        """
        self._managed_instance_group = managed_instance_group

    @property
    def lifecycle_environment(self):
        """
        Gets the lifecycle_environment of this ProfileVersion.

        :return: The lifecycle_environment of this ProfileVersion.
        :rtype: oci.os_management_hub.models.LifecycleEnvironmentDetails
        """
        return self._lifecycle_environment

    @lifecycle_environment.setter
    def lifecycle_environment(self, lifecycle_environment):
        """
        Sets the lifecycle_environment of this ProfileVersion.

        :param lifecycle_environment: The lifecycle_environment of this ProfileVersion.
        :type: oci.os_management_hub.models.LifecycleEnvironmentDetails
        """
        self._lifecycle_environment = lifecycle_environment

    @property
    def lifecycle_stage(self):
        """
        Gets the lifecycle_stage of this ProfileVersion.

        :return: The lifecycle_stage of this ProfileVersion.
        :rtype: oci.os_management_hub.models.LifecycleStageDetails
        """
        return self._lifecycle_stage

    @lifecycle_stage.setter
    def lifecycle_stage(self, lifecycle_stage):
        """
        Sets the lifecycle_stage of this ProfileVersion.

        :param lifecycle_stage: The lifecycle_stage of this ProfileVersion.
        :type: oci.os_management_hub.models.LifecycleStageDetails
        """
        self._lifecycle_stage = lifecycle_stage

    @property
    def profile_type(self):
        """
        Gets the profile_type of this ProfileVersion.
        The type of profile.

        Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION", "WINDOWS_STANDALONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The profile_type of this ProfileVersion.
        :rtype: str
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """
        Sets the profile_type of this ProfileVersion.
        The type of profile.


        :param profile_type: The profile_type of this ProfileVersion.
        :type: str
        """
        allowed_values = ["SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION", "WINDOWS_STANDALONE"]
        if not value_allowed_none_or_none_sentinel(profile_type, allowed_values):
            profile_type = 'UNKNOWN_ENUM_VALUE'
        self._profile_type = profile_type

    @property
    def vendor_name(self):
        """
        **[Required]** Gets the vendor_name of this ProfileVersion.
        The vendor of the operating system for the instance.

        Allowed values for this property are: "ORACLE", "MICROSOFT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The vendor_name of this ProfileVersion.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this ProfileVersion.
        The vendor of the operating system for the instance.


        :param vendor_name: The vendor_name of this ProfileVersion.
        :type: str
        """
        allowed_values = ["ORACLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(vendor_name, allowed_values):
            vendor_name = 'UNKNOWN_ENUM_VALUE'
        self._vendor_name = vendor_name

    @property
    def os_family(self):
        """
        **[Required]** Gets the os_family of this ProfileVersion.
        The operating system family.

        Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this ProfileVersion.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this ProfileVersion.
        The operating system family.


        :param os_family: The os_family of this ProfileVersion.
        :type: str
        """
        allowed_values = ["ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7", "ORACLE_LINUX_6", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019", "WINDOWS_SERVER_2022", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this ProfileVersion.
        The architecture type.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this ProfileVersion.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this ProfileVersion.
        The architecture type.


        :param arch_type: The arch_type of this ProfileVersion.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def time_created(self):
        """
        Gets the time_created of this ProfileVersion.
        The time the registration profile was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ProfileVersion.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProfileVersion.
        The time the registration profile was created (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ProfileVersion.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        Gets the time_modified of this ProfileVersion.
        The time the registration profile was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_modified of this ProfileVersion.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ProfileVersion.
        The time the registration profile was last modified (in `RFC 3339`__ format).

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_modified: The time_modified of this ProfileVersion.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def profile_version(self):
        """
        Gets the profile_version of this ProfileVersion.
        The version of the profile.


        :return: The profile_version of this ProfileVersion.
        :rtype: str
        """
        return self._profile_version

    @profile_version.setter
    def profile_version(self, profile_version):
        """
        Sets the profile_version of this ProfileVersion.
        The version of the profile.


        :param profile_version: The profile_version of this ProfileVersion.
        :type: str
        """
        self._profile_version = profile_version

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ProfileVersion.
        The current state of the registration profile.


        :return: The lifecycle_state of this ProfileVersion.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProfileVersion.
        The current state of the registration profile.


        :param lifecycle_state: The lifecycle_state of this ProfileVersion.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def registration_type(self):
        """
        Gets the registration_type of this ProfileVersion.
        The type of instance to register.

        Allowed values for this property are: "OCI_LINUX", "NON_OCI_LINUX", "OCI_WINDOWS", "AUTONOMOUS_LINUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The registration_type of this ProfileVersion.
        :rtype: str
        """
        return self._registration_type

    @registration_type.setter
    def registration_type(self, registration_type):
        """
        Sets the registration_type of this ProfileVersion.
        The type of instance to register.


        :param registration_type: The registration_type of this ProfileVersion.
        :type: str
        """
        allowed_values = ["OCI_LINUX", "NON_OCI_LINUX", "OCI_WINDOWS", "AUTONOMOUS_LINUX"]
        if not value_allowed_none_or_none_sentinel(registration_type, allowed_values):
            registration_type = 'UNKNOWN_ENUM_VALUE'
        self._registration_type = registration_type

    @property
    def is_default_profile(self):
        """
        Gets the is_default_profile of this ProfileVersion.
        Indicates if the profile is set as the default. There is exactly one default profile for a specified architecture, OS family, registration type, and vendor. When registering an instance with the corresonding characteristics, the default profile is used, unless another profile is specified.


        :return: The is_default_profile of this ProfileVersion.
        :rtype: bool
        """
        return self._is_default_profile

    @is_default_profile.setter
    def is_default_profile(self, is_default_profile):
        """
        Sets the is_default_profile of this ProfileVersion.
        Indicates if the profile is set as the default. There is exactly one default profile for a specified architecture, OS family, registration type, and vendor. When registering an instance with the corresonding characteristics, the default profile is used, unless another profile is specified.


        :param is_default_profile: The is_default_profile of this ProfileVersion.
        :type: bool
        """
        self._is_default_profile = is_default_profile

    @property
    def is_service_provided_profile(self):
        """
        Gets the is_service_provided_profile of this ProfileVersion.
        Indicates if the profile was created by the service. OS Management Hub provides a limited set of standardized profiles that can be used to register Autonomous Linux or Windows instances.


        :return: The is_service_provided_profile of this ProfileVersion.
        :rtype: bool
        """
        return self._is_service_provided_profile

    @is_service_provided_profile.setter
    def is_service_provided_profile(self, is_service_provided_profile):
        """
        Sets the is_service_provided_profile of this ProfileVersion.
        Indicates if the profile was created by the service. OS Management Hub provides a limited set of standardized profiles that can be used to register Autonomous Linux or Windows instances.


        :param is_service_provided_profile: The is_service_provided_profile of this ProfileVersion.
        :type: bool
        """
        self._is_service_provided_profile = is_service_provided_profile

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
