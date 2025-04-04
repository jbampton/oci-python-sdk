# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240815


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityAttributeNamespaceSummary(object):
    """
    A container for security attributes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityAttributeNamespaceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SecurityAttributeNamespaceSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SecurityAttributeNamespaceSummary.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this SecurityAttributeNamespaceSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this SecurityAttributeNamespaceSummary.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SecurityAttributeNamespaceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SecurityAttributeNamespaceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SecurityAttributeNamespaceSummary.
        :type system_tags: dict(str, dict(str, object))

        :param is_retired:
            The value to assign to the is_retired property of this SecurityAttributeNamespaceSummary.
        :type is_retired: bool

        :param mode:
            The value to assign to the mode property of this SecurityAttributeNamespaceSummary.
        :type mode: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SecurityAttributeNamespaceSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this SecurityAttributeNamespaceSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'is_retired': 'bool',
            'mode': 'list[str]',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'is_retired': 'isRetired',
            'mode': 'mode',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }
        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._is_retired = None
        self._mode = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        Gets the id of this SecurityAttributeNamespaceSummary.
        The OCID of the security attribute namespace.


        :return: The id of this SecurityAttributeNamespaceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SecurityAttributeNamespaceSummary.
        The OCID of the security attribute namespace.


        :param id: The id of this SecurityAttributeNamespaceSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SecurityAttributeNamespaceSummary.
        The OCID of the compartment that contains the security attribute namespace.


        :return: The compartment_id of this SecurityAttributeNamespaceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SecurityAttributeNamespaceSummary.
        The OCID of the compartment that contains the security attribute namespace.


        :param compartment_id: The compartment_id of this SecurityAttributeNamespaceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this SecurityAttributeNamespaceSummary.
        The name of the security attribute namespace. It must be unique across all security attribute namespaces in the tenancy and cannot be changed.


        :return: The name of this SecurityAttributeNamespaceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityAttributeNamespaceSummary.
        The name of the security attribute namespace. It must be unique across all security attribute namespaces in the tenancy and cannot be changed.


        :param name: The name of this SecurityAttributeNamespaceSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SecurityAttributeNamespaceSummary.
        A description you create for the security attribute namespace to help you identify it.


        :return: The description of this SecurityAttributeNamespaceSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityAttributeNamespaceSummary.
        A description you create for the security attribute namespace to help you identify it.


        :param description: The description of this SecurityAttributeNamespaceSummary.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SecurityAttributeNamespaceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SecurityAttributeNamespaceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SecurityAttributeNamespaceSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SecurityAttributeNamespaceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SecurityAttributeNamespaceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SecurityAttributeNamespaceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SecurityAttributeNamespaceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SecurityAttributeNamespaceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SecurityAttributeNamespaceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SecurityAttributeNamespaceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SecurityAttributeNamespaceSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SecurityAttributeNamespaceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def is_retired(self):
        """
        Gets the is_retired of this SecurityAttributeNamespaceSummary.
        Indicates whether the security attribute namespace is retired.


        :return: The is_retired of this SecurityAttributeNamespaceSummary.
        :rtype: bool
        """
        return self._is_retired

    @is_retired.setter
    def is_retired(self, is_retired):
        """
        Sets the is_retired of this SecurityAttributeNamespaceSummary.
        Indicates whether the security attribute namespace is retired.


        :param is_retired: The is_retired of this SecurityAttributeNamespaceSummary.
        :type: bool
        """
        self._is_retired = is_retired

    @property
    def mode(self):
        """
        Gets the mode of this SecurityAttributeNamespaceSummary.
        Indicates possible modes the security attributes in the namespace can be set to.
        This is not accepted from the user. Currently the supported values are enforce and audit.


        :return: The mode of this SecurityAttributeNamespaceSummary.
        :rtype: list[str]
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this SecurityAttributeNamespaceSummary.
        Indicates possible modes the security attributes in the namespace can be set to.
        This is not accepted from the user. Currently the supported values are enforce and audit.


        :param mode: The mode of this SecurityAttributeNamespaceSummary.
        :type: list[str]
        """
        self._mode = mode

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SecurityAttributeNamespaceSummary.
        The security attribute namespace's current state. After creating a security attribute namespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute namespace, make sure its `lifecycleState` is INACTIVE.


        :return: The lifecycle_state of this SecurityAttributeNamespaceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SecurityAttributeNamespaceSummary.
        The security attribute namespace's current state. After creating a security attribute namespace, make sure its `lifecycleState` is ACTIVE before using it. After retiring a security attribute namespace, make sure its `lifecycleState` is INACTIVE.


        :param lifecycle_state: The lifecycle_state of this SecurityAttributeNamespaceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this SecurityAttributeNamespaceSummary.
        Date and time the security attribute namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SecurityAttributeNamespaceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SecurityAttributeNamespaceSummary.
        Date and time the security attribute namespace was created, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SecurityAttributeNamespaceSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
