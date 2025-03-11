# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180828


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpensearchClusterPipelineSummary(object):
    """
    The summary of information about an OpenSearch cluster Pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OpensearchClusterPipelineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpensearchClusterPipelineSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OpensearchClusterPipelineSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpensearchClusterPipelineSummary.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this OpensearchClusterPipelineSummary.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this OpensearchClusterPipelineSummary.
        :type subnet_id: str

        :param ocpu_count:
            The value to assign to the ocpu_count property of this OpensearchClusterPipelineSummary.
        :type ocpu_count: int

        :param memory_gb:
            The value to assign to the memory_gb property of this OpensearchClusterPipelineSummary.
        :type memory_gb: int

        :param node_count:
            The value to assign to the node_count property of this OpensearchClusterPipelineSummary.
        :type node_count: int

        :param pipeline_configuration_body:
            The value to assign to the pipeline_configuration_body property of this OpensearchClusterPipelineSummary.
        :type pipeline_configuration_body: str

        :param data_prepper_configuration_body:
            The value to assign to the data_prepper_configuration_body property of this OpensearchClusterPipelineSummary.
        :type data_prepper_configuration_body: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpensearchClusterPipelineSummary.
        :type lifecycle_state: str

        :param pipeline_mode:
            The value to assign to the pipeline_mode property of this OpensearchClusterPipelineSummary.
        :type pipeline_mode: str

        :param time_created:
            The value to assign to the time_created property of this OpensearchClusterPipelineSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpensearchClusterPipelineSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpensearchClusterPipelineSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpensearchClusterPipelineSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpensearchClusterPipelineSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'ocpu_count': 'int',
            'memory_gb': 'int',
            'node_count': 'int',
            'pipeline_configuration_body': 'str',
            'data_prepper_configuration_body': 'str',
            'lifecycle_state': 'str',
            'pipeline_mode': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'ocpu_count': 'ocpuCount',
            'memory_gb': 'memoryGB',
            'node_count': 'nodeCount',
            'pipeline_configuration_body': 'pipelineConfigurationBody',
            'data_prepper_configuration_body': 'dataPrepperConfigurationBody',
            'lifecycle_state': 'lifecycleState',
            'pipeline_mode': 'pipelineMode',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._ocpu_count = None
        self._memory_gb = None
        self._node_count = None
        self._pipeline_configuration_body = None
        self._data_prepper_configuration_body = None
        self._lifecycle_state = None
        self._pipeline_mode = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OpensearchClusterPipelineSummary.
        The OCID of the cluster pipeline.


        :return: The id of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpensearchClusterPipelineSummary.
        The OCID of the cluster pipeline.


        :param id: The id of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this OpensearchClusterPipelineSummary.
        The name of the cluster pipeline. Avoid entering confidential information.


        :return: The display_name of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpensearchClusterPipelineSummary.
        The name of the cluster pipeline. Avoid entering confidential information.


        :param display_name: The display_name of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OpensearchClusterPipelineSummary.
        The OCID of the compartment where the cluster pipeline is located.


        :return: The compartment_id of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpensearchClusterPipelineSummary.
        The OCID of the compartment where the cluster pipeline is located.


        :param compartment_id: The compartment_id of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this OpensearchClusterPipelineSummary.
        The OCID of the pipeline's VCN.


        :return: The vcn_id of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this OpensearchClusterPipelineSummary.
        The OCID of the pipeline's VCN.


        :param vcn_id: The vcn_id of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this OpensearchClusterPipelineSummary.
        The OCID of the pipeline's subnet.


        :return: The subnet_id of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this OpensearchClusterPipelineSummary.
        The OCID of the pipeline's subnet.


        :param subnet_id: The subnet_id of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ocpu_count(self):
        """
        **[Required]** Gets the ocpu_count of this OpensearchClusterPipelineSummary.
        The number of OCPUs configured for each pipeline node.


        :return: The ocpu_count of this OpensearchClusterPipelineSummary.
        :rtype: int
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this OpensearchClusterPipelineSummary.
        The number of OCPUs configured for each pipeline node.


        :param ocpu_count: The ocpu_count of this OpensearchClusterPipelineSummary.
        :type: int
        """
        self._ocpu_count = ocpu_count

    @property
    def memory_gb(self):
        """
        **[Required]** Gets the memory_gb of this OpensearchClusterPipelineSummary.
        The amount of memory in GB, for each pipeline node.


        :return: The memory_gb of this OpensearchClusterPipelineSummary.
        :rtype: int
        """
        return self._memory_gb

    @memory_gb.setter
    def memory_gb(self, memory_gb):
        """
        Sets the memory_gb of this OpensearchClusterPipelineSummary.
        The amount of memory in GB, for each pipeline node.


        :param memory_gb: The memory_gb of this OpensearchClusterPipelineSummary.
        :type: int
        """
        self._memory_gb = memory_gb

    @property
    def node_count(self):
        """
        **[Required]** Gets the node_count of this OpensearchClusterPipelineSummary.
        The number of nodes configured for the pipeline.


        :return: The node_count of this OpensearchClusterPipelineSummary.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this OpensearchClusterPipelineSummary.
        The number of nodes configured for the pipeline.


        :param node_count: The node_count of this OpensearchClusterPipelineSummary.
        :type: int
        """
        self._node_count = node_count

    @property
    def pipeline_configuration_body(self):
        """
        **[Required]** Gets the pipeline_configuration_body of this OpensearchClusterPipelineSummary.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :return: The pipeline_configuration_body of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._pipeline_configuration_body

    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, pipeline_configuration_body):
        """
        Sets the pipeline_configuration_body of this OpensearchClusterPipelineSummary.
        The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :param pipeline_configuration_body: The pipeline_configuration_body of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._pipeline_configuration_body = pipeline_configuration_body

    @property
    def data_prepper_configuration_body(self):
        """
        **[Required]** Gets the data_prepper_configuration_body of this OpensearchClusterPipelineSummary.
        The data prepper config in YAML format. The command accepts the data prepper config as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :return: The data_prepper_configuration_body of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._data_prepper_configuration_body

    @data_prepper_configuration_body.setter
    def data_prepper_configuration_body(self, data_prepper_configuration_body):
        """
        Sets the data_prepper_configuration_body of this OpensearchClusterPipelineSummary.
        The data prepper config in YAML format. The command accepts the data prepper config as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with \\.


        :param data_prepper_configuration_body: The data_prepper_configuration_body of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._data_prepper_configuration_body = data_prepper_configuration_body

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OpensearchClusterPipelineSummary.
        The current state of the cluster pipeline.


        :return: The lifecycle_state of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpensearchClusterPipelineSummary.
        The current state of the cluster pipeline.


        :param lifecycle_state: The lifecycle_state of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def pipeline_mode(self):
        """
        **[Required]** Gets the pipeline_mode of this OpensearchClusterPipelineSummary.
        The current state of the pipeline.


        :return: The pipeline_mode of this OpensearchClusterPipelineSummary.
        :rtype: str
        """
        return self._pipeline_mode

    @pipeline_mode.setter
    def pipeline_mode(self, pipeline_mode):
        """
        Sets the pipeline_mode of this OpensearchClusterPipelineSummary.
        The current state of the pipeline.


        :param pipeline_mode: The pipeline_mode of this OpensearchClusterPipelineSummary.
        :type: str
        """
        self._pipeline_mode = pipeline_mode

    @property
    def time_created(self):
        """
        Gets the time_created of this OpensearchClusterPipelineSummary.
        The date and time the cluster pipeline was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OpensearchClusterPipelineSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpensearchClusterPipelineSummary.
        The date and time the cluster pipeline was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OpensearchClusterPipelineSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpensearchClusterPipelineSummary.
        The date and time the cluster pipeline was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this OpensearchClusterPipelineSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpensearchClusterPipelineSummary.
        The date and time the cluster pipeline was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this OpensearchClusterPipelineSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpensearchClusterPipelineSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpensearchClusterPipelineSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpensearchClusterPipelineSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpensearchClusterPipelineSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpensearchClusterPipelineSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpensearchClusterPipelineSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpensearchClusterPipelineSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpensearchClusterPipelineSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpensearchClusterPipelineSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpensearchClusterPipelineSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpensearchClusterPipelineSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpensearchClusterPipelineSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
