# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MicrosoftFabricConnection(Connection):
    """
    Represents the metadata of a Microsoft Fabric Connection.
    """

    #: A constant which can be used with the technology_type property of a MicrosoftFabricConnection.
    #: This constant has a value of "MICROSOFT_FABRIC_LAKEHOUSE"
    TECHNOLOGY_TYPE_MICROSOFT_FABRIC_LAKEHOUSE = "MICROSOFT_FABRIC_LAKEHOUSE"

    #: A constant which can be used with the technology_type property of a MicrosoftFabricConnection.
    #: This constant has a value of "MICROSOFT_FABRIC_MIRROR"
    TECHNOLOGY_TYPE_MICROSOFT_FABRIC_MIRROR = "MICROSOFT_FABRIC_MIRROR"

    def __init__(self, **kwargs):
        """
        Initializes a new MicrosoftFabricConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.MicrosoftFabricConnection.connection_type` attribute
        of this class is ``MICROSOFT_FABRIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this MicrosoftFabricConnection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this MicrosoftFabricConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MicrosoftFabricConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MicrosoftFabricConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MicrosoftFabricConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MicrosoftFabricConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MicrosoftFabricConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MicrosoftFabricConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MicrosoftFabricConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MicrosoftFabricConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MicrosoftFabricConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MicrosoftFabricConnection.
        :type time_updated: datetime

        :param locks:
            The value to assign to the locks property of this MicrosoftFabricConnection.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param vault_id:
            The value to assign to the vault_id property of this MicrosoftFabricConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this MicrosoftFabricConnection.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this MicrosoftFabricConnection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this MicrosoftFabricConnection.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this MicrosoftFabricConnection.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this MicrosoftFabricConnection.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this MicrosoftFabricConnection.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this MicrosoftFabricConnection.
            Allowed values for this property are: "MICROSOFT_FABRIC_LAKEHOUSE", "MICROSOFT_FABRIC_MIRROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MicrosoftFabricConnection.
        :type tenant_id: str

        :param client_id:
            The value to assign to the client_id property of this MicrosoftFabricConnection.
        :type client_id: str

        :param client_secret_secret_id:
            The value to assign to the client_secret_secret_id property of this MicrosoftFabricConnection.
        :type client_secret_secret_id: str

        :param endpoint:
            The value to assign to the endpoint property of this MicrosoftFabricConnection.
        :type endpoint: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'locks': 'list[ResourceLock]',
            'vault_id': 'str',
            'key_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'tenant_id': 'str',
            'client_id': 'str',
            'client_secret_secret_id': 'str',
            'endpoint': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'locks': 'locks',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'tenant_id': 'tenantId',
            'client_id': 'clientId',
            'client_secret_secret_id': 'clientSecretSecretId',
            'endpoint': 'endpoint'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._locks = None
        self._vault_id = None
        self._key_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._tenant_id = None
        self._client_id = None
        self._client_secret_secret_id = None
        self._endpoint = None
        self._connection_type = 'MICROSOFT_FABRIC'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this MicrosoftFabricConnection.
        The Microsoft Fabric technology type.

        Allowed values for this property are: "MICROSOFT_FABRIC_LAKEHOUSE", "MICROSOFT_FABRIC_MIRROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this MicrosoftFabricConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this MicrosoftFabricConnection.
        The Microsoft Fabric technology type.


        :param technology_type: The technology_type of this MicrosoftFabricConnection.
        :type: str
        """
        allowed_values = ["MICROSOFT_FABRIC_LAKEHOUSE", "MICROSOFT_FABRIC_MIRROR"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MicrosoftFabricConnection.
        Azure tenant ID of the application.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :return: The tenant_id of this MicrosoftFabricConnection.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MicrosoftFabricConnection.
        Azure tenant ID of the application.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :param tenant_id: The tenant_id of this MicrosoftFabricConnection.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this MicrosoftFabricConnection.
        Azure client ID of the application.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :return: The client_id of this MicrosoftFabricConnection.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this MicrosoftFabricConnection.
        Azure client ID of the application.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :param client_id: The client_id of this MicrosoftFabricConnection.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret_secret_id(self):
        """
        Gets the client_secret_secret_id of this MicrosoftFabricConnection.
        The `OCID`__ of the Secret where the client secret is stored.
        Note: When provided, 'clientSecret' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The client_secret_secret_id of this MicrosoftFabricConnection.
        :rtype: str
        """
        return self._client_secret_secret_id

    @client_secret_secret_id.setter
    def client_secret_secret_id(self, client_secret_secret_id):
        """
        Sets the client_secret_secret_id of this MicrosoftFabricConnection.
        The `OCID`__ of the Secret where the client secret is stored.
        Note: When provided, 'clientSecret' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param client_secret_secret_id: The client_secret_secret_id of this MicrosoftFabricConnection.
        :type: str
        """
        self._client_secret_secret_id = client_secret_secret_id

    @property
    def endpoint(self):
        """
        Gets the endpoint of this MicrosoftFabricConnection.
        Optional Microsoft Fabric service endpoint.
        Default value: https://onelake.dfs.fabric.microsoft.com


        :return: The endpoint of this MicrosoftFabricConnection.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this MicrosoftFabricConnection.
        Optional Microsoft Fabric service endpoint.
        Default value: https://onelake.dfs.fabric.microsoft.com


        :param endpoint: The endpoint of this MicrosoftFabricConnection.
        :type: str
        """
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
