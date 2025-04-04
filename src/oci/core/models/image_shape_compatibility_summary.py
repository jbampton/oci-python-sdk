# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageShapeCompatibilitySummary(object):
    """
    Summary information for a compatible image and shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageShapeCompatibilitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param image_id:
            The value to assign to the image_id property of this ImageShapeCompatibilitySummary.
        :type image_id: str

        :param shape:
            The value to assign to the shape property of this ImageShapeCompatibilitySummary.
        :type shape: str

        :param memory_constraints:
            The value to assign to the memory_constraints property of this ImageShapeCompatibilitySummary.
        :type memory_constraints: oci.core.models.ImageMemoryConstraints

        :param ocpu_constraints:
            The value to assign to the ocpu_constraints property of this ImageShapeCompatibilitySummary.
        :type ocpu_constraints: oci.core.models.ImageOcpuConstraints

        """
        self.swagger_types = {
            'image_id': 'str',
            'shape': 'str',
            'memory_constraints': 'ImageMemoryConstraints',
            'ocpu_constraints': 'ImageOcpuConstraints'
        }
        self.attribute_map = {
            'image_id': 'imageId',
            'shape': 'shape',
            'memory_constraints': 'memoryConstraints',
            'ocpu_constraints': 'ocpuConstraints'
        }
        self._image_id = None
        self._shape = None
        self._memory_constraints = None
        self._ocpu_constraints = None

    @property
    def image_id(self):
        """
        **[Required]** Gets the image_id of this ImageShapeCompatibilitySummary.
        The image `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The image_id of this ImageShapeCompatibilitySummary.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ImageShapeCompatibilitySummary.
        The image `OCID`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param image_id: The image_id of this ImageShapeCompatibilitySummary.
        :type: str
        """
        self._image_id = image_id

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this ImageShapeCompatibilitySummary.
        The shape name.


        :return: The shape of this ImageShapeCompatibilitySummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this ImageShapeCompatibilitySummary.
        The shape name.


        :param shape: The shape of this ImageShapeCompatibilitySummary.
        :type: str
        """
        self._shape = shape

    @property
    def memory_constraints(self):
        """
        Gets the memory_constraints of this ImageShapeCompatibilitySummary.

        :return: The memory_constraints of this ImageShapeCompatibilitySummary.
        :rtype: oci.core.models.ImageMemoryConstraints
        """
        return self._memory_constraints

    @memory_constraints.setter
    def memory_constraints(self, memory_constraints):
        """
        Sets the memory_constraints of this ImageShapeCompatibilitySummary.

        :param memory_constraints: The memory_constraints of this ImageShapeCompatibilitySummary.
        :type: oci.core.models.ImageMemoryConstraints
        """
        self._memory_constraints = memory_constraints

    @property
    def ocpu_constraints(self):
        """
        Gets the ocpu_constraints of this ImageShapeCompatibilitySummary.

        :return: The ocpu_constraints of this ImageShapeCompatibilitySummary.
        :rtype: oci.core.models.ImageOcpuConstraints
        """
        return self._ocpu_constraints

    @ocpu_constraints.setter
    def ocpu_constraints(self, ocpu_constraints):
        """
        Sets the ocpu_constraints of this ImageShapeCompatibilitySummary.

        :param ocpu_constraints: The ocpu_constraints of this ImageShapeCompatibilitySummary.
        :type: oci.core.models.ImageOcpuConstraints
        """
        self._ocpu_constraints = ocpu_constraints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
