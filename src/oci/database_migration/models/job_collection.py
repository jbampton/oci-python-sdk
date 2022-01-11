# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobCollection(object):
    """
    Results of a Job search. Contains JobSummary items.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this JobCollection.
        :type items: list[oci.database_migration.models.JobSummary]

        """
        self.swagger_types = {
            'items': 'list[JobSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this JobCollection.
        Items in collection.


        :return: The items of this JobCollection.
        :rtype: list[oci.database_migration.models.JobSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this JobCollection.
        Items in collection.


        :param items: The items of this JobCollection.
        :type: list[oci.database_migration.models.JobSummary]
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
