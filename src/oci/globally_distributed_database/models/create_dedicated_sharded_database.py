# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230301

from .create_sharded_database_details import CreateShardedDatabaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDedicatedShardedDatabase(CreateShardedDatabaseDetails):
    """
    Request details for creation of ATP-Dedicated based sharded database.
    """

    #: A constant which can be used with the db_workload property of a CreateDedicatedShardedDatabase.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a CreateDedicatedShardedDatabase.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the sharding_method property of a CreateDedicatedShardedDatabase.
    #: This constant has a value of "USER"
    SHARDING_METHOD_USER = "USER"

    #: A constant which can be used with the sharding_method property of a CreateDedicatedShardedDatabase.
    #: This constant has a value of "SYSTEM"
    SHARDING_METHOD_SYSTEM = "SYSTEM"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDedicatedShardedDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.globally_distributed_database.models.CreateDedicatedShardedDatabase.db_deployment_type` attribute
        of this class is ``DEDICATED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDedicatedShardedDatabase.
        :type compartment_id: str

        :param db_deployment_type:
            The value to assign to the db_deployment_type property of this CreateDedicatedShardedDatabase.
            Allowed values for this property are: "DEDICATED"
        :type db_deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateDedicatedShardedDatabase.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDedicatedShardedDatabase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDedicatedShardedDatabase.
        :type defined_tags: dict(str, dict(str, object))

        :param replication_method:
            The value to assign to the replication_method property of this CreateDedicatedShardedDatabase.
        :type replication_method: str

        :param replication_factor:
            The value to assign to the replication_factor property of this CreateDedicatedShardedDatabase.
        :type replication_factor: int

        :param replication_unit:
            The value to assign to the replication_unit property of this CreateDedicatedShardedDatabase.
        :type replication_unit: int

        :param cluster_certificate_common_name:
            The value to assign to the cluster_certificate_common_name property of this CreateDedicatedShardedDatabase.
        :type cluster_certificate_common_name: str

        :param chunks:
            The value to assign to the chunks property of this CreateDedicatedShardedDatabase.
        :type chunks: int

        :param db_workload:
            The value to assign to the db_workload property of this CreateDedicatedShardedDatabase.
            Allowed values for this property are: "OLTP", "DW"
        :type db_workload: str

        :param sharding_method:
            The value to assign to the sharding_method property of this CreateDedicatedShardedDatabase.
            Allowed values for this property are: "USER", "SYSTEM"
        :type sharding_method: str

        :param db_version:
            The value to assign to the db_version property of this CreateDedicatedShardedDatabase.
        :type db_version: str

        :param character_set:
            The value to assign to the character_set property of this CreateDedicatedShardedDatabase.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateDedicatedShardedDatabase.
        :type ncharacter_set: str

        :param listener_port:
            The value to assign to the listener_port property of this CreateDedicatedShardedDatabase.
        :type listener_port: int

        :param listener_port_tls:
            The value to assign to the listener_port_tls property of this CreateDedicatedShardedDatabase.
        :type listener_port_tls: int

        :param ons_port_local:
            The value to assign to the ons_port_local property of this CreateDedicatedShardedDatabase.
        :type ons_port_local: int

        :param ons_port_remote:
            The value to assign to the ons_port_remote property of this CreateDedicatedShardedDatabase.
        :type ons_port_remote: int

        :param prefix:
            The value to assign to the prefix property of this CreateDedicatedShardedDatabase.
        :type prefix: str

        :param shard_details:
            The value to assign to the shard_details property of this CreateDedicatedShardedDatabase.
        :type shard_details: list[oci.globally_distributed_database.models.CreateDedicatedShardDetail]

        :param catalog_details:
            The value to assign to the catalog_details property of this CreateDedicatedShardedDatabase.
        :type catalog_details: list[oci.globally_distributed_database.models.CreateDedicatedCatalogDetail]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'replication_method': 'str',
            'replication_factor': 'int',
            'replication_unit': 'int',
            'cluster_certificate_common_name': 'str',
            'chunks': 'int',
            'db_workload': 'str',
            'sharding_method': 'str',
            'db_version': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'listener_port': 'int',
            'listener_port_tls': 'int',
            'ons_port_local': 'int',
            'ons_port_remote': 'int',
            'prefix': 'str',
            'shard_details': 'list[CreateDedicatedShardDetail]',
            'catalog_details': 'list[CreateDedicatedCatalogDetail]'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_deployment_type': 'dbDeploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'replication_method': 'replicationMethod',
            'replication_factor': 'replicationFactor',
            'replication_unit': 'replicationUnit',
            'cluster_certificate_common_name': 'clusterCertificateCommonName',
            'chunks': 'chunks',
            'db_workload': 'dbWorkload',
            'sharding_method': 'shardingMethod',
            'db_version': 'dbVersion',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'listener_port': 'listenerPort',
            'listener_port_tls': 'listenerPortTls',
            'ons_port_local': 'onsPortLocal',
            'ons_port_remote': 'onsPortRemote',
            'prefix': 'prefix',
            'shard_details': 'shardDetails',
            'catalog_details': 'catalogDetails'
        }
        self._compartment_id = None
        self._db_deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._replication_method = None
        self._replication_factor = None
        self._replication_unit = None
        self._cluster_certificate_common_name = None
        self._chunks = None
        self._db_workload = None
        self._sharding_method = None
        self._db_version = None
        self._character_set = None
        self._ncharacter_set = None
        self._listener_port = None
        self._listener_port_tls = None
        self._ons_port_local = None
        self._ons_port_remote = None
        self._prefix = None
        self._shard_details = None
        self._catalog_details = None
        self._db_deployment_type = 'DEDICATED'

    @property
    def replication_method(self):
        """
        Gets the replication_method of this CreateDedicatedShardedDatabase.
        The Replication method for sharded database.


        :return: The replication_method of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._replication_method

    @replication_method.setter
    def replication_method(self, replication_method):
        """
        Sets the replication_method of this CreateDedicatedShardedDatabase.
        The Replication method for sharded database.


        :param replication_method: The replication_method of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._replication_method = replication_method

    @property
    def replication_factor(self):
        """
        Gets the replication_factor of this CreateDedicatedShardedDatabase.
        The Replication factor for RAFT replication based sharded database. Currently supported values are 3, 5 and 7.


        :return: The replication_factor of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        """
        Sets the replication_factor of this CreateDedicatedShardedDatabase.
        The Replication factor for RAFT replication based sharded database. Currently supported values are 3, 5 and 7.


        :param replication_factor: The replication_factor of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._replication_factor = replication_factor

    @property
    def replication_unit(self):
        """
        Gets the replication_unit of this CreateDedicatedShardedDatabase.
        For RAFT replication based sharded database, the value should be atleast twice the number of shards.


        :return: The replication_unit of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._replication_unit

    @replication_unit.setter
    def replication_unit(self, replication_unit):
        """
        Sets the replication_unit of this CreateDedicatedShardedDatabase.
        For RAFT replication based sharded database, the value should be atleast twice the number of shards.


        :param replication_unit: The replication_unit of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._replication_unit = replication_unit

    @property
    def cluster_certificate_common_name(self):
        """
        Gets the cluster_certificate_common_name of this CreateDedicatedShardedDatabase.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :return: The cluster_certificate_common_name of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._cluster_certificate_common_name

    @cluster_certificate_common_name.setter
    def cluster_certificate_common_name(self, cluster_certificate_common_name):
        """
        Sets the cluster_certificate_common_name of this CreateDedicatedShardedDatabase.
        The certificate common name used in all cloudAutonomousVmClusters for the sharded database topology. Eg. Production.
        All the clusters used in one sharded database topology shall have same CABundle setup. Valid characterset for
        clusterCertificateCommonName include uppercase or lowercase letters, numbers, hyphens, underscores, and period.


        :param cluster_certificate_common_name: The cluster_certificate_common_name of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._cluster_certificate_common_name = cluster_certificate_common_name

    @property
    def chunks(self):
        """
        Gets the chunks of this CreateDedicatedShardedDatabase.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :return: The chunks of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._chunks

    @chunks.setter
    def chunks(self, chunks):
        """
        Sets the chunks of this CreateDedicatedShardedDatabase.
        The default number of unique chunks in a shardspace. The value of chunks must be
        greater than 2 times the size of the largest shardgroup in any shardspace.


        :param chunks: The chunks of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._chunks = chunks

    @property
    def db_workload(self):
        """
        **[Required]** Gets the db_workload of this CreateDedicatedShardedDatabase.
        Possible workload types.

        Allowed values for this property are: "OLTP", "DW"


        :return: The db_workload of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this CreateDedicatedShardedDatabase.
        Possible workload types.


        :param db_workload: The db_workload of this CreateDedicatedShardedDatabase.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            raise ValueError(
                f"Invalid value for `db_workload`, must be None or one of {allowed_values}"
            )
        self._db_workload = db_workload

    @property
    def sharding_method(self):
        """
        **[Required]** Gets the sharding_method of this CreateDedicatedShardedDatabase.
        Sharding Method.

        Allowed values for this property are: "USER", "SYSTEM"


        :return: The sharding_method of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._sharding_method

    @sharding_method.setter
    def sharding_method(self, sharding_method):
        """
        Sets the sharding_method of this CreateDedicatedShardedDatabase.
        Sharding Method.


        :param sharding_method: The sharding_method of this CreateDedicatedShardedDatabase.
        :type: str
        """
        allowed_values = ["USER", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(sharding_method, allowed_values):
            raise ValueError(
                f"Invalid value for `sharding_method`, must be None or one of {allowed_values}"
            )
        self._sharding_method = sharding_method

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this CreateDedicatedShardedDatabase.
        Oracle Database version of the Autonomous Container Database.


        :return: The db_version of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateDedicatedShardedDatabase.
        Oracle Database version of the Autonomous Container Database.


        :param db_version: The db_version of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._db_version = db_version

    @property
    def character_set(self):
        """
        **[Required]** Gets the character_set of this CreateDedicatedShardedDatabase.
        The character set for the new shard database being created. Use database api ListAutonomousDatabaseCharacterSets to
        get the list of allowed character set for autonomous dedicated database. See documentation:
        https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/ListAutonomousDatabaseCharacterSets


        :return: The character_set of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this CreateDedicatedShardedDatabase.
        The character set for the new shard database being created. Use database api ListAutonomousDatabaseCharacterSets to
        get the list of allowed character set for autonomous dedicated database. See documentation:
        https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/ListAutonomousDatabaseCharacterSets


        :param character_set: The character_set of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        **[Required]** Gets the ncharacter_set of this CreateDedicatedShardedDatabase.
        The national character set for the new shard database being created. Use database api ListAutonomousDatabaseCharacterSets to
        get the list of allowed national character set for autonomous dedicated database. See documentation:
        https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/ListAutonomousDatabaseCharacterSets


        :return: The ncharacter_set of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this CreateDedicatedShardedDatabase.
        The national character set for the new shard database being created. Use database api ListAutonomousDatabaseCharacterSets to
        get the list of allowed national character set for autonomous dedicated database. See documentation:
        https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/ListAutonomousDatabaseCharacterSets


        :param ncharacter_set: The ncharacter_set of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def listener_port(self):
        """
        **[Required]** Gets the listener_port of this CreateDedicatedShardedDatabase.
        The listener port number for sharded database.


        :return: The listener_port of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._listener_port

    @listener_port.setter
    def listener_port(self, listener_port):
        """
        Sets the listener_port of this CreateDedicatedShardedDatabase.
        The listener port number for sharded database.


        :param listener_port: The listener_port of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._listener_port = listener_port

    @property
    def listener_port_tls(self):
        """
        **[Required]** Gets the listener_port_tls of this CreateDedicatedShardedDatabase.
        The TLS listener port number for sharded database.


        :return: The listener_port_tls of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._listener_port_tls

    @listener_port_tls.setter
    def listener_port_tls(self, listener_port_tls):
        """
        Sets the listener_port_tls of this CreateDedicatedShardedDatabase.
        The TLS listener port number for sharded database.


        :param listener_port_tls: The listener_port_tls of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._listener_port_tls = listener_port_tls

    @property
    def ons_port_local(self):
        """
        **[Required]** Gets the ons_port_local of this CreateDedicatedShardedDatabase.
        Ons port local for sharded database.


        :return: The ons_port_local of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._ons_port_local

    @ons_port_local.setter
    def ons_port_local(self, ons_port_local):
        """
        Sets the ons_port_local of this CreateDedicatedShardedDatabase.
        Ons port local for sharded database.


        :param ons_port_local: The ons_port_local of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._ons_port_local = ons_port_local

    @property
    def ons_port_remote(self):
        """
        **[Required]** Gets the ons_port_remote of this CreateDedicatedShardedDatabase.
        Ons remote port for sharded database.


        :return: The ons_port_remote of this CreateDedicatedShardedDatabase.
        :rtype: int
        """
        return self._ons_port_remote

    @ons_port_remote.setter
    def ons_port_remote(self, ons_port_remote):
        """
        Sets the ons_port_remote of this CreateDedicatedShardedDatabase.
        Ons remote port for sharded database.


        :param ons_port_remote: The ons_port_remote of this CreateDedicatedShardedDatabase.
        :type: int
        """
        self._ons_port_remote = ons_port_remote

    @property
    def prefix(self):
        """
        **[Required]** Gets the prefix of this CreateDedicatedShardedDatabase.
        Unique name prefix for the sharded databases. Only alpha-numeric values are allowed. First character
        has to be a letter followed by any combination of letter and number.


        :return: The prefix of this CreateDedicatedShardedDatabase.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CreateDedicatedShardedDatabase.
        Unique name prefix for the sharded databases. Only alpha-numeric values are allowed. First character
        has to be a letter followed by any combination of letter and number.


        :param prefix: The prefix of this CreateDedicatedShardedDatabase.
        :type: str
        """
        self._prefix = prefix

    @property
    def shard_details(self):
        """
        **[Required]** Gets the shard_details of this CreateDedicatedShardedDatabase.
        Collection of ATP-Dedicated shards that needs to be created.


        :return: The shard_details of this CreateDedicatedShardedDatabase.
        :rtype: list[oci.globally_distributed_database.models.CreateDedicatedShardDetail]
        """
        return self._shard_details

    @shard_details.setter
    def shard_details(self, shard_details):
        """
        Sets the shard_details of this CreateDedicatedShardedDatabase.
        Collection of ATP-Dedicated shards that needs to be created.


        :param shard_details: The shard_details of this CreateDedicatedShardedDatabase.
        :type: list[oci.globally_distributed_database.models.CreateDedicatedShardDetail]
        """
        self._shard_details = shard_details

    @property
    def catalog_details(self):
        """
        **[Required]** Gets the catalog_details of this CreateDedicatedShardedDatabase.
        Collection of ATP-Dedicated catalogs that needs to be created.


        :return: The catalog_details of this CreateDedicatedShardedDatabase.
        :rtype: list[oci.globally_distributed_database.models.CreateDedicatedCatalogDetail]
        """
        return self._catalog_details

    @catalog_details.setter
    def catalog_details(self, catalog_details):
        """
        Sets the catalog_details of this CreateDedicatedShardedDatabase.
        Collection of ATP-Dedicated catalogs that needs to be created.


        :param catalog_details: The catalog_details of this CreateDedicatedShardedDatabase.
        :type: list[oci.globally_distributed_database.models.CreateDedicatedCatalogDetail]
        """
        self._catalog_details = catalog_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
