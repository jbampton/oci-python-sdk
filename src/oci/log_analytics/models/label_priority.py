# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LabelPriority(object):
    """
    The label priority.
    """

    #: A constant which can be used with the priority property of a LabelPriority.
    #: This constant has a value of "NONE"
    PRIORITY_NONE = "NONE"

    #: A constant which can be used with the priority property of a LabelPriority.
    #: This constant has a value of "LOW"
    PRIORITY_LOW = "LOW"

    #: A constant which can be used with the priority property of a LabelPriority.
    #: This constant has a value of "MEDIUM"
    PRIORITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the priority property of a LabelPriority.
    #: This constant has a value of "HIGH"
    PRIORITY_HIGH = "HIGH"

    def __init__(self, **kwargs):
        """
        Initializes a new LabelPriority object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param priority:
            The value to assign to the priority property of this LabelPriority.
            Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type priority: str

        """
        self.swagger_types = {
            'priority': 'str'
        }

        self.attribute_map = {
            'priority': 'priority'
        }

        self._priority = None

    @property
    def priority(self):
        """
        Gets the priority of this LabelPriority.
        The label priority. Default value is NONE.

        Allowed values for this property are: "NONE", "LOW", "MEDIUM", "HIGH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The priority of this LabelPriority.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this LabelPriority.
        The label priority. Default value is NONE.


        :param priority: The priority of this LabelPriority.
        :type: str
        """
        allowed_values = ["NONE", "LOW", "MEDIUM", "HIGH"]
        if not value_allowed_none_or_none_sentinel(priority, allowed_values):
            priority = 'UNKNOWN_ENUM_VALUE'
        self._priority = priority

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
