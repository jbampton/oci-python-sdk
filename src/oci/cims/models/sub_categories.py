# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubCategories(object):
    """
    List of subcategories under a service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubCategories object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_category:
            The value to assign to the service_category property of this SubCategories.
        :type service_category: dict(str, str)

        :param schema:
            The value to assign to the schema property of this SubCategories.
        :type schema: str

        :param has_sub_category:
            The value to assign to the has_sub_category property of this SubCategories.
        :type has_sub_category: str

        :param sub_categories:
            The value to assign to the sub_categories property of this SubCategories.
        :type sub_categories: list[oci.cims.models.SubComponents]

        """
        self.swagger_types = {
            'service_category': 'dict(str, str)',
            'schema': 'str',
            'has_sub_category': 'str',
            'sub_categories': 'list[SubComponents]'
        }

        self.attribute_map = {
            'service_category': 'serviceCategory',
            'schema': 'schema',
            'has_sub_category': 'hasSubCategory',
            'sub_categories': 'subCategories'
        }

        self._service_category = None
        self._schema = None
        self._has_sub_category = None
        self._sub_categories = None

    @property
    def service_category(self):
        """
        Gets the service_category of this SubCategories.
        Subcategory list.


        :return: The service_category of this SubCategories.
        :rtype: dict(str, str)
        """
        return self._service_category

    @service_category.setter
    def service_category(self, service_category):
        """
        Sets the service_category of this SubCategories.
        Subcategory list.


        :param service_category: The service_category of this SubCategories.
        :type: dict(str, str)
        """
        self._service_category = service_category

    @property
    def schema(self):
        """
        Gets the schema of this SubCategories.
        Schema of a subcategory.


        :return: The schema of this SubCategories.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this SubCategories.
        Schema of a subcategory.


        :param schema: The schema of this SubCategories.
        :type: str
        """
        self._schema = schema

    @property
    def has_sub_category(self):
        """
        Gets the has_sub_category of this SubCategories.
        Flag to identify if subComponent is present


        :return: The has_sub_category of this SubCategories.
        :rtype: str
        """
        return self._has_sub_category

    @has_sub_category.setter
    def has_sub_category(self, has_sub_category):
        """
        Sets the has_sub_category of this SubCategories.
        Flag to identify if subComponent is present


        :param has_sub_category: The has_sub_category of this SubCategories.
        :type: str
        """
        self._has_sub_category = has_sub_category

    @property
    def sub_categories(self):
        """
        Gets the sub_categories of this SubCategories.
        The sub component list for MOS Taxonomy.


        :return: The sub_categories of this SubCategories.
        :rtype: list[oci.cims.models.SubComponents]
        """
        return self._sub_categories

    @sub_categories.setter
    def sub_categories(self, sub_categories):
        """
        Sets the sub_categories of this SubCategories.
        The sub component list for MOS Taxonomy.


        :param sub_categories: The sub_categories of this SubCategories.
        :type: list[oci.cims.models.SubComponents]
        """
        self._sub_categories = sub_categories

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
