# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .ca_bundle_response import CaBundleResponse
from .ca_details import CaDetails
from .certificate_details import CertificateDetails
from .change_rover_cluster_compartment_details import ChangeRoverClusterCompartmentDetails
from .change_rover_entitlement_compartment_details import ChangeRoverEntitlementCompartmentDetails
from .change_rover_node_compartment_details import ChangeRoverNodeCompartmentDetails
from .create_rover_cluster_details import CreateRoverClusterDetails
from .create_rover_entitlement_details import CreateRoverEntitlementDetails
from .create_rover_node_details import CreateRoverNodeDetails
from .current_rover_bundle_details import CurrentRoverBundleDetails
from .generate_certificate_response import GenerateCertificateResponse
from .leaf_certificate_details import LeafCertificateDetails
from .leaf_certificate_response import LeafCertificateResponse
from .renew_certificate_response import RenewCertificateResponse
from .replace_ca_details import ReplaceCaDetails
from .replace_certificate_authority_response import ReplaceCertificateAuthorityResponse
from .request_additional_nodes_details import RequestAdditionalNodesDetails
from .request_rover_bundle_details import RequestRoverBundleDetails
from .rover_bundle_request_collection import RoverBundleRequestCollection
from .rover_bundle_request_summary import RoverBundleRequestSummary
from .rover_bundle_status import RoverBundleStatus
from .rover_bundle_status_details import RoverBundleStatusDetails
from .rover_bundle_version import RoverBundleVersion
from .rover_cluster import RoverCluster
from .rover_cluster_certificate import RoverClusterCertificate
from .rover_cluster_collection import RoverClusterCollection
from .rover_cluster_summary import RoverClusterSummary
from .rover_entitlement import RoverEntitlement
from .rover_entitlement_collection import RoverEntitlementCollection
from .rover_entitlement_summary import RoverEntitlementSummary
from .rover_node import RoverNode
from .rover_node_action_set_key_details import RoverNodeActionSetKeyDetails
from .rover_node_certificate import RoverNodeCertificate
from .rover_node_collection import RoverNodeCollection
from .rover_node_encryption_key import RoverNodeEncryptionKey
from .rover_node_generate_certificate_details import RoverNodeGenerateCertificateDetails
from .rover_node_get_rpt import RoverNodeGetRpt
from .rover_node_renew_certificate_details import RoverNodeRenewCertificateDetails
from .rover_node_replace_certificate_authority_details import RoverNodeReplaceCertificateAuthorityDetails
from .rover_node_set_key import RoverNodeSetKey
from .rover_node_summary import RoverNodeSummary
from .rover_workload import RoverWorkload
from .shape_collection import ShapeCollection
from .shape_summary import ShapeSummary
from .shipping_address import ShippingAddress
from .update_rover_cluster_details import UpdateRoverClusterDetails
from .update_rover_entitlement_details import UpdateRoverEntitlementDetails
from .update_rover_node_details import UpdateRoverNodeDetails
from .work_request import WorkRequest
from .work_request_collection import WorkRequestCollection
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log import WorkRequestLog
from .work_request_log_collection import WorkRequestLogCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary

# Maps type names to classes for rover services.
rover_type_mapping = {
    "CaBundleResponse": CaBundleResponse,
    "CaDetails": CaDetails,
    "CertificateDetails": CertificateDetails,
    "ChangeRoverClusterCompartmentDetails": ChangeRoverClusterCompartmentDetails,
    "ChangeRoverEntitlementCompartmentDetails": ChangeRoverEntitlementCompartmentDetails,
    "ChangeRoverNodeCompartmentDetails": ChangeRoverNodeCompartmentDetails,
    "CreateRoverClusterDetails": CreateRoverClusterDetails,
    "CreateRoverEntitlementDetails": CreateRoverEntitlementDetails,
    "CreateRoverNodeDetails": CreateRoverNodeDetails,
    "CurrentRoverBundleDetails": CurrentRoverBundleDetails,
    "GenerateCertificateResponse": GenerateCertificateResponse,
    "LeafCertificateDetails": LeafCertificateDetails,
    "LeafCertificateResponse": LeafCertificateResponse,
    "RenewCertificateResponse": RenewCertificateResponse,
    "ReplaceCaDetails": ReplaceCaDetails,
    "ReplaceCertificateAuthorityResponse": ReplaceCertificateAuthorityResponse,
    "RequestAdditionalNodesDetails": RequestAdditionalNodesDetails,
    "RequestRoverBundleDetails": RequestRoverBundleDetails,
    "RoverBundleRequestCollection": RoverBundleRequestCollection,
    "RoverBundleRequestSummary": RoverBundleRequestSummary,
    "RoverBundleStatus": RoverBundleStatus,
    "RoverBundleStatusDetails": RoverBundleStatusDetails,
    "RoverBundleVersion": RoverBundleVersion,
    "RoverCluster": RoverCluster,
    "RoverClusterCertificate": RoverClusterCertificate,
    "RoverClusterCollection": RoverClusterCollection,
    "RoverClusterSummary": RoverClusterSummary,
    "RoverEntitlement": RoverEntitlement,
    "RoverEntitlementCollection": RoverEntitlementCollection,
    "RoverEntitlementSummary": RoverEntitlementSummary,
    "RoverNode": RoverNode,
    "RoverNodeActionSetKeyDetails": RoverNodeActionSetKeyDetails,
    "RoverNodeCertificate": RoverNodeCertificate,
    "RoverNodeCollection": RoverNodeCollection,
    "RoverNodeEncryptionKey": RoverNodeEncryptionKey,
    "RoverNodeGenerateCertificateDetails": RoverNodeGenerateCertificateDetails,
    "RoverNodeGetRpt": RoverNodeGetRpt,
    "RoverNodeRenewCertificateDetails": RoverNodeRenewCertificateDetails,
    "RoverNodeReplaceCertificateAuthorityDetails": RoverNodeReplaceCertificateAuthorityDetails,
    "RoverNodeSetKey": RoverNodeSetKey,
    "RoverNodeSummary": RoverNodeSummary,
    "RoverWorkload": RoverWorkload,
    "ShapeCollection": ShapeCollection,
    "ShapeSummary": ShapeSummary,
    "ShippingAddress": ShippingAddress,
    "UpdateRoverClusterDetails": UpdateRoverClusterDetails,
    "UpdateRoverEntitlementDetails": UpdateRoverEntitlementDetails,
    "UpdateRoverNodeDetails": UpdateRoverNodeDetails,
    "WorkRequest": WorkRequest,
    "WorkRequestCollection": WorkRequestCollection,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLog": WorkRequestLog,
    "WorkRequestLogCollection": WorkRequestLogCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary
}
