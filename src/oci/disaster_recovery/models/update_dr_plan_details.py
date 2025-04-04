# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrPlanDetails(object):
    """
    The details for updating a DR plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrPlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDrPlanDetails.
        :type display_name: str

        :param plan_groups:
            The value to assign to the plan_groups property of this UpdateDrPlanDetails.
        :type plan_groups: list[oci.disaster_recovery.models.UpdateDrPlanGroupDetails]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDrPlanDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDrPlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'plan_groups': 'list[UpdateDrPlanGroupDetails]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'plan_groups': 'planGroups',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._plan_groups = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrPlanDetails.
        The display name of the DR plan being updated.

        Example: `EBS Switchover PHX to IAD`


        :return: The display_name of this UpdateDrPlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrPlanDetails.
        The display name of the DR plan being updated.

        Example: `EBS Switchover PHX to IAD`


        :param display_name: The display_name of this UpdateDrPlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def plan_groups(self):
        """
        Gets the plan_groups of this UpdateDrPlanDetails.
        An ordered list of groups in a DR plan.


        :return: The plan_groups of this UpdateDrPlanDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateDrPlanGroupDetails]
        """
        return self._plan_groups

    @plan_groups.setter
    def plan_groups(self, plan_groups):
        """
        Sets the plan_groups of this UpdateDrPlanDetails.
        An ordered list of groups in a DR plan.


        :param plan_groups: The plan_groups of this UpdateDrPlanDetails.
        :type: list[oci.disaster_recovery.models.UpdateDrPlanGroupDetails]
        """
        self._plan_groups = plan_groups

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDrPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.

        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this UpdateDrPlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDrPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.

        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this UpdateDrPlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDrPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this UpdateDrPlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDrPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this UpdateDrPlanDetails.
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
