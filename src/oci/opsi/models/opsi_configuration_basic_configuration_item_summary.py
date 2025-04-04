# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630

from .opsi_configuration_configuration_item_summary import OpsiConfigurationConfigurationItemSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiConfigurationBasicConfigurationItemSummary(OpsiConfigurationConfigurationItemSummary):
    """
    Basic configuration item summary. Value and defaultValue fields will contain the custom value stored in the resource and default value from Ops Insights respectively.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiConfigurationBasicConfigurationItemSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.OpsiConfigurationBasicConfigurationItemSummary.config_item_type` attribute
        of this class is ``BASIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_item_type:
            The value to assign to the config_item_type property of this OpsiConfigurationBasicConfigurationItemSummary.
            Allowed values for this property are: "BASIC"
        :type config_item_type: str

        :param name:
            The value to assign to the name property of this OpsiConfigurationBasicConfigurationItemSummary.
        :type name: str

        :param value:
            The value to assign to the value property of this OpsiConfigurationBasicConfigurationItemSummary.
        :type value: str

        :param default_value:
            The value to assign to the default_value property of this OpsiConfigurationBasicConfigurationItemSummary.
        :type default_value: str

        :param applicable_contexts:
            The value to assign to the applicable_contexts property of this OpsiConfigurationBasicConfigurationItemSummary.
        :type applicable_contexts: list[str]

        :param metadata:
            The value to assign to the metadata property of this OpsiConfigurationBasicConfigurationItemSummary.
        :type metadata: oci.opsi.models.ConfigurationItemMetadata

        """
        self.swagger_types = {
            'config_item_type': 'str',
            'name': 'str',
            'value': 'str',
            'default_value': 'str',
            'applicable_contexts': 'list[str]',
            'metadata': 'ConfigurationItemMetadata'
        }
        self.attribute_map = {
            'config_item_type': 'configItemType',
            'name': 'name',
            'value': 'value',
            'default_value': 'defaultValue',
            'applicable_contexts': 'applicableContexts',
            'metadata': 'metadata'
        }
        self._config_item_type = None
        self._name = None
        self._value = None
        self._default_value = None
        self._applicable_contexts = None
        self._metadata = None
        self._config_item_type = 'BASIC'

    @property
    def name(self):
        """
        Gets the name of this OpsiConfigurationBasicConfigurationItemSummary.
        Name of configuration item.


        :return: The name of this OpsiConfigurationBasicConfigurationItemSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OpsiConfigurationBasicConfigurationItemSummary.
        Name of configuration item.


        :param name: The name of this OpsiConfigurationBasicConfigurationItemSummary.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """
        Gets the value of this OpsiConfigurationBasicConfigurationItemSummary.
        Value of configuration item.


        :return: The value of this OpsiConfigurationBasicConfigurationItemSummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this OpsiConfigurationBasicConfigurationItemSummary.
        Value of configuration item.


        :param value: The value of this OpsiConfigurationBasicConfigurationItemSummary.
        :type: str
        """
        self._value = value

    @property
    def default_value(self):
        """
        Gets the default_value of this OpsiConfigurationBasicConfigurationItemSummary.
        Value of configuration item.


        :return: The default_value of this OpsiConfigurationBasicConfigurationItemSummary.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this OpsiConfigurationBasicConfigurationItemSummary.
        Value of configuration item.


        :param default_value: The default_value of this OpsiConfigurationBasicConfigurationItemSummary.
        :type: str
        """
        self._default_value = default_value

    @property
    def applicable_contexts(self):
        """
        Gets the applicable_contexts of this OpsiConfigurationBasicConfigurationItemSummary.
        List of contexts in Operations Insights where this configuration item is applicable.


        :return: The applicable_contexts of this OpsiConfigurationBasicConfigurationItemSummary.
        :rtype: list[str]
        """
        return self._applicable_contexts

    @applicable_contexts.setter
    def applicable_contexts(self, applicable_contexts):
        """
        Sets the applicable_contexts of this OpsiConfigurationBasicConfigurationItemSummary.
        List of contexts in Operations Insights where this configuration item is applicable.


        :param applicable_contexts: The applicable_contexts of this OpsiConfigurationBasicConfigurationItemSummary.
        :type: list[str]
        """
        self._applicable_contexts = applicable_contexts

    @property
    def metadata(self):
        """
        Gets the metadata of this OpsiConfigurationBasicConfigurationItemSummary.

        :return: The metadata of this OpsiConfigurationBasicConfigurationItemSummary.
        :rtype: oci.opsi.models.ConfigurationItemMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this OpsiConfigurationBasicConfigurationItemSummary.

        :param metadata: The metadata of this OpsiConfigurationBasicConfigurationItemSummary.
        :type: oci.opsi.models.ConfigurationItemMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
