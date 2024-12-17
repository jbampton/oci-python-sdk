# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330

from .metric_extension_update_query_properties import MetricExtensionUpdateQueryProperties
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JmxUpdateQueryProperties(MetricExtensionUpdateQueryProperties):
    """
    Query Properties applicable to JMX type of collection method
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JmxUpdateQueryProperties object with values from keyword arguments. The default value of the :py:attr:`~oci.stack_monitoring.models.JmxUpdateQueryProperties.collection_method` attribute
        of this class is ``JMX`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param collection_method:
            The value to assign to the collection_method property of this JmxUpdateQueryProperties.
            Allowed values for this property are: "OS_COMMAND", "SQL", "JMX", "HTTP"
        :type collection_method: str

        :param managed_bean_query:
            The value to assign to the managed_bean_query property of this JmxUpdateQueryProperties.
        :type managed_bean_query: str

        :param jmx_attributes:
            The value to assign to the jmx_attributes property of this JmxUpdateQueryProperties.
        :type jmx_attributes: str

        :param identity_metric:
            The value to assign to the identity_metric property of this JmxUpdateQueryProperties.
        :type identity_metric: str

        :param auto_row_prefix:
            The value to assign to the auto_row_prefix property of this JmxUpdateQueryProperties.
        :type auto_row_prefix: str

        :param is_metric_service_enabled:
            The value to assign to the is_metric_service_enabled property of this JmxUpdateQueryProperties.
        :type is_metric_service_enabled: bool

        """
        self.swagger_types = {
            'collection_method': 'str',
            'managed_bean_query': 'str',
            'jmx_attributes': 'str',
            'identity_metric': 'str',
            'auto_row_prefix': 'str',
            'is_metric_service_enabled': 'bool'
        }

        self.attribute_map = {
            'collection_method': 'collectionMethod',
            'managed_bean_query': 'managedBeanQuery',
            'jmx_attributes': 'jmxAttributes',
            'identity_metric': 'identityMetric',
            'auto_row_prefix': 'autoRowPrefix',
            'is_metric_service_enabled': 'isMetricServiceEnabled'
        }

        self._collection_method = None
        self._managed_bean_query = None
        self._jmx_attributes = None
        self._identity_metric = None
        self._auto_row_prefix = None
        self._is_metric_service_enabled = None
        self._collection_method = 'JMX'

    @property
    def managed_bean_query(self):
        """
        Gets the managed_bean_query of this JmxUpdateQueryProperties.
        JMX Managed Bean Query or Metric Service Table name


        :return: The managed_bean_query of this JmxUpdateQueryProperties.
        :rtype: str
        """
        return self._managed_bean_query

    @managed_bean_query.setter
    def managed_bean_query(self, managed_bean_query):
        """
        Sets the managed_bean_query of this JmxUpdateQueryProperties.
        JMX Managed Bean Query or Metric Service Table name


        :param managed_bean_query: The managed_bean_query of this JmxUpdateQueryProperties.
        :type: str
        """
        self._managed_bean_query = managed_bean_query

    @property
    def jmx_attributes(self):
        """
        Gets the jmx_attributes of this JmxUpdateQueryProperties.
        List of JMX attributes or Metric Service Table columns separated by semi-colon


        :return: The jmx_attributes of this JmxUpdateQueryProperties.
        :rtype: str
        """
        return self._jmx_attributes

    @jmx_attributes.setter
    def jmx_attributes(self, jmx_attributes):
        """
        Sets the jmx_attributes of this JmxUpdateQueryProperties.
        List of JMX attributes or Metric Service Table columns separated by semi-colon


        :param jmx_attributes: The jmx_attributes of this JmxUpdateQueryProperties.
        :type: str
        """
        self._jmx_attributes = jmx_attributes

    @property
    def identity_metric(self):
        """
        Gets the identity_metric of this JmxUpdateQueryProperties.
        Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics


        :return: The identity_metric of this JmxUpdateQueryProperties.
        :rtype: str
        """
        return self._identity_metric

    @identity_metric.setter
    def identity_metric(self, identity_metric):
        """
        Sets the identity_metric of this JmxUpdateQueryProperties.
        Semi-colon separated list of key properties from Managed Bean ObjectName to be used as key metrics


        :param identity_metric: The identity_metric of this JmxUpdateQueryProperties.
        :type: str
        """
        self._identity_metric = identity_metric

    @property
    def auto_row_prefix(self):
        """
        Gets the auto_row_prefix of this JmxUpdateQueryProperties.
        Prefix for an auto generated metric, in case multiple rows with non unique key values are returned


        :return: The auto_row_prefix of this JmxUpdateQueryProperties.
        :rtype: str
        """
        return self._auto_row_prefix

    @auto_row_prefix.setter
    def auto_row_prefix(self, auto_row_prefix):
        """
        Sets the auto_row_prefix of this JmxUpdateQueryProperties.
        Prefix for an auto generated metric, in case multiple rows with non unique key values are returned


        :param auto_row_prefix: The auto_row_prefix of this JmxUpdateQueryProperties.
        :type: str
        """
        self._auto_row_prefix = auto_row_prefix

    @property
    def is_metric_service_enabled(self):
        """
        Gets the is_metric_service_enabled of this JmxUpdateQueryProperties.
        Indicates if Metric Service is enabled on server domain


        :return: The is_metric_service_enabled of this JmxUpdateQueryProperties.
        :rtype: bool
        """
        return self._is_metric_service_enabled

    @is_metric_service_enabled.setter
    def is_metric_service_enabled(self, is_metric_service_enabled):
        """
        Sets the is_metric_service_enabled of this JmxUpdateQueryProperties.
        Indicates if Metric Service is enabled on server domain


        :param is_metric_service_enabled: The is_metric_service_enabled of this JmxUpdateQueryProperties.
        :type: bool
        """
        self._is_metric_service_enabled = is_metric_service_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
