# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ForcePatchPipelineDetails(object):
    """
    force patching a pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ForcePatchPipelineDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pipeline_id:
            The value to assign to the pipeline_id property of this ForcePatchPipelineDetails.
        :type pipeline_id: str

        :param flex_shape:
            The value to assign to the flex_shape property of this ForcePatchPipelineDetails.
        :type flex_shape: str

        """
        self.swagger_types = {
            'pipeline_id': 'str',
            'flex_shape': 'str'
        }

        self.attribute_map = {
            'pipeline_id': 'pipelineId',
            'flex_shape': 'flexShape'
        }

        self._pipeline_id = None
        self._flex_shape = None

    @property
    def pipeline_id(self):
        """
        **[Required]** Gets the pipeline_id of this ForcePatchPipelineDetails.
        OCID of the Opensearch Pipeline.


        :return: The pipeline_id of this ForcePatchPipelineDetails.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """
        Sets the pipeline_id of this ForcePatchPipelineDetails.
        OCID of the Opensearch Pipeline.


        :param pipeline_id: The pipeline_id of this ForcePatchPipelineDetails.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def flex_shape(self):
        """
        Gets the flex_shape of this ForcePatchPipelineDetails.
        flex shape name for the instances in the pipeline


        :return: The flex_shape of this ForcePatchPipelineDetails.
        :rtype: str
        """
        return self._flex_shape

    @flex_shape.setter
    def flex_shape(self, flex_shape):
        """
        Sets the flex_shape of this ForcePatchPipelineDetails.
        flex shape name for the instances in the pipeline


        :param flex_shape: The flex_shape of this ForcePatchPipelineDetails.
        :type: str
        """
        self._flex_shape = flex_shape

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
