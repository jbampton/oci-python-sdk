# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240430

from .patch_instruction import PatchInstruction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchRequireInstruction(PatchInstruction):
    """
    A precondition operation that requires a selection to be non-empty, and optionally to include an item with a specified value
    (useful for asserting that a value exists before attempting to update it, avoiding accidental creation).
    It fails if the selection is empty, or if value is provided and no item of the selection matches it.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PatchRequireInstruction object with values from keyword arguments. The default value of the :py:attr:`~oci.demand_signal.models.PatchRequireInstruction.operation` attribute
        of this class is ``REQUIRE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this PatchRequireInstruction.
            Allowed values for this property are: "REQUIRE", "PROHIBIT", "REPLACE", "INSERT", "REMOVE", "MOVE", "MERGE"
        :type operation: str

        :param selection:
            The value to assign to the selection property of this PatchRequireInstruction.
        :type selection: str

        :param value:
            The value to assign to the value property of this PatchRequireInstruction.
        :type value: object

        """
        self.swagger_types = {
            'operation': 'str',
            'selection': 'str',
            'value': 'object'
        }

        self.attribute_map = {
            'operation': 'operation',
            'selection': 'selection',
            'value': 'value'
        }

        self._operation = None
        self._selection = None
        self._value = None
        self._operation = 'REQUIRE'

    @property
    def value(self):
        """
        Gets the value of this PatchRequireInstruction.
        A value to be compared against each item of the selection.
        If this value is an object, then it matches any item that would be unaffected by applying this value as a merge operation.
        Otherwise, it matches any item to which it is equal according to the rules of `JSON Schema`__.

        __ https://tools.ietf.org/html/draft-handrews-json-schema-00#section-4.2.3


        :return: The value of this PatchRequireInstruction.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this PatchRequireInstruction.
        A value to be compared against each item of the selection.
        If this value is an object, then it matches any item that would be unaffected by applying this value as a merge operation.
        Otherwise, it matches any item to which it is equal according to the rules of `JSON Schema`__.

        __ https://tools.ietf.org/html/draft-handrews-json-schema-00#section-4.2.3


        :param value: The value of this PatchRequireInstruction.
        :type: object
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
