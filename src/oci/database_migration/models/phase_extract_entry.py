# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PhaseExtractEntry(object):
    """
    Job phase extract message.
    """

    #: A constant which can be used with the type property of a PhaseExtractEntry.
    #: This constant has a value of "ERROR"
    TYPE_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new PhaseExtractEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PhaseExtractEntry.
            Allowed values for this property are: "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param message:
            The value to assign to the message property of this PhaseExtractEntry.
        :type message: str

        """
        self.swagger_types = {
            'type': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'message': 'message'
        }

        self._type = None
        self._message = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this PhaseExtractEntry.
        Type of extract.

        Allowed values for this property are: "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this PhaseExtractEntry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PhaseExtractEntry.
        Type of extract.


        :param type: The type of this PhaseExtractEntry.
        :type: str
        """
        allowed_values = ["ERROR"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def message(self):
        """
        **[Required]** Gets the message of this PhaseExtractEntry.
        Message in entry.


        :return: The message of this PhaseExtractEntry.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this PhaseExtractEntry.
        Message in entry.


        :param message: The message of this PhaseExtractEntry.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
