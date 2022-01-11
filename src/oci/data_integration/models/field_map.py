# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldMap(object):
    """
    A field map is a way to map a source row shape to a target row shape that may be different.
    """

    #: A constant which can be used with the model_type property of a FieldMap.
    #: This constant has a value of "DIRECT_NAMED_FIELD_MAP"
    MODEL_TYPE_DIRECT_NAMED_FIELD_MAP = "DIRECT_NAMED_FIELD_MAP"

    #: A constant which can be used with the model_type property of a FieldMap.
    #: This constant has a value of "COMPOSITE_FIELD_MAP"
    MODEL_TYPE_COMPOSITE_FIELD_MAP = "COMPOSITE_FIELD_MAP"

    #: A constant which can be used with the model_type property of a FieldMap.
    #: This constant has a value of "DIRECT_FIELD_MAP"
    MODEL_TYPE_DIRECT_FIELD_MAP = "DIRECT_FIELD_MAP"

    #: A constant which can be used with the model_type property of a FieldMap.
    #: This constant has a value of "RULE_BASED_FIELD_MAP"
    MODEL_TYPE_RULE_BASED_FIELD_MAP = "RULE_BASED_FIELD_MAP"

    def __init__(self, **kwargs):
        """
        Initializes a new FieldMap object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.RuleBasedFieldMap`
        * :class:`~oci.data_integration.models.DirectFieldMap`
        * :class:`~oci.data_integration.models.CompositeFieldMap`
        * :class:`~oci.data_integration.models.DirectNamedFieldMap`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this FieldMap.
            Allowed values for this property are: "DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param description:
            The value to assign to the description property of this FieldMap.
        :type description: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'description': 'description'
        }

        self._model_type = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'RULE_BASED_FIELD_MAP':
            return 'RuleBasedFieldMap'

        if type == 'DIRECT_FIELD_MAP':
            return 'DirectFieldMap'

        if type == 'COMPOSITE_FIELD_MAP':
            return 'CompositeFieldMap'

        if type == 'DIRECT_NAMED_FIELD_MAP':
            return 'DirectNamedFieldMap'
        else:
            return 'FieldMap'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this FieldMap.
        The model type for the field map.

        Allowed values for this property are: "DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this FieldMap.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FieldMap.
        The model type for the field map.


        :param model_type: The model_type of this FieldMap.
        :type: str
        """
        allowed_values = ["DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def description(self):
        """
        Gets the description of this FieldMap.
        Detailed description for the object.


        :return: The description of this FieldMap.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FieldMap.
        Detailed description for the object.


        :param description: The description of this FieldMap.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
