# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AppFlatFileConnectorBundle(object):
    """
    Flat file connector bundle to sync from a flat file.

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AppFlatFileConnectorBundle object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this AppFlatFileConnectorBundle.
        :type value: str

        :param ref:
            The value to assign to the ref property of this AppFlatFileConnectorBundle.
        :type ref: str

        :param display:
            The value to assign to the display property of this AppFlatFileConnectorBundle.
        :type display: str

        :param well_known_id:
            The value to assign to the well_known_id property of this AppFlatFileConnectorBundle.
        :type well_known_id: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'well_known_id': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'well_known_id': 'wellKnownId'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._well_known_id = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AppFlatFileConnectorBundle.
        ConnectorBundle identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this AppFlatFileConnectorBundle.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AppFlatFileConnectorBundle.
        ConnectorBundle identifier

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this AppFlatFileConnectorBundle.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this AppFlatFileConnectorBundle.
        ConnectorBundle URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this AppFlatFileConnectorBundle.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this AppFlatFileConnectorBundle.
        ConnectorBundle URI

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this AppFlatFileConnectorBundle.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this AppFlatFileConnectorBundle.
        ConnectorBundle display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this AppFlatFileConnectorBundle.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this AppFlatFileConnectorBundle.
        ConnectorBundle display name

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this AppFlatFileConnectorBundle.
        :type: str
        """
        self._display = display

    @property
    def well_known_id(self):
        """
        Gets the well_known_id of this AppFlatFileConnectorBundle.
        Unique well-known identifier used to reference connector bundle.

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The well_known_id of this AppFlatFileConnectorBundle.
        :rtype: str
        """
        return self._well_known_id

    @well_known_id.setter
    def well_known_id(self, well_known_id):
        """
        Sets the well_known_id of this AppFlatFileConnectorBundle.
        Unique well-known identifier used to reference connector bundle.

        **Added In:** 19.1.4

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: immutable
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param well_known_id: The well_known_id of this AppFlatFileConnectorBundle.
        :type: str
        """
        self._well_known_id = well_known_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
