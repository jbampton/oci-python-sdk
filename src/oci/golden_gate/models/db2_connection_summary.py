# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Db2ConnectionSummary(ConnectionSummary):
    """
    Summary of the DB2 Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Db2ConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.Db2ConnectionSummary.connection_type` attribute
        of this class is ``DB2`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this Db2ConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this Db2ConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Db2ConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Db2ConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Db2ConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Db2ConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Db2ConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Db2ConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Db2ConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Db2ConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this Db2ConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Db2ConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this Db2ConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this Db2ConnectionSummary.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this Db2ConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Db2ConnectionSummary.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this Db2ConnectionSummary.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this Db2ConnectionSummary.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param locks:
            The value to assign to the locks property of this Db2ConnectionSummary.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this Db2ConnectionSummary.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this Db2ConnectionSummary.
        :type technology_type: str

        :param database_name:
            The value to assign to the database_name property of this Db2ConnectionSummary.
        :type database_name: str

        :param host:
            The value to assign to the host property of this Db2ConnectionSummary.
        :type host: str

        :param port:
            The value to assign to the port property of this Db2ConnectionSummary.
        :type port: int

        :param username:
            The value to assign to the username property of this Db2ConnectionSummary.
        :type username: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this Db2ConnectionSummary.
        :type additional_attributes: list[oci.golden_gate.models.NameValuePair]

        :param security_protocol:
            The value to assign to the security_protocol property of this Db2ConnectionSummary.
        :type security_protocol: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this Db2ConnectionSummary.
        :type password_secret_id: str

        :param ssl_client_keystoredb_secret_id:
            The value to assign to the ssl_client_keystoredb_secret_id property of this Db2ConnectionSummary.
        :type ssl_client_keystoredb_secret_id: str

        :param ssl_client_keystash_secret_id:
            The value to assign to the ssl_client_keystash_secret_id property of this Db2ConnectionSummary.
        :type ssl_client_keystash_secret_id: str

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
            'vault_id': 'str',
            'key_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'locks': 'list[ResourceLock]',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'database_name': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'security_protocol': 'str',
            'password_secret_id': 'str',
            'ssl_client_keystoredb_secret_id': 'str',
            'ssl_client_keystash_secret_id': 'str'
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
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'locks': 'locks',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'database_name': 'databaseName',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'additional_attributes': 'additionalAttributes',
            'security_protocol': 'securityProtocol',
            'password_secret_id': 'passwordSecretId',
            'ssl_client_keystoredb_secret_id': 'sslClientKeystoredbSecretId',
            'ssl_client_keystash_secret_id': 'sslClientKeystashSecretId'
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
        self._vault_id = None
        self._key_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._locks = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._database_name = None
        self._host = None
        self._port = None
        self._username = None
        self._additional_attributes = None
        self._security_protocol = None
        self._password_secret_id = None
        self._ssl_client_keystoredb_secret_id = None
        self._ssl_client_keystash_secret_id = None
        self._connection_type = 'DB2'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this Db2ConnectionSummary.
        The DB2 technology type.


        :return: The technology_type of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this Db2ConnectionSummary.
        The DB2 technology type.


        :param technology_type: The technology_type of this Db2ConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this Db2ConnectionSummary.
        The name of the database.


        :return: The database_name of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this Db2ConnectionSummary.
        The name of the database.


        :param database_name: The database_name of this Db2ConnectionSummary.
        :type: str
        """
        self._database_name = database_name

    @property
    def host(self):
        """
        **[Required]** Gets the host of this Db2ConnectionSummary.
        The name or address of a host.


        :return: The host of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this Db2ConnectionSummary.
        The name or address of a host.


        :param host: The host of this Db2ConnectionSummary.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Db2ConnectionSummary.
        The port of an endpoint usually specified for a connection.


        :return: The port of this Db2ConnectionSummary.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Db2ConnectionSummary.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this Db2ConnectionSummary.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        **[Required]** Gets the username of this Db2ConnectionSummary.
        The username Oracle GoldenGate uses to connect to the DB2 database.
        This username must already exist and be available by the DB2 to be connected to.


        :return: The username of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Db2ConnectionSummary.
        The username Oracle GoldenGate uses to connect to the DB2 database.
        This username must already exist and be available by the DB2 to be connected to.


        :param username: The username of this Db2ConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this Db2ConnectionSummary.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :return: The additional_attributes of this Db2ConnectionSummary.
        :rtype: list[oci.golden_gate.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this Db2ConnectionSummary.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :param additional_attributes: The additional_attributes of this Db2ConnectionSummary.
        :type: list[oci.golden_gate.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def security_protocol(self):
        """
        **[Required]** Gets the security_protocol of this Db2ConnectionSummary.
        Security protocol for the DB2 database.


        :return: The security_protocol of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this Db2ConnectionSummary.
        Security protocol for the DB2 database.


        :param security_protocol: The security_protocol of this Db2ConnectionSummary.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the password is stored,
        that Oracle GoldenGate uses to connect the associated DB2 database.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the password is stored,
        that Oracle GoldenGate uses to connect the associated DB2 database.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this Db2ConnectionSummary.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def ssl_client_keystoredb_secret_id(self):
        """
        Gets the ssl_client_keystoredb_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the keystore file stored,
        which created at the client containing the server certificate / CA root certificate.
        Note: When provided, 'sslClientKeystoredb' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ssl_client_keystoredb_secret_id of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._ssl_client_keystoredb_secret_id

    @ssl_client_keystoredb_secret_id.setter
    def ssl_client_keystoredb_secret_id(self, ssl_client_keystoredb_secret_id):
        """
        Sets the ssl_client_keystoredb_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the keystore file stored,
        which created at the client containing the server certificate / CA root certificate.
        Note: When provided, 'sslClientKeystoredb' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ssl_client_keystoredb_secret_id: The ssl_client_keystoredb_secret_id of this Db2ConnectionSummary.
        :type: str
        """
        self._ssl_client_keystoredb_secret_id = ssl_client_keystoredb_secret_id

    @property
    def ssl_client_keystash_secret_id(self):
        """
        Gets the ssl_client_keystash_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the keystash file is stored,
        which contains the encrypted password to the key database file.
        Note: When provided, 'sslClientKeystash' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ssl_client_keystash_secret_id of this Db2ConnectionSummary.
        :rtype: str
        """
        return self._ssl_client_keystash_secret_id

    @ssl_client_keystash_secret_id.setter
    def ssl_client_keystash_secret_id(self, ssl_client_keystash_secret_id):
        """
        Sets the ssl_client_keystash_secret_id of this Db2ConnectionSummary.
        The `OCID`__ of the Secret where the keystash file is stored,
        which contains the encrypted password to the key database file.
        Note: When provided, 'sslClientKeystash' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ssl_client_keystash_secret_id: The ssl_client_keystash_secret_id of this Db2ConnectionSummary.
        :type: str
        """
        self._ssl_client_keystash_secret_id = ssl_client_keystash_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
