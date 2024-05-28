# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231107


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OccAvailabilitySummary(object):
    """
    The details about the available capacity and constraints for different resource types present in the availability catalog.
    """

    #: A constant which can be used with the namespace property of a OccAvailabilitySummary.
    #: This constant has a value of "COMPUTE"
    NAMESPACE_COMPUTE = "COMPUTE"

    def __init__(self, **kwargs):
        """
        Initializes a new OccAvailabilitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param catalog_id:
            The value to assign to the catalog_id property of this OccAvailabilitySummary.
        :type catalog_id: str

        :param namespace:
            The value to assign to the namespace property of this OccAvailabilitySummary.
            Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type namespace: str

        :param date_final_customer_order:
            The value to assign to the date_final_customer_order property of this OccAvailabilitySummary.
        :type date_final_customer_order: datetime

        :param date_expected_capacity_handover:
            The value to assign to the date_expected_capacity_handover property of this OccAvailabilitySummary.
        :type date_expected_capacity_handover: datetime

        :param resource_type:
            The value to assign to the resource_type property of this OccAvailabilitySummary.
        :type resource_type: str

        :param workload_type:
            The value to assign to the workload_type property of this OccAvailabilitySummary.
        :type workload_type: str

        :param resource_name:
            The value to assign to the resource_name property of this OccAvailabilitySummary.
        :type resource_name: str

        :param available_quantity:
            The value to assign to the available_quantity property of this OccAvailabilitySummary.
        :type available_quantity: int

        :param total_available_quantity:
            The value to assign to the total_available_quantity property of this OccAvailabilitySummary.
        :type total_available_quantity: int

        :param demanded_quantity:
            The value to assign to the demanded_quantity property of this OccAvailabilitySummary.
        :type demanded_quantity: int

        :param unit:
            The value to assign to the unit property of this OccAvailabilitySummary.
        :type unit: str

        :param system_tags:
            The value to assign to the system_tags property of this OccAvailabilitySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'catalog_id': 'str',
            'namespace': 'str',
            'date_final_customer_order': 'datetime',
            'date_expected_capacity_handover': 'datetime',
            'resource_type': 'str',
            'workload_type': 'str',
            'resource_name': 'str',
            'available_quantity': 'int',
            'total_available_quantity': 'int',
            'demanded_quantity': 'int',
            'unit': 'str',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'catalog_id': 'catalogId',
            'namespace': 'namespace',
            'date_final_customer_order': 'dateFinalCustomerOrder',
            'date_expected_capacity_handover': 'dateExpectedCapacityHandover',
            'resource_type': 'resourceType',
            'workload_type': 'workloadType',
            'resource_name': 'resourceName',
            'available_quantity': 'availableQuantity',
            'total_available_quantity': 'totalAvailableQuantity',
            'demanded_quantity': 'demandedQuantity',
            'unit': 'unit',
            'system_tags': 'systemTags'
        }

        self._catalog_id = None
        self._namespace = None
        self._date_final_customer_order = None
        self._date_expected_capacity_handover = None
        self._resource_type = None
        self._workload_type = None
        self._resource_name = None
        self._available_quantity = None
        self._total_available_quantity = None
        self._demanded_quantity = None
        self._unit = None
        self._system_tags = None

    @property
    def catalog_id(self):
        """
        **[Required]** Gets the catalog_id of this OccAvailabilitySummary.
        The OCID of the availability catalog.


        :return: The catalog_id of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this OccAvailabilitySummary.
        The OCID of the availability catalog.


        :param catalog_id: The catalog_id of this OccAvailabilitySummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this OccAvailabilitySummary.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.

        Allowed values for this property are: "COMPUTE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The namespace of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OccAvailabilitySummary.
        The name of the OCI service in consideration. For example, Compute, Exadata, and so on.


        :param namespace: The namespace of this OccAvailabilitySummary.
        :type: str
        """
        allowed_values = ["COMPUTE"]
        if not value_allowed_none_or_none_sentinel(namespace, allowed_values):
            namespace = 'UNKNOWN_ENUM_VALUE'
        self._namespace = namespace

    @property
    def date_final_customer_order(self):
        """
        **[Required]** Gets the date_final_customer_order of this OccAvailabilitySummary.
        The date by which the customer must place the order to have their capacity requirements met by the customer handover date.


        :return: The date_final_customer_order of this OccAvailabilitySummary.
        :rtype: datetime
        """
        return self._date_final_customer_order

    @date_final_customer_order.setter
    def date_final_customer_order(self, date_final_customer_order):
        """
        Sets the date_final_customer_order of this OccAvailabilitySummary.
        The date by which the customer must place the order to have their capacity requirements met by the customer handover date.


        :param date_final_customer_order: The date_final_customer_order of this OccAvailabilitySummary.
        :type: datetime
        """
        self._date_final_customer_order = date_final_customer_order

    @property
    def date_expected_capacity_handover(self):
        """
        **[Required]** Gets the date_expected_capacity_handover of this OccAvailabilitySummary.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :return: The date_expected_capacity_handover of this OccAvailabilitySummary.
        :rtype: datetime
        """
        return self._date_expected_capacity_handover

    @date_expected_capacity_handover.setter
    def date_expected_capacity_handover(self, date_expected_capacity_handover):
        """
        Sets the date_expected_capacity_handover of this OccAvailabilitySummary.
        The date by which the capacity requested by customers before dateFinalCustomerOrder needs to be fulfilled.


        :param date_expected_capacity_handover: The date_expected_capacity_handover of this OccAvailabilitySummary.
        :type: datetime
        """
        self._date_expected_capacity_handover = date_expected_capacity_handover

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this OccAvailabilitySummary.
        The different types of resources against which customers can place capacity requests.


        :return: The resource_type of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this OccAvailabilitySummary.
        The different types of resources against which customers can place capacity requests.


        :param resource_type: The resource_type of this OccAvailabilitySummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def workload_type(self):
        """
        **[Required]** Gets the workload_type of this OccAvailabilitySummary.
        The type of workload (Generic/ROW).


        :return: The workload_type of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this OccAvailabilitySummary.
        The type of workload (Generic/ROW).


        :param workload_type: The workload_type of this OccAvailabilitySummary.
        :type: str
        """
        self._workload_type = workload_type

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this OccAvailabilitySummary.
        The name of the resource that the customer can request.


        :return: The resource_name of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this OccAvailabilitySummary.
        The name of the resource that the customer can request.


        :param resource_name: The resource_name of this OccAvailabilitySummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def available_quantity(self):
        """
        **[Required]** Gets the available_quantity of this OccAvailabilitySummary.
        The quantity of resource currently available that the customer can request.


        :return: The available_quantity of this OccAvailabilitySummary.
        :rtype: int
        """
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        """
        Sets the available_quantity of this OccAvailabilitySummary.
        The quantity of resource currently available that the customer can request.


        :param available_quantity: The available_quantity of this OccAvailabilitySummary.
        :type: int
        """
        self._available_quantity = available_quantity

    @property
    def total_available_quantity(self):
        """
        **[Required]** Gets the total_available_quantity of this OccAvailabilitySummary.
        The total quantity of resource that the customer can request.


        :return: The total_available_quantity of this OccAvailabilitySummary.
        :rtype: int
        """
        return self._total_available_quantity

    @total_available_quantity.setter
    def total_available_quantity(self, total_available_quantity):
        """
        Sets the total_available_quantity of this OccAvailabilitySummary.
        The total quantity of resource that the customer can request.


        :param total_available_quantity: The total_available_quantity of this OccAvailabilitySummary.
        :type: int
        """
        self._total_available_quantity = total_available_quantity

    @property
    def demanded_quantity(self):
        """
        **[Required]** Gets the demanded_quantity of this OccAvailabilitySummary.
        The quantity of resource currently demanded by the customer.


        :return: The demanded_quantity of this OccAvailabilitySummary.
        :rtype: int
        """
        return self._demanded_quantity

    @demanded_quantity.setter
    def demanded_quantity(self, demanded_quantity):
        """
        Sets the demanded_quantity of this OccAvailabilitySummary.
        The quantity of resource currently demanded by the customer.


        :param demanded_quantity: The demanded_quantity of this OccAvailabilitySummary.
        :type: int
        """
        self._demanded_quantity = demanded_quantity

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this OccAvailabilitySummary.
        The unit in which the resource available is measured.


        :return: The unit of this OccAvailabilitySummary.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this OccAvailabilitySummary.
        The unit in which the resource available is measured.


        :param unit: The unit of this OccAvailabilitySummary.
        :type: str
        """
        self._unit = unit

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OccAvailabilitySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OccAvailabilitySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OccAvailabilitySummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OccAvailabilitySummary.
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
