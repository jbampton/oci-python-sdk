# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnotationAnalyticsAggregationCollection(object):
    """
    Aggregation entities are required by the api consistency guidelines for API Consistency Guidelines#AnalyticsAPIs.  These are used to summarize annotations for a given dataset and will be used to populate UI elements.  Aggregations need to have the fields that identify the exact scope that they're summarizing.  Any filters to the list API we apply would have to show up in the aggregation. We should limit the number of filters and dimensions as much as possible.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnotationAnalyticsAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this AnnotationAnalyticsAggregationCollection.
        :type items: list[oci.data_labeling_service_dataplane.models.AnnotationAnalyticsAggregation]

        """
        self.swagger_types = {
            'items': 'list[AnnotationAnalyticsAggregation]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AnnotationAnalyticsAggregationCollection.
        List of Annotation entities.


        :return: The items of this AnnotationAnalyticsAggregationCollection.
        :rtype: list[oci.data_labeling_service_dataplane.models.AnnotationAnalyticsAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AnnotationAnalyticsAggregationCollection.
        List of Annotation entities.


        :param items: The items of this AnnotationAnalyticsAggregationCollection.
        :type: list[oci.data_labeling_service_dataplane.models.AnnotationAnalyticsAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
