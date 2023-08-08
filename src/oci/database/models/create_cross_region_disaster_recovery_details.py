# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateCrossRegionDisasterRecoveryDetails(CreateAutonomousDatabaseBase):
    """
    The following are the details necessary to create a disaster recovery (DR) association for an existing Autonomous Database with a standby in a remote region.
    *IMPORTANT*
    For creating a standby databases in a cross-region DR association:
    - To create the standby database in a remote region, use the API endpoint in the region where the standby is located. For example, if the primary database is in the IAD region and the standby is in the PHX region, make the API call using the PHX endpoint (https://database.us-phoenix-1.oraclecloud.com). See API Endpoints for the list of Database Service API endpoints.
    - To create the request in the standby database, the sourceId value must be the OCID of the primary database.
    The following parameters are required for the cross-region standby database and must contain the same values as the source Autonomous Database:
    - remoteDisasterRecoveryType
    The following parameters are optional for the cross-region standby database. If included in the request, these parameters must contain the same values as the source Autonomous Database:
    - dbName
    - dbVersion
    - ecpuCount
    - dataStorageSizeInTB
    - customerContacts
    - scheduledOperations
    - isAutoScalingForStorageEnabled
    - definedTags
    - freeformTags
    - licenseModel
    - whitelistedIps
    - isMtlsConnectionRequired
    Example I - Creating a cross-region standby with required parameters only:
    `{
    \"compartmentId\": \"ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>\",
    \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>\",
    \"source\": \"CROSS_REGION_DISASTER_RECOVERY\",
    \"remoteDisasterRecoveryType\": \"BACKUP_BASED\"
    }`
    Example II - Creating a cross-region standby that specifies optional parameters in addition to the required parameters:
    `{
    \"compartmentId\": \"ocid.compartment.oc1..<var>&lt;unique_ID&gt;</var>\",
    \"ecpuCount\": 2,
    \"dbName\": \"adatabasedb1\",
    \"sourceId\": \"ocid1.autonomousdatabase.oc1.phx..<var>&lt;unique_ID&gt;</var>\",
    \"dataStorageSizeInTBs\": 1,
    \"source\": \"CROSS_REGION_DISASTER_RECOVERY\",
    \"adminPassword\" : \"<var>&lt;password&gt;</var>\",
    \"dbVersion\": \"19c\",
    \"licenseModel\": \"LICENSE_INCLUDED\",
    \"isAutoScalingForStorageEnabled\": \"true\",
    \"remoteDisasterRecoveryType\": \"BACKUP_BASED\"
    }`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateCrossRegionDisasterRecoveryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateCrossRegionDisasterRecoveryDetails.source` attribute
        of this class is ``CROSS_REGION_DISASTER_RECOVERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type compartment_id: str

        :param character_set:
            The value to assign to the character_set property of this CreateCrossRegionDisasterRecoveryDetails.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateCrossRegionDisasterRecoveryDetails.
        :type ncharacter_set: str

        :param db_name:
            The value to assign to the db_name property of this CreateCrossRegionDisasterRecoveryDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateCrossRegionDisasterRecoveryDetails.
        :type cpu_core_count: int

        :param backup_retention_period_in_days:
            The value to assign to the backup_retention_period_in_days property of this CreateCrossRegionDisasterRecoveryDetails.
        :type backup_retention_period_in_days: int

        :param compute_model:
            The value to assign to the compute_model property of this CreateCrossRegionDisasterRecoveryDetails.
            Allowed values for this property are: "ECPU", "OCPU"
        :type compute_model: str

        :param compute_count:
            The value to assign to the compute_count property of this CreateCrossRegionDisasterRecoveryDetails.
        :type compute_count: float

        :param ocpu_count:
            The value to assign to the ocpu_count property of this CreateCrossRegionDisasterRecoveryDetails.
        :type ocpu_count: float

        :param db_workload:
            The value to assign to the db_workload property of this CreateCrossRegionDisasterRecoveryDetails.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateCrossRegionDisasterRecoveryDetails.
        :type data_storage_size_in_tbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CreateCrossRegionDisasterRecoveryDetails.
        :type data_storage_size_in_gbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_free_tier: bool

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type vault_id: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateCrossRegionDisasterRecoveryDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateCrossRegionDisasterRecoveryDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateCrossRegionDisasterRecoveryDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type autonomous_container_database_id: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateCrossRegionDisasterRecoveryDetails.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this CreateCrossRegionDisasterRecoveryDetails.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this CreateCrossRegionDisasterRecoveryDetails.
        :type standby_whitelisted_ips: list[str]

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_data_guard_enabled: bool

        :param is_local_data_guard_enabled:
            The value to assign to the is_local_data_guard_enabled property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_local_data_guard_enabled: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateCrossRegionDisasterRecoveryDetails.
        :type nsg_ids: list[str]

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this CreateCrossRegionDisasterRecoveryDetails.
        :type private_endpoint_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateCrossRegionDisasterRecoveryDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateCrossRegionDisasterRecoveryDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this CreateCrossRegionDisasterRecoveryDetails.
        :type private_endpoint_ip: str

        :param db_version:
            The value to assign to the db_version property of this CreateCrossRegionDisasterRecoveryDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateCrossRegionDisasterRecoveryDetails.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE", "CROSS_REGION_DATAGUARD", "CROSS_REGION_DISASTER_RECOVERY"
        :type source: str

        :param customer_contacts:
            The value to assign to the customer_contacts property of this CreateCrossRegionDisasterRecoveryDetails.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        :param is_mtls_connection_required:
            The value to assign to the is_mtls_connection_required property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_mtls_connection_required: bool

        :param autonomous_maintenance_schedule_type:
            The value to assign to the autonomous_maintenance_schedule_type property of this CreateCrossRegionDisasterRecoveryDetails.
            Allowed values for this property are: "EARLY", "REGULAR"
        :type autonomous_maintenance_schedule_type: str

        :param scheduled_operations:
            The value to assign to the scheduled_operations property of this CreateCrossRegionDisasterRecoveryDetails.
        :type scheduled_operations: list[oci.database.models.ScheduledOperationDetails]

        :param is_auto_scaling_for_storage_enabled:
            The value to assign to the is_auto_scaling_for_storage_enabled property of this CreateCrossRegionDisasterRecoveryDetails.
        :type is_auto_scaling_for_storage_enabled: bool

        :param max_cpu_core_count:
            The value to assign to the max_cpu_core_count property of this CreateCrossRegionDisasterRecoveryDetails.
        :type max_cpu_core_count: int

        :param database_edition:
            The value to assign to the database_edition property of this CreateCrossRegionDisasterRecoveryDetails.
        :type database_edition: str

        :param db_tools_details:
            The value to assign to the db_tools_details property of this CreateCrossRegionDisasterRecoveryDetails.
        :type db_tools_details: list[oci.database.models.DatabaseTool]

        :param secret_id:
            The value to assign to the secret_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type secret_id: str

        :param secret_version_number:
            The value to assign to the secret_version_number property of this CreateCrossRegionDisasterRecoveryDetails.
        :type secret_version_number: int

        :param source_id:
            The value to assign to the source_id property of this CreateCrossRegionDisasterRecoveryDetails.
        :type source_id: str

        :param remote_disaster_recovery_type:
            The value to assign to the remote_disaster_recovery_type property of this CreateCrossRegionDisasterRecoveryDetails.
        :type remote_disaster_recovery_type: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'backup_retention_period_in_days': 'int',
            'compute_model': 'str',
            'compute_count': 'float',
            'ocpu_count': 'float',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'is_free_tier': 'bool',
            'kms_key_id': 'str',
            'vault_id': 'str',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'is_preview_version_with_service_terms_accepted': 'bool',
            'is_auto_scaling_enabled': 'bool',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'is_access_control_enabled': 'bool',
            'whitelisted_ips': 'list[str]',
            'are_primary_whitelisted_ips_used': 'bool',
            'standby_whitelisted_ips': 'list[str]',
            'is_data_guard_enabled': 'bool',
            'is_local_data_guard_enabled': 'bool',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'private_endpoint_ip': 'str',
            'db_version': 'str',
            'source': 'str',
            'customer_contacts': 'list[CustomerContact]',
            'is_mtls_connection_required': 'bool',
            'autonomous_maintenance_schedule_type': 'str',
            'scheduled_operations': 'list[ScheduledOperationDetails]',
            'is_auto_scaling_for_storage_enabled': 'bool',
            'max_cpu_core_count': 'int',
            'database_edition': 'str',
            'db_tools_details': 'list[DatabaseTool]',
            'secret_id': 'str',
            'secret_version_number': 'int',
            'source_id': 'str',
            'remote_disaster_recovery_type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'backup_retention_period_in_days': 'backupRetentionPeriodInDays',
            'compute_model': 'computeModel',
            'compute_count': 'computeCount',
            'ocpu_count': 'ocpuCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'is_free_tier': 'isFreeTier',
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'is_preview_version_with_service_terms_accepted': 'isPreviewVersionWithServiceTermsAccepted',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'is_access_control_enabled': 'isAccessControlEnabled',
            'whitelisted_ips': 'whitelistedIps',
            'are_primary_whitelisted_ips_used': 'arePrimaryWhitelistedIpsUsed',
            'standby_whitelisted_ips': 'standbyWhitelistedIps',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'is_local_data_guard_enabled': 'isLocalDataGuardEnabled',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint_label': 'privateEndpointLabel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'private_endpoint_ip': 'privateEndpointIp',
            'db_version': 'dbVersion',
            'source': 'source',
            'customer_contacts': 'customerContacts',
            'is_mtls_connection_required': 'isMtlsConnectionRequired',
            'autonomous_maintenance_schedule_type': 'autonomousMaintenanceScheduleType',
            'scheduled_operations': 'scheduledOperations',
            'is_auto_scaling_for_storage_enabled': 'isAutoScalingForStorageEnabled',
            'max_cpu_core_count': 'maxCpuCoreCount',
            'database_edition': 'databaseEdition',
            'db_tools_details': 'dbToolsDetails',
            'secret_id': 'secretId',
            'secret_version_number': 'secretVersionNumber',
            'source_id': 'sourceId',
            'remote_disaster_recovery_type': 'remoteDisasterRecoveryType'
        }

        self._compartment_id = None
        self._character_set = None
        self._ncharacter_set = None
        self._db_name = None
        self._cpu_core_count = None
        self._backup_retention_period_in_days = None
        self._compute_model = None
        self._compute_count = None
        self._ocpu_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._is_free_tier = None
        self._kms_key_id = None
        self._vault_id = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._is_preview_version_with_service_terms_accepted = None
        self._is_auto_scaling_enabled = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._is_access_control_enabled = None
        self._whitelisted_ips = None
        self._are_primary_whitelisted_ips_used = None
        self._standby_whitelisted_ips = None
        self._is_data_guard_enabled = None
        self._is_local_data_guard_enabled = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint_label = None
        self._freeform_tags = None
        self._defined_tags = None
        self._private_endpoint_ip = None
        self._db_version = None
        self._source = None
        self._customer_contacts = None
        self._is_mtls_connection_required = None
        self._autonomous_maintenance_schedule_type = None
        self._scheduled_operations = None
        self._is_auto_scaling_for_storage_enabled = None
        self._max_cpu_core_count = None
        self._database_edition = None
        self._db_tools_details = None
        self._secret_id = None
        self._secret_version_number = None
        self._source_id = None
        self._remote_disaster_recovery_type = None
        self._source = 'CROSS_REGION_DISASTER_RECOVERY'

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this CreateCrossRegionDisasterRecoveryDetails.
        The `OCID`__ of the source Autonomous Database that will be used to create a new standby database for the DR association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_id of this CreateCrossRegionDisasterRecoveryDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateCrossRegionDisasterRecoveryDetails.
        The `OCID`__ of the source Autonomous Database that will be used to create a new standby database for the DR association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this CreateCrossRegionDisasterRecoveryDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def remote_disaster_recovery_type(self):
        """
        **[Required]** Gets the remote_disaster_recovery_type of this CreateCrossRegionDisasterRecoveryDetails.
        Indicates the cross-region disaster recovery (DR) type of the standby Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.


        :return: The remote_disaster_recovery_type of this CreateCrossRegionDisasterRecoveryDetails.
        :rtype: str
        """
        return self._remote_disaster_recovery_type

    @remote_disaster_recovery_type.setter
    def remote_disaster_recovery_type(self, remote_disaster_recovery_type):
        """
        Sets the remote_disaster_recovery_type of this CreateCrossRegionDisasterRecoveryDetails.
        Indicates the cross-region disaster recovery (DR) type of the standby Shared Autonomous Database.
        Autonomous Data Guard (ADG) DR type provides business critical DR with a faster recovery time objective (RTO) during failover or switchover.
        Backup-based DR type provides lower cost DR with a slower RTO during failover or switchover.


        :param remote_disaster_recovery_type: The remote_disaster_recovery_type of this CreateCrossRegionDisasterRecoveryDetails.
        :type: str
        """
        self._remote_disaster_recovery_type = remote_disaster_recovery_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
