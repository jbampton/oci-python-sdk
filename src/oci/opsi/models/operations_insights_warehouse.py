# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationsInsightsWarehouse(object):
    """
    OPSI warehouse resource.
    """

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OperationsInsightsWarehouse.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OperationsInsightsWarehouse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperationsInsightsWarehouse.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperationsInsightsWarehouse.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this OperationsInsightsWarehouse.
        :type display_name: str

        :param cpu_allocated:
            The value to assign to the cpu_allocated property of this OperationsInsightsWarehouse.
        :type cpu_allocated: float

        :param cpu_used:
            The value to assign to the cpu_used property of this OperationsInsightsWarehouse.
        :type cpu_used: float

        :param storage_allocated_in_gbs:
            The value to assign to the storage_allocated_in_gbs property of this OperationsInsightsWarehouse.
        :type storage_allocated_in_gbs: float

        :param storage_used_in_gbs:
            The value to assign to the storage_used_in_gbs property of this OperationsInsightsWarehouse.
        :type storage_used_in_gbs: float

        :param dynamic_group_id:
            The value to assign to the dynamic_group_id property of this OperationsInsightsWarehouse.
        :type dynamic_group_id: str

        :param operations_insights_tenancy_id:
            The value to assign to the operations_insights_tenancy_id property of this OperationsInsightsWarehouse.
        :type operations_insights_tenancy_id: str

        :param time_last_wallet_rotated:
            The value to assign to the time_last_wallet_rotated property of this OperationsInsightsWarehouse.
        :type time_last_wallet_rotated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OperationsInsightsWarehouse.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OperationsInsightsWarehouse.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OperationsInsightsWarehouse.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this OperationsInsightsWarehouse.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OperationsInsightsWarehouse.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperationsInsightsWarehouse.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OperationsInsightsWarehouse.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'cpu_allocated': 'float',
            'cpu_used': 'float',
            'storage_allocated_in_gbs': 'float',
            'storage_used_in_gbs': 'float',
            'dynamic_group_id': 'str',
            'operations_insights_tenancy_id': 'str',
            'time_last_wallet_rotated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'cpu_allocated': 'cpuAllocated',
            'cpu_used': 'cpuUsed',
            'storage_allocated_in_gbs': 'storageAllocatedInGBs',
            'storage_used_in_gbs': 'storageUsedInGBs',
            'dynamic_group_id': 'dynamicGroupId',
            'operations_insights_tenancy_id': 'operationsInsightsTenancyId',
            'time_last_wallet_rotated': 'timeLastWalletRotated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._cpu_allocated = None
        self._cpu_used = None
        self._storage_allocated_in_gbs = None
        self._storage_used_in_gbs = None
        self._dynamic_group_id = None
        self._operations_insights_tenancy_id = None
        self._time_last_wallet_rotated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperationsInsightsWarehouse.
        OPSI Warehouse OCID


        :return: The id of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperationsInsightsWarehouse.
        OPSI Warehouse OCID


        :param id: The id of this OperationsInsightsWarehouse.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OperationsInsightsWarehouse.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperationsInsightsWarehouse.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OperationsInsightsWarehouse.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OperationsInsightsWarehouse.
        User-friedly name of Operations Insights Warehouse that does not have to be unique.


        :return: The display_name of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OperationsInsightsWarehouse.
        User-friedly name of Operations Insights Warehouse that does not have to be unique.


        :param display_name: The display_name of this OperationsInsightsWarehouse.
        :type: str
        """
        self._display_name = display_name

    @property
    def cpu_allocated(self):
        """
        **[Required]** Gets the cpu_allocated of this OperationsInsightsWarehouse.
        Number of OCPUs allocated to OPSI Warehouse ADW.


        :return: The cpu_allocated of this OperationsInsightsWarehouse.
        :rtype: float
        """
        return self._cpu_allocated

    @cpu_allocated.setter
    def cpu_allocated(self, cpu_allocated):
        """
        Sets the cpu_allocated of this OperationsInsightsWarehouse.
        Number of OCPUs allocated to OPSI Warehouse ADW.


        :param cpu_allocated: The cpu_allocated of this OperationsInsightsWarehouse.
        :type: float
        """
        self._cpu_allocated = cpu_allocated

    @property
    def cpu_used(self):
        """
        Gets the cpu_used of this OperationsInsightsWarehouse.
        Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.


        :return: The cpu_used of this OperationsInsightsWarehouse.
        :rtype: float
        """
        return self._cpu_used

    @cpu_used.setter
    def cpu_used(self, cpu_used):
        """
        Sets the cpu_used of this OperationsInsightsWarehouse.
        Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.


        :param cpu_used: The cpu_used of this OperationsInsightsWarehouse.
        :type: float
        """
        self._cpu_used = cpu_used

    @property
    def storage_allocated_in_gbs(self):
        """
        Gets the storage_allocated_in_gbs of this OperationsInsightsWarehouse.
        Storage allocated to OPSI Warehouse ADW.


        :return: The storage_allocated_in_gbs of this OperationsInsightsWarehouse.
        :rtype: float
        """
        return self._storage_allocated_in_gbs

    @storage_allocated_in_gbs.setter
    def storage_allocated_in_gbs(self, storage_allocated_in_gbs):
        """
        Sets the storage_allocated_in_gbs of this OperationsInsightsWarehouse.
        Storage allocated to OPSI Warehouse ADW.


        :param storage_allocated_in_gbs: The storage_allocated_in_gbs of this OperationsInsightsWarehouse.
        :type: float
        """
        self._storage_allocated_in_gbs = storage_allocated_in_gbs

    @property
    def storage_used_in_gbs(self):
        """
        Gets the storage_used_in_gbs of this OperationsInsightsWarehouse.
        Storage by OPSI Warehouse ADW in GB.


        :return: The storage_used_in_gbs of this OperationsInsightsWarehouse.
        :rtype: float
        """
        return self._storage_used_in_gbs

    @storage_used_in_gbs.setter
    def storage_used_in_gbs(self, storage_used_in_gbs):
        """
        Sets the storage_used_in_gbs of this OperationsInsightsWarehouse.
        Storage by OPSI Warehouse ADW in GB.


        :param storage_used_in_gbs: The storage_used_in_gbs of this OperationsInsightsWarehouse.
        :type: float
        """
        self._storage_used_in_gbs = storage_used_in_gbs

    @property
    def dynamic_group_id(self):
        """
        Gets the dynamic_group_id of this OperationsInsightsWarehouse.
        OCID of the dynamic group created for the warehouse


        :return: The dynamic_group_id of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._dynamic_group_id

    @dynamic_group_id.setter
    def dynamic_group_id(self, dynamic_group_id):
        """
        Sets the dynamic_group_id of this OperationsInsightsWarehouse.
        OCID of the dynamic group created for the warehouse


        :param dynamic_group_id: The dynamic_group_id of this OperationsInsightsWarehouse.
        :type: str
        """
        self._dynamic_group_id = dynamic_group_id

    @property
    def operations_insights_tenancy_id(self):
        """
        Gets the operations_insights_tenancy_id of this OperationsInsightsWarehouse.
        Tenancy Identifier of Operations Insights service


        :return: The operations_insights_tenancy_id of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._operations_insights_tenancy_id

    @operations_insights_tenancy_id.setter
    def operations_insights_tenancy_id(self, operations_insights_tenancy_id):
        """
        Sets the operations_insights_tenancy_id of this OperationsInsightsWarehouse.
        Tenancy Identifier of Operations Insights service


        :param operations_insights_tenancy_id: The operations_insights_tenancy_id of this OperationsInsightsWarehouse.
        :type: str
        """
        self._operations_insights_tenancy_id = operations_insights_tenancy_id

    @property
    def time_last_wallet_rotated(self):
        """
        Gets the time_last_wallet_rotated of this OperationsInsightsWarehouse.
        The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string


        :return: The time_last_wallet_rotated of this OperationsInsightsWarehouse.
        :rtype: datetime
        """
        return self._time_last_wallet_rotated

    @time_last_wallet_rotated.setter
    def time_last_wallet_rotated(self, time_last_wallet_rotated):
        """
        Sets the time_last_wallet_rotated of this OperationsInsightsWarehouse.
        The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string


        :param time_last_wallet_rotated: The time_last_wallet_rotated of this OperationsInsightsWarehouse.
        :type: datetime
        """
        self._time_last_wallet_rotated = time_last_wallet_rotated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OperationsInsightsWarehouse.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OperationsInsightsWarehouse.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OperationsInsightsWarehouse.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OperationsInsightsWarehouse.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OperationsInsightsWarehouse.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OperationsInsightsWarehouse.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OperationsInsightsWarehouse.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OperationsInsightsWarehouse.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OperationsInsightsWarehouse.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OperationsInsightsWarehouse.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OperationsInsightsWarehouse.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OperationsInsightsWarehouse.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OperationsInsightsWarehouse.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :return: The time_created of this OperationsInsightsWarehouse.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OperationsInsightsWarehouse.
        The time at which the resource was first created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this OperationsInsightsWarehouse.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OperationsInsightsWarehouse.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this OperationsInsightsWarehouse.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OperationsInsightsWarehouse.
        The time at which the resource was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this OperationsInsightsWarehouse.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OperationsInsightsWarehouse.
        Possible lifecycle states

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperationsInsightsWarehouse.
        Possible lifecycle states


        :param lifecycle_state: The lifecycle_state of this OperationsInsightsWarehouse.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this OperationsInsightsWarehouse.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this OperationsInsightsWarehouse.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this OperationsInsightsWarehouse.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this OperationsInsightsWarehouse.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
