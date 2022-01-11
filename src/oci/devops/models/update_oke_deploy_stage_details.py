# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOkeDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies the Kubernetes cluster deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOkeDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateOkeDeployStageDetails.deploy_stage_type` attribute
        of this class is ``OKE_DEPLOYMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateOkeDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOkeDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateOkeDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateOkeDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOkeDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOkeDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param oke_cluster_deploy_environment_id:
            The value to assign to the oke_cluster_deploy_environment_id property of this UpdateOkeDeployStageDetails.
        :type oke_cluster_deploy_environment_id: str

        :param kubernetes_manifest_deploy_artifact_ids:
            The value to assign to the kubernetes_manifest_deploy_artifact_ids property of this UpdateOkeDeployStageDetails.
        :type kubernetes_manifest_deploy_artifact_ids: list[str]

        :param namespace:
            The value to assign to the namespace property of this UpdateOkeDeployStageDetails.
        :type namespace: str

        :param rollback_policy:
            The value to assign to the rollback_policy property of this UpdateOkeDeployStageDetails.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'oke_cluster_deploy_environment_id': 'str',
            'kubernetes_manifest_deploy_artifact_ids': 'list[str]',
            'namespace': 'str',
            'rollback_policy': 'DeployStageRollbackPolicy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'oke_cluster_deploy_environment_id': 'okeClusterDeployEnvironmentId',
            'kubernetes_manifest_deploy_artifact_ids': 'kubernetesManifestDeployArtifactIds',
            'namespace': 'namespace',
            'rollback_policy': 'rollbackPolicy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._oke_cluster_deploy_environment_id = None
        self._kubernetes_manifest_deploy_artifact_ids = None
        self._namespace = None
        self._rollback_policy = None
        self._deploy_stage_type = 'OKE_DEPLOYMENT'

    @property
    def oke_cluster_deploy_environment_id(self):
        """
        Gets the oke_cluster_deploy_environment_id of this UpdateOkeDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :return: The oke_cluster_deploy_environment_id of this UpdateOkeDeployStageDetails.
        :rtype: str
        """
        return self._oke_cluster_deploy_environment_id

    @oke_cluster_deploy_environment_id.setter
    def oke_cluster_deploy_environment_id(self, oke_cluster_deploy_environment_id):
        """
        Sets the oke_cluster_deploy_environment_id of this UpdateOkeDeployStageDetails.
        Kubernetes cluster environment OCID for deployment.


        :param oke_cluster_deploy_environment_id: The oke_cluster_deploy_environment_id of this UpdateOkeDeployStageDetails.
        :type: str
        """
        self._oke_cluster_deploy_environment_id = oke_cluster_deploy_environment_id

    @property
    def kubernetes_manifest_deploy_artifact_ids(self):
        """
        Gets the kubernetes_manifest_deploy_artifact_ids of this UpdateOkeDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.


        :return: The kubernetes_manifest_deploy_artifact_ids of this UpdateOkeDeployStageDetails.
        :rtype: list[str]
        """
        return self._kubernetes_manifest_deploy_artifact_ids

    @kubernetes_manifest_deploy_artifact_ids.setter
    def kubernetes_manifest_deploy_artifact_ids(self, kubernetes_manifest_deploy_artifact_ids):
        """
        Sets the kubernetes_manifest_deploy_artifact_ids of this UpdateOkeDeployStageDetails.
        List of Kubernetes manifest artifact OCIDs, the manifests should not include any job resource.


        :param kubernetes_manifest_deploy_artifact_ids: The kubernetes_manifest_deploy_artifact_ids of this UpdateOkeDeployStageDetails.
        :type: list[str]
        """
        self._kubernetes_manifest_deploy_artifact_ids = kubernetes_manifest_deploy_artifact_ids

    @property
    def namespace(self):
        """
        Gets the namespace of this UpdateOkeDeployStageDetails.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :return: The namespace of this UpdateOkeDeployStageDetails.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this UpdateOkeDeployStageDetails.
        Default namespace to be used for Kubernetes deployment when not specified in the manifest.


        :param namespace: The namespace of this UpdateOkeDeployStageDetails.
        :type: str
        """
        self._namespace = namespace

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this UpdateOkeDeployStageDetails.

        :return: The rollback_policy of this UpdateOkeDeployStageDetails.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this UpdateOkeDeployStageDetails.

        :param rollback_policy: The rollback_policy of this UpdateOkeDeployStageDetails.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
