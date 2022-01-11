# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudExadataInfrastructure(object):
    """
    Details of the cloud Exadata infrastructure resource. Applies to Exadata Cloud Service instances only.
    """

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CloudExadataInfrastructure.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudExadataInfrastructure object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CloudExadataInfrastructure.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudExadataInfrastructure.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CloudExadataInfrastructure.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this CloudExadataInfrastructure.
        :type display_name: str

        :param shape:
            The value to assign to the shape property of this CloudExadataInfrastructure.
        :type shape: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CloudExadataInfrastructure.
        :type availability_domain: str

        :param compute_count:
            The value to assign to the compute_count property of this CloudExadataInfrastructure.
        :type compute_count: int

        :param storage_count:
            The value to assign to the storage_count property of this CloudExadataInfrastructure.
        :type storage_count: int

        :param total_storage_size_in_gbs:
            The value to assign to the total_storage_size_in_gbs property of this CloudExadataInfrastructure.
        :type total_storage_size_in_gbs: int

        :param available_storage_size_in_gbs:
            The value to assign to the available_storage_size_in_gbs property of this CloudExadataInfrastructure.
        :type available_storage_size_in_gbs: int

        :param time_created:
            The value to assign to the time_created property of this CloudExadataInfrastructure.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CloudExadataInfrastructure.
        :type lifecycle_details: str

        :param maintenance_window:
            The value to assign to the maintenance_window property of this CloudExadataInfrastructure.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this CloudExadataInfrastructure.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this CloudExadataInfrastructure.
        :type next_maintenance_run_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloudExadataInfrastructure.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloudExadataInfrastructure.
        :type defined_tags: dict(str, dict(str, object))

        :param customer_contacts:
            The value to assign to the customer_contacts property of this CloudExadataInfrastructure.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'shape': 'str',
            'availability_domain': 'str',
            'compute_count': 'int',
            'storage_count': 'int',
            'total_storage_size_in_gbs': 'int',
            'available_storage_size_in_gbs': 'int',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'maintenance_window': 'MaintenanceWindow',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'customer_contacts': 'list[CustomerContact]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'shape': 'shape',
            'availability_domain': 'availabilityDomain',
            'compute_count': 'computeCount',
            'storage_count': 'storageCount',
            'total_storage_size_in_gbs': 'totalStorageSizeInGBs',
            'available_storage_size_in_gbs': 'availableStorageSizeInGBs',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'maintenance_window': 'maintenanceWindow',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'customer_contacts': 'customerContacts'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._display_name = None
        self._shape = None
        self._availability_domain = None
        self._compute_count = None
        self._storage_count = None
        self._total_storage_size_in_gbs = None
        self._available_storage_size_in_gbs = None
        self._time_created = None
        self._lifecycle_details = None
        self._maintenance_window = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._customer_contacts = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CloudExadataInfrastructure.
        The `OCID`__ of the cloud Exadata infrastructure resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudExadataInfrastructure.
        The `OCID`__ of the cloud Exadata infrastructure resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CloudExadataInfrastructure.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CloudExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloudExadataInfrastructure.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CloudExadataInfrastructure.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CloudExadataInfrastructure.
        The current lifecycle state of the cloud Exadata infrastructure resource.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CloudExadataInfrastructure.
        The current lifecycle state of the cloud Exadata infrastructure resource.


        :param lifecycle_state: The lifecycle_state of this CloudExadataInfrastructure.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CloudExadataInfrastructure.
        The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.


        :return: The display_name of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloudExadataInfrastructure.
        The user-friendly name for the cloud Exadata infrastructure resource. The name does not need to be unique.


        :param display_name: The display_name of this CloudExadataInfrastructure.
        :type: str
        """
        self._display_name = display_name

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CloudExadataInfrastructure.
        The model name of the cloud Exadata infrastructure resource.


        :return: The shape of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CloudExadataInfrastructure.
        The model name of the cloud Exadata infrastructure resource.


        :param shape: The shape of this CloudExadataInfrastructure.
        :type: str
        """
        self._shape = shape

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this CloudExadataInfrastructure.
        The name of the availability domain that the cloud Exadata infrastructure resource is located in.


        :return: The availability_domain of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CloudExadataInfrastructure.
        The name of the availability domain that the cloud Exadata infrastructure resource is located in.


        :param availability_domain: The availability_domain of this CloudExadataInfrastructure.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compute_count(self):
        """
        Gets the compute_count of this CloudExadataInfrastructure.
        The number of compute servers for the cloud Exadata infrastructure.


        :return: The compute_count of this CloudExadataInfrastructure.
        :rtype: int
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this CloudExadataInfrastructure.
        The number of compute servers for the cloud Exadata infrastructure.


        :param compute_count: The compute_count of this CloudExadataInfrastructure.
        :type: int
        """
        self._compute_count = compute_count

    @property
    def storage_count(self):
        """
        Gets the storage_count of this CloudExadataInfrastructure.
        The number of storage servers for the cloud Exadata infrastructure.


        :return: The storage_count of this CloudExadataInfrastructure.
        :rtype: int
        """
        return self._storage_count

    @storage_count.setter
    def storage_count(self, storage_count):
        """
        Sets the storage_count of this CloudExadataInfrastructure.
        The number of storage servers for the cloud Exadata infrastructure.


        :param storage_count: The storage_count of this CloudExadataInfrastructure.
        :type: int
        """
        self._storage_count = storage_count

    @property
    def total_storage_size_in_gbs(self):
        """
        Gets the total_storage_size_in_gbs of this CloudExadataInfrastructure.
        The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).


        :return: The total_storage_size_in_gbs of this CloudExadataInfrastructure.
        :rtype: int
        """
        return self._total_storage_size_in_gbs

    @total_storage_size_in_gbs.setter
    def total_storage_size_in_gbs(self, total_storage_size_in_gbs):
        """
        Sets the total_storage_size_in_gbs of this CloudExadataInfrastructure.
        The total storage allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).


        :param total_storage_size_in_gbs: The total_storage_size_in_gbs of this CloudExadataInfrastructure.
        :type: int
        """
        self._total_storage_size_in_gbs = total_storage_size_in_gbs

    @property
    def available_storage_size_in_gbs(self):
        """
        Gets the available_storage_size_in_gbs of this CloudExadataInfrastructure.
        The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).


        :return: The available_storage_size_in_gbs of this CloudExadataInfrastructure.
        :rtype: int
        """
        return self._available_storage_size_in_gbs

    @available_storage_size_in_gbs.setter
    def available_storage_size_in_gbs(self, available_storage_size_in_gbs):
        """
        Sets the available_storage_size_in_gbs of this CloudExadataInfrastructure.
        The available storage can be allocated to the cloud Exadata infrastructure resource, in gigabytes (GB).


        :param available_storage_size_in_gbs: The available_storage_size_in_gbs of this CloudExadataInfrastructure.
        :type: int
        """
        self._available_storage_size_in_gbs = available_storage_size_in_gbs

    @property
    def time_created(self):
        """
        Gets the time_created of this CloudExadataInfrastructure.
        The date and time the cloud Exadata infrastructure resource was created.


        :return: The time_created of this CloudExadataInfrastructure.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CloudExadataInfrastructure.
        The date and time the cloud Exadata infrastructure resource was created.


        :param time_created: The time_created of this CloudExadataInfrastructure.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CloudExadataInfrastructure.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CloudExadataInfrastructure.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this CloudExadataInfrastructure.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def maintenance_window(self):
        """
        Gets the maintenance_window of this CloudExadataInfrastructure.

        :return: The maintenance_window of this CloudExadataInfrastructure.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this CloudExadataInfrastructure.

        :param maintenance_window: The maintenance_window of this CloudExadataInfrastructure.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def last_maintenance_run_id(self):
        """
        Gets the last_maintenance_run_id of this CloudExadataInfrastructure.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_maintenance_run_id of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._last_maintenance_run_id

    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, last_maintenance_run_id):
        """
        Sets the last_maintenance_run_id of this CloudExadataInfrastructure.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_maintenance_run_id: The last_maintenance_run_id of this CloudExadataInfrastructure.
        :type: str
        """
        self._last_maintenance_run_id = last_maintenance_run_id

    @property
    def next_maintenance_run_id(self):
        """
        Gets the next_maintenance_run_id of this CloudExadataInfrastructure.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_maintenance_run_id of this CloudExadataInfrastructure.
        :rtype: str
        """
        return self._next_maintenance_run_id

    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, next_maintenance_run_id):
        """
        Sets the next_maintenance_run_id of this CloudExadataInfrastructure.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_maintenance_run_id: The next_maintenance_run_id of this CloudExadataInfrastructure.
        :type: str
        """
        self._next_maintenance_run_id = next_maintenance_run_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CloudExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CloudExadataInfrastructure.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CloudExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CloudExadataInfrastructure.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CloudExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CloudExadataInfrastructure.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CloudExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CloudExadataInfrastructure.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this CloudExadataInfrastructure.
        The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource.
        Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators.
        Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.


        :return: The customer_contacts of this CloudExadataInfrastructure.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this CloudExadataInfrastructure.
        The list of customer email addresses that receive information from Oracle about the specified OCI Database service resource.
        Oracle uses these email addresses to send notifications about planned and unplanned software maintenance updates, information about system hardware, and other information needed by administrators.
        Up to 10 email addresses can be added to the customer contacts for a cloud Exadata infrastructure instance.


        :param customer_contacts: The customer_contacts of this CloudExadataInfrastructure.
        :type: list[oci.database.models.CustomerContact]
        """
        self._customer_contacts = customer_contacts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
