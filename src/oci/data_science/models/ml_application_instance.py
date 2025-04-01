# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MlApplicationInstance(object):
    """
    Resource representing instance of ML Application.
    """

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a MlApplicationInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_SUBSTATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_SUBSTATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_SUBSTATE_UPGRADING = "UPGRADING"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_SUBSTATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_SUBSTATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_SUBSTATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_SUBSTATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_SUBSTATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_SUBSTATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "NON_RECOVERABLE_PROVIDER_ISSUE"
    LIFECYCLE_SUBSTATE_NON_RECOVERABLE_PROVIDER_ISSUE = "NON_RECOVERABLE_PROVIDER_ISSUE"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "RECOVERABLE_PROVIDER_ISSUE"
    LIFECYCLE_SUBSTATE_RECOVERABLE_PROVIDER_ISSUE = "RECOVERABLE_PROVIDER_ISSUE"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "NON_RECOVERABLE_SERVICE_ISSUE"
    LIFECYCLE_SUBSTATE_NON_RECOVERABLE_SERVICE_ISSUE = "NON_RECOVERABLE_SERVICE_ISSUE"

    #: A constant which can be used with the lifecycle_substate property of a MlApplicationInstance.
    #: This constant has a value of "RECOVERABLE_SERVICE_ISSUE"
    LIFECYCLE_SUBSTATE_RECOVERABLE_SERVICE_ISSUE = "RECOVERABLE_SERVICE_ISSUE"

    def __init__(self, **kwargs):
        """
        Initializes a new MlApplicationInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MlApplicationInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MlApplicationInstance.
        :type display_name: str

        :param ml_application_id:
            The value to assign to the ml_application_id property of this MlApplicationInstance.
        :type ml_application_id: str

        :param ml_application_name:
            The value to assign to the ml_application_name property of this MlApplicationInstance.
        :type ml_application_name: str

        :param ml_application_implementation_id:
            The value to assign to the ml_application_implementation_id property of this MlApplicationInstance.
        :type ml_application_implementation_id: str

        :param ml_application_implementation_name:
            The value to assign to the ml_application_implementation_name property of this MlApplicationInstance.
        :type ml_application_implementation_name: str

        :param auth_configuration:
            The value to assign to the auth_configuration property of this MlApplicationInstance.
        :type auth_configuration: oci.data_science.models.AuthConfiguration

        :param configuration:
            The value to assign to the configuration property of this MlApplicationInstance.
        :type configuration: list[oci.data_science.models.ConfigurationProperty]

        :param is_enabled:
            The value to assign to the is_enabled property of this MlApplicationInstance.
        :type is_enabled: bool

        :param compartment_id:
            The value to assign to the compartment_id property of this MlApplicationInstance.
        :type compartment_id: str

        :param prediction_endpoint_details:
            The value to assign to the prediction_endpoint_details property of this MlApplicationInstance.
        :type prediction_endpoint_details: oci.data_science.models.PredictionEndpointDetails

        :param time_created:
            The value to assign to the time_created property of this MlApplicationInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MlApplicationInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MlApplicationInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_substate:
            The value to assign to the lifecycle_substate property of this MlApplicationInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "UPGRADING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", "NON_RECOVERABLE_PROVIDER_ISSUE", "RECOVERABLE_PROVIDER_ISSUE", "NON_RECOVERABLE_SERVICE_ISSUE", "RECOVERABLE_SERVICE_ISSUE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_substate: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MlApplicationInstance.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MlApplicationInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MlApplicationInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MlApplicationInstance.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'ml_application_id': 'str',
            'ml_application_name': 'str',
            'ml_application_implementation_id': 'str',
            'ml_application_implementation_name': 'str',
            'auth_configuration': 'AuthConfiguration',
            'configuration': 'list[ConfigurationProperty]',
            'is_enabled': 'bool',
            'compartment_id': 'str',
            'prediction_endpoint_details': 'PredictionEndpointDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_substate': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'ml_application_id': 'mlApplicationId',
            'ml_application_name': 'mlApplicationName',
            'ml_application_implementation_id': 'mlApplicationImplementationId',
            'ml_application_implementation_name': 'mlApplicationImplementationName',
            'auth_configuration': 'authConfiguration',
            'configuration': 'configuration',
            'is_enabled': 'isEnabled',
            'compartment_id': 'compartmentId',
            'prediction_endpoint_details': 'predictionEndpointDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_substate': 'lifecycleSubstate',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._display_name = None
        self._ml_application_id = None
        self._ml_application_name = None
        self._ml_application_implementation_id = None
        self._ml_application_implementation_name = None
        self._auth_configuration = None
        self._configuration = None
        self._is_enabled = None
        self._compartment_id = None
        self._prediction_endpoint_details = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_substate = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MlApplicationInstance.
        The OCID of the MlApplicationInstance. Unique identifier that is immutable after creation


        :return: The id of this MlApplicationInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MlApplicationInstance.
        The OCID of the MlApplicationInstance. Unique identifier that is immutable after creation


        :param id: The id of this MlApplicationInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MlApplicationInstance.
        The name of MlApplicationInstance. System will generate displayName when not provided during creation.


        :return: The display_name of this MlApplicationInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MlApplicationInstance.
        The name of MlApplicationInstance. System will generate displayName when not provided during creation.


        :param display_name: The display_name of this MlApplicationInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def ml_application_id(self):
        """
        **[Required]** Gets the ml_application_id of this MlApplicationInstance.
        The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.


        :return: The ml_application_id of this MlApplicationInstance.
        :rtype: str
        """
        return self._ml_application_id

    @ml_application_id.setter
    def ml_application_id(self, ml_application_id):
        """
        Sets the ml_application_id of this MlApplicationInstance.
        The OCID of ML Application. This resource is an instance of ML Application referenced by this OCID.


        :param ml_application_id: The ml_application_id of this MlApplicationInstance.
        :type: str
        """
        self._ml_application_id = ml_application_id

    @property
    def ml_application_name(self):
        """
        **[Required]** Gets the ml_application_name of this MlApplicationInstance.
        The name of ML Application (based on mlApplicationId).


        :return: The ml_application_name of this MlApplicationInstance.
        :rtype: str
        """
        return self._ml_application_name

    @ml_application_name.setter
    def ml_application_name(self, ml_application_name):
        """
        Sets the ml_application_name of this MlApplicationInstance.
        The name of ML Application (based on mlApplicationId).


        :param ml_application_name: The ml_application_name of this MlApplicationInstance.
        :type: str
        """
        self._ml_application_name = ml_application_name

    @property
    def ml_application_implementation_id(self):
        """
        **[Required]** Gets the ml_application_implementation_id of this MlApplicationInstance.
        The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)


        :return: The ml_application_implementation_id of this MlApplicationInstance.
        :rtype: str
        """
        return self._ml_application_implementation_id

    @ml_application_implementation_id.setter
    def ml_application_implementation_id(self, ml_application_implementation_id):
        """
        Sets the ml_application_implementation_id of this MlApplicationInstance.
        The OCID of ML Application Implementation selected as a certain solution for a given ML problem (ML Application)


        :param ml_application_implementation_id: The ml_application_implementation_id of this MlApplicationInstance.
        :type: str
        """
        self._ml_application_implementation_id = ml_application_implementation_id

    @property
    def ml_application_implementation_name(self):
        """
        **[Required]** Gets the ml_application_implementation_name of this MlApplicationInstance.
        The name of Ml Application Implementation (based on mlApplicationImplementationId)


        :return: The ml_application_implementation_name of this MlApplicationInstance.
        :rtype: str
        """
        return self._ml_application_implementation_name

    @ml_application_implementation_name.setter
    def ml_application_implementation_name(self, ml_application_implementation_name):
        """
        Sets the ml_application_implementation_name of this MlApplicationInstance.
        The name of Ml Application Implementation (based on mlApplicationImplementationId)


        :param ml_application_implementation_name: The ml_application_implementation_name of this MlApplicationInstance.
        :type: str
        """
        self._ml_application_implementation_name = ml_application_implementation_name

    @property
    def auth_configuration(self):
        """
        Gets the auth_configuration of this MlApplicationInstance.

        :return: The auth_configuration of this MlApplicationInstance.
        :rtype: oci.data_science.models.AuthConfiguration
        """
        return self._auth_configuration

    @auth_configuration.setter
    def auth_configuration(self, auth_configuration):
        """
        Sets the auth_configuration of this MlApplicationInstance.

        :param auth_configuration: The auth_configuration of this MlApplicationInstance.
        :type: oci.data_science.models.AuthConfiguration
        """
        self._auth_configuration = auth_configuration

    @property
    def configuration(self):
        """
        Gets the configuration of this MlApplicationInstance.
        Data that are used for provisioning of the given MlApplicationInstance. These are validated against configurationSchema defined in referenced MlApplicationImplementation.


        :return: The configuration of this MlApplicationInstance.
        :rtype: list[oci.data_science.models.ConfigurationProperty]
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this MlApplicationInstance.
        Data that are used for provisioning of the given MlApplicationInstance. These are validated against configurationSchema defined in referenced MlApplicationImplementation.


        :param configuration: The configuration of this MlApplicationInstance.
        :type: list[oci.data_science.models.ConfigurationProperty]
        """
        self._configuration = configuration

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this MlApplicationInstance.
        States whether the MlApplicationInstance is supposed to be in ACTIVE lifecycle state.


        :return: The is_enabled of this MlApplicationInstance.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this MlApplicationInstance.
        States whether the MlApplicationInstance is supposed to be in ACTIVE lifecycle state.


        :param is_enabled: The is_enabled of this MlApplicationInstance.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MlApplicationInstance.
        The OCID of the compartment where the MlApplicationInstance is created.


        :return: The compartment_id of this MlApplicationInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MlApplicationInstance.
        The OCID of the compartment where the MlApplicationInstance is created.


        :param compartment_id: The compartment_id of this MlApplicationInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def prediction_endpoint_details(self):
        """
        Gets the prediction_endpoint_details of this MlApplicationInstance.

        :return: The prediction_endpoint_details of this MlApplicationInstance.
        :rtype: oci.data_science.models.PredictionEndpointDetails
        """
        return self._prediction_endpoint_details

    @prediction_endpoint_details.setter
    def prediction_endpoint_details(self, prediction_endpoint_details):
        """
        Sets the prediction_endpoint_details of this MlApplicationInstance.

        :param prediction_endpoint_details: The prediction_endpoint_details of this MlApplicationInstance.
        :type: oci.data_science.models.PredictionEndpointDetails
        """
        self._prediction_endpoint_details = prediction_endpoint_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MlApplicationInstance.
        The time the the MlApplication was created. An RFC3339 formatted datetime string


        :return: The time_created of this MlApplicationInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MlApplicationInstance.
        The time the the MlApplication was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MlApplicationInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this MlApplicationInstance.
        Time of last MlApplicationInstance update in the format defined by RFC 3339.


        :return: The time_updated of this MlApplicationInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MlApplicationInstance.
        Time of last MlApplicationInstance update in the format defined by RFC 3339.


        :param time_updated: The time_updated of this MlApplicationInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MlApplicationInstance.
        The current state of the MlApplicationInstance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MlApplicationInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MlApplicationInstance.
        The current state of the MlApplicationInstance.


        :param lifecycle_state: The lifecycle_state of this MlApplicationInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_substate(self):
        """
        **[Required]** Gets the lifecycle_substate of this MlApplicationInstance.
        The current substate of the MlApplicationInstance. The substate has MlApplicationInstance specific values in comparison with lifecycleState which has standard values common for all OCI resources.
        The NEEDS_ATTENTION and FAILED substates are deprecated in favor of (NON_)?RECOVERABLE_(PROVIDER|SERVICE)_ISSUE and will be removed in next release.

        Allowed values for this property are: "CREATING", "UPDATING", "UPGRADING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", "NON_RECOVERABLE_PROVIDER_ISSUE", "RECOVERABLE_PROVIDER_ISSUE", "NON_RECOVERABLE_SERVICE_ISSUE", "RECOVERABLE_SERVICE_ISSUE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_substate of this MlApplicationInstance.
        :rtype: str
        """
        return self._lifecycle_substate

    @lifecycle_substate.setter
    def lifecycle_substate(self, lifecycle_substate):
        """
        Sets the lifecycle_substate of this MlApplicationInstance.
        The current substate of the MlApplicationInstance. The substate has MlApplicationInstance specific values in comparison with lifecycleState which has standard values common for all OCI resources.
        The NEEDS_ATTENTION and FAILED substates are deprecated in favor of (NON_)?RECOVERABLE_(PROVIDER|SERVICE)_ISSUE and will be removed in next release.


        :param lifecycle_substate: The lifecycle_substate of this MlApplicationInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "UPGRADING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "NEEDS_ATTENTION", "FAILED", "NON_RECOVERABLE_PROVIDER_ISSUE", "RECOVERABLE_PROVIDER_ISSUE", "NON_RECOVERABLE_SERVICE_ISSUE", "RECOVERABLE_SERVICE_ISSUE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_substate, allowed_values):
            lifecycle_substate = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_substate = lifecycle_substate

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this MlApplicationInstance.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this MlApplicationInstance.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MlApplicationInstance.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this MlApplicationInstance.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this MlApplicationInstance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this MlApplicationInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MlApplicationInstance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this MlApplicationInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this MlApplicationInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this MlApplicationInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MlApplicationInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this MlApplicationInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MlApplicationInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MlApplicationInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MlApplicationInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MlApplicationInstance.
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
