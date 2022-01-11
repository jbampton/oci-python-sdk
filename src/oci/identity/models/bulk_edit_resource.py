# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkEditResource(object):
    """
    BulkEditResource model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkEditResource object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BulkEditResource.
        :type id: str

        :param resource_type:
            The value to assign to the resource_type property of this BulkEditResource.
        :type resource_type: str

        :param metadata:
            The value to assign to the metadata property of this BulkEditResource.
        :type metadata: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'resource_type': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'resource_type': 'resourceType',
            'metadata': 'metadata'
        }

        self._id = None
        self._resource_type = None
        self._metadata = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BulkEditResource.
        The unique OCID of the resource.


        :return: The id of this BulkEditResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BulkEditResource.
        The unique OCID of the resource.


        :param id: The id of this BulkEditResource.
        :type: str
        """
        self._id = id

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this BulkEditResource.
        The type of resource. See :func:`list_bulk_edit_tags_resource_types`.


        :return: The resource_type of this BulkEditResource.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this BulkEditResource.
        The type of resource. See :func:`list_bulk_edit_tags_resource_types`.


        :param resource_type: The resource_type of this BulkEditResource.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def metadata(self):
        """
        Gets the metadata of this BulkEditResource.
        Additional information that identifies the resource for bulk editing of tags. This information is provided in the resource's API documentation.


        :return: The metadata of this BulkEditResource.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this BulkEditResource.
        Additional information that identifies the resource for bulk editing of tags. This information is provided in the resource's API documentation.


        :param metadata: The metadata of this BulkEditResource.
        :type: dict(str, str)
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
