# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileCollection(object):
    """
    The set of registration profiles returned for the :func:`list_profiles` operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this ProfileCollection.
        :type items: list[oci.os_management_hub.models.ProfileSummary]

        """
        self.swagger_types = {
            'items': 'list[ProfileSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ProfileCollection.
        List of registration profiles.


        :return: The items of this ProfileCollection.
        :rtype: list[oci.os_management_hub.models.ProfileSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ProfileCollection.
        List of registration profiles.


        :param items: The items of this ProfileCollection.
        :type: list[oci.os_management_hub.models.ProfileSummary]
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
