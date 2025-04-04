# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVbsInstanceDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVbsInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateVbsInstanceDetails.
        :type display_name: str

        :param is_resource_usage_agreement_granted:
            The value to assign to the is_resource_usage_agreement_granted property of this UpdateVbsInstanceDetails.
        :type is_resource_usage_agreement_granted: bool

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this UpdateVbsInstanceDetails.
        :type resource_compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVbsInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVbsInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_resource_usage_agreement_granted': 'bool',
            'resource_compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'is_resource_usage_agreement_granted': 'isResourceUsageAgreementGranted',
            'resource_compartment_id': 'resourceCompartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._is_resource_usage_agreement_granted = None
        self._resource_compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this UpdateVbsInstanceDetails.
        Display Name


        :return: The display_name of this UpdateVbsInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVbsInstanceDetails.
        Display Name


        :param display_name: The display_name of this UpdateVbsInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_resource_usage_agreement_granted(self):
        """
        Gets the is_resource_usage_agreement_granted of this UpdateVbsInstanceDetails.
        Whether VBS is authorized to create and use resources in the customer tenancy


        :return: The is_resource_usage_agreement_granted of this UpdateVbsInstanceDetails.
        :rtype: bool
        """
        return self._is_resource_usage_agreement_granted

    @is_resource_usage_agreement_granted.setter
    def is_resource_usage_agreement_granted(self, is_resource_usage_agreement_granted):
        """
        Sets the is_resource_usage_agreement_granted of this UpdateVbsInstanceDetails.
        Whether VBS is authorized to create and use resources in the customer tenancy


        :param is_resource_usage_agreement_granted: The is_resource_usage_agreement_granted of this UpdateVbsInstanceDetails.
        :type: bool
        """
        self._is_resource_usage_agreement_granted = is_resource_usage_agreement_granted

    @property
    def resource_compartment_id(self):
        """
        Gets the resource_compartment_id of this UpdateVbsInstanceDetails.
        Compartment where VBS may create additional resources for the service instance


        :return: The resource_compartment_id of this UpdateVbsInstanceDetails.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this UpdateVbsInstanceDetails.
        Compartment where VBS may create additional resources for the service instance


        :param resource_compartment_id: The resource_compartment_id of this UpdateVbsInstanceDetails.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVbsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateVbsInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVbsInstanceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateVbsInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVbsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateVbsInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVbsInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateVbsInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
