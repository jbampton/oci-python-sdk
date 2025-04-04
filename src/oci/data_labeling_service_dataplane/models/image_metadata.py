# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211001

from .record_metadata import RecordMetadata
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageMetadata(RecordMetadata):
    """
    Collection of metadata related to image record.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageMetadata object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service_dataplane.models.ImageMetadata.record_type` attribute
        of this class is ``IMAGE_METADATA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param record_type:
            The value to assign to the record_type property of this ImageMetadata.
            Allowed values for this property are: "IMAGE_METADATA", "TEXT_METADATA", "DOCUMENT_METADATA"
        :type record_type: str

        :param height:
            The value to assign to the height property of this ImageMetadata.
        :type height: int

        :param width:
            The value to assign to the width property of this ImageMetadata.
        :type width: int

        :param depth:
            The value to assign to the depth property of this ImageMetadata.
        :type depth: int

        """
        self.swagger_types = {
            'record_type': 'str',
            'height': 'int',
            'width': 'int',
            'depth': 'int'
        }
        self.attribute_map = {
            'record_type': 'recordType',
            'height': 'height',
            'width': 'width',
            'depth': 'depth'
        }
        self._record_type = None
        self._height = None
        self._width = None
        self._depth = None
        self._record_type = 'IMAGE_METADATA'

    @property
    def height(self):
        """
        Gets the height of this ImageMetadata.
        Height of the image record.


        :return: The height of this ImageMetadata.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ImageMetadata.
        Height of the image record.


        :param height: The height of this ImageMetadata.
        :type: int
        """
        self._height = height

    @property
    def width(self):
        """
        Gets the width of this ImageMetadata.
        Width of the image record.


        :return: The width of this ImageMetadata.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ImageMetadata.
        Width of the image record.


        :param width: The width of this ImageMetadata.
        :type: int
        """
        self._width = width

    @property
    def depth(self):
        """
        Gets the depth of this ImageMetadata.
        Depth of the image record.


        :return: The depth of this ImageMetadata.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """
        Sets the depth of this ImageMetadata.
        Depth of the image record.


        :param depth: The depth of this ImageMetadata.
        :type: int
        """
        self._depth = depth

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
