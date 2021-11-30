# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Tablespace(object):
    """
    The details of a tablespace.
    """

    #: A constant which can be used with the type property of a Tablespace.
    #: This constant has a value of "UNDO"
    TYPE_UNDO = "UNDO"

    #: A constant which can be used with the type property of a Tablespace.
    #: This constant has a value of "LOST_WRITE_PROTECTION"
    TYPE_LOST_WRITE_PROTECTION = "LOST_WRITE_PROTECTION"

    #: A constant which can be used with the type property of a Tablespace.
    #: This constant has a value of "PERMANENT"
    TYPE_PERMANENT = "PERMANENT"

    #: A constant which can be used with the type property of a Tablespace.
    #: This constant has a value of "TEMPORARY"
    TYPE_TEMPORARY = "TEMPORARY"

    #: A constant which can be used with the status property of a Tablespace.
    #: This constant has a value of "ONLINE"
    STATUS_ONLINE = "ONLINE"

    #: A constant which can be used with the status property of a Tablespace.
    #: This constant has a value of "OFFLINE"
    STATUS_OFFLINE = "OFFLINE"

    #: A constant which can be used with the status property of a Tablespace.
    #: This constant has a value of "READ_ONLY"
    STATUS_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the logging property of a Tablespace.
    #: This constant has a value of "LOGGING"
    LOGGING_LOGGING = "LOGGING"

    #: A constant which can be used with the logging property of a Tablespace.
    #: This constant has a value of "NOLOGGING"
    LOGGING_NOLOGGING = "NOLOGGING"

    #: A constant which can be used with the extent_management property of a Tablespace.
    #: This constant has a value of "LOCAL"
    EXTENT_MANAGEMENT_LOCAL = "LOCAL"

    #: A constant which can be used with the extent_management property of a Tablespace.
    #: This constant has a value of "DICTIONARY"
    EXTENT_MANAGEMENT_DICTIONARY = "DICTIONARY"

    #: A constant which can be used with the allocation_type property of a Tablespace.
    #: This constant has a value of "SYSTEM"
    ALLOCATION_TYPE_SYSTEM = "SYSTEM"

    #: A constant which can be used with the allocation_type property of a Tablespace.
    #: This constant has a value of "UNIFORM"
    ALLOCATION_TYPE_UNIFORM = "UNIFORM"

    #: A constant which can be used with the allocation_type property of a Tablespace.
    #: This constant has a value of "USER"
    ALLOCATION_TYPE_USER = "USER"

    #: A constant which can be used with the segment_space_management property of a Tablespace.
    #: This constant has a value of "MANUAL"
    SEGMENT_SPACE_MANAGEMENT_MANUAL = "MANUAL"

    #: A constant which can be used with the segment_space_management property of a Tablespace.
    #: This constant has a value of "AUTO"
    SEGMENT_SPACE_MANAGEMENT_AUTO = "AUTO"

    #: A constant which can be used with the default_table_compression property of a Tablespace.
    #: This constant has a value of "ENABLED"
    DEFAULT_TABLE_COMPRESSION_ENABLED = "ENABLED"

    #: A constant which can be used with the default_table_compression property of a Tablespace.
    #: This constant has a value of "DISABLED"
    DEFAULT_TABLE_COMPRESSION_DISABLED = "DISABLED"

    #: A constant which can be used with the retention property of a Tablespace.
    #: This constant has a value of "GUARANTEE"
    RETENTION_GUARANTEE = "GUARANTEE"

    #: A constant which can be used with the retention property of a Tablespace.
    #: This constant has a value of "NOGUARANTEE"
    RETENTION_NOGUARANTEE = "NOGUARANTEE"

    #: A constant which can be used with the retention property of a Tablespace.
    #: This constant has a value of "NOT_APPLY"
    RETENTION_NOT_APPLY = "NOT_APPLY"

    #: A constant which can be used with the predicate_evaluation property of a Tablespace.
    #: This constant has a value of "HOST"
    PREDICATE_EVALUATION_HOST = "HOST"

    #: A constant which can be used with the predicate_evaluation property of a Tablespace.
    #: This constant has a value of "STORAGE"
    PREDICATE_EVALUATION_STORAGE = "STORAGE"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "BASIC"
    COMPRESS_FOR_BASIC = "BASIC"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "ADVANCED"
    COMPRESS_FOR_ADVANCED = "ADVANCED"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "QUERY_LOW"
    COMPRESS_FOR_QUERY_LOW = "QUERY_LOW"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "QUERY_HIGH"
    COMPRESS_FOR_QUERY_HIGH = "QUERY_HIGH"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "ARCHIVE_LOW"
    COMPRESS_FOR_ARCHIVE_LOW = "ARCHIVE_LOW"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "ARCHIVE_HIGH"
    COMPRESS_FOR_ARCHIVE_HIGH = "ARCHIVE_HIGH"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "DIRECT_LOAD_ONLY"
    COMPRESS_FOR_DIRECT_LOAD_ONLY = "DIRECT_LOAD_ONLY"

    #: A constant which can be used with the compress_for property of a Tablespace.
    #: This constant has a value of "FOR_ALL_OPERATIONS"
    COMPRESS_FOR_FOR_ALL_OPERATIONS = "FOR_ALL_OPERATIONS"

    #: A constant which can be used with the default_in_memory property of a Tablespace.
    #: This constant has a value of "ENABLED"
    DEFAULT_IN_MEMORY_ENABLED = "ENABLED"

    #: A constant which can be used with the default_in_memory property of a Tablespace.
    #: This constant has a value of "DISABLED"
    DEFAULT_IN_MEMORY_DISABLED = "DISABLED"

    #: A constant which can be used with the default_in_memory_priority property of a Tablespace.
    #: This constant has a value of "LOW"
    DEFAULT_IN_MEMORY_PRIORITY_LOW = "LOW"

    #: A constant which can be used with the default_in_memory_priority property of a Tablespace.
    #: This constant has a value of "MEDIUM"
    DEFAULT_IN_MEMORY_PRIORITY_MEDIUM = "MEDIUM"

    #: A constant which can be used with the default_in_memory_priority property of a Tablespace.
    #: This constant has a value of "HIGH"
    DEFAULT_IN_MEMORY_PRIORITY_HIGH = "HIGH"

    #: A constant which can be used with the default_in_memory_priority property of a Tablespace.
    #: This constant has a value of "CRITICAL"
    DEFAULT_IN_MEMORY_PRIORITY_CRITICAL = "CRITICAL"

    #: A constant which can be used with the default_in_memory_priority property of a Tablespace.
    #: This constant has a value of "NONE"
    DEFAULT_IN_MEMORY_PRIORITY_NONE = "NONE"

    #: A constant which can be used with the default_in_memory_distribute property of a Tablespace.
    #: This constant has a value of "AUTO"
    DEFAULT_IN_MEMORY_DISTRIBUTE_AUTO = "AUTO"

    #: A constant which can be used with the default_in_memory_distribute property of a Tablespace.
    #: This constant has a value of "BY_ROWID_RANGE"
    DEFAULT_IN_MEMORY_DISTRIBUTE_BY_ROWID_RANGE = "BY_ROWID_RANGE"

    #: A constant which can be used with the default_in_memory_distribute property of a Tablespace.
    #: This constant has a value of "BY_PARTITION"
    DEFAULT_IN_MEMORY_DISTRIBUTE_BY_PARTITION = "BY_PARTITION"

    #: A constant which can be used with the default_in_memory_distribute property of a Tablespace.
    #: This constant has a value of "BY_SUBPARTITION"
    DEFAULT_IN_MEMORY_DISTRIBUTE_BY_SUBPARTITION = "BY_SUBPARTITION"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "NO_MEMCOMPRESS"
    DEFAULT_IN_MEMORY_COMPRESSION_NO_MEMCOMPRESS = "NO_MEMCOMPRESS"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "FOR_DML"
    DEFAULT_IN_MEMORY_COMPRESSION_FOR_DML = "FOR_DML"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "FOR_QUERY_LOW"
    DEFAULT_IN_MEMORY_COMPRESSION_FOR_QUERY_LOW = "FOR_QUERY_LOW"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "FOR_QUERY_HIGH"
    DEFAULT_IN_MEMORY_COMPRESSION_FOR_QUERY_HIGH = "FOR_QUERY_HIGH"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "FOR_CAPACITY_LOW"
    DEFAULT_IN_MEMORY_COMPRESSION_FOR_CAPACITY_LOW = "FOR_CAPACITY_LOW"

    #: A constant which can be used with the default_in_memory_compression property of a Tablespace.
    #: This constant has a value of "FOR_CAPACITY_HIGH"
    DEFAULT_IN_MEMORY_COMPRESSION_FOR_CAPACITY_HIGH = "FOR_CAPACITY_HIGH"

    #: A constant which can be used with the default_in_memory_duplicate property of a Tablespace.
    #: This constant has a value of "NO_DUPLICATE"
    DEFAULT_IN_MEMORY_DUPLICATE_NO_DUPLICATE = "NO_DUPLICATE"

    #: A constant which can be used with the default_in_memory_duplicate property of a Tablespace.
    #: This constant has a value of "DUPLICATE"
    DEFAULT_IN_MEMORY_DUPLICATE_DUPLICATE = "DUPLICATE"

    #: A constant which can be used with the default_in_memory_duplicate property of a Tablespace.
    #: This constant has a value of "DUPLICATE_ALL"
    DEFAULT_IN_MEMORY_DUPLICATE_DUPLICATE_ALL = "DUPLICATE_ALL"

    #: A constant which can be used with the shared property of a Tablespace.
    #: This constant has a value of "SHARED"
    SHARED_SHARED = "SHARED"

    #: A constant which can be used with the shared property of a Tablespace.
    #: This constant has a value of "LOCAL_ON_LEAF"
    SHARED_LOCAL_ON_LEAF = "LOCAL_ON_LEAF"

    #: A constant which can be used with the shared property of a Tablespace.
    #: This constant has a value of "LOCAL_ON_ALL"
    SHARED_LOCAL_ON_ALL = "LOCAL_ON_ALL"

    #: A constant which can be used with the default_index_compression property of a Tablespace.
    #: This constant has a value of "ENABLED"
    DEFAULT_INDEX_COMPRESSION_ENABLED = "ENABLED"

    #: A constant which can be used with the default_index_compression property of a Tablespace.
    #: This constant has a value of "DISABLED"
    DEFAULT_INDEX_COMPRESSION_DISABLED = "DISABLED"

    #: A constant which can be used with the index_compress_for property of a Tablespace.
    #: This constant has a value of "ADVANCED_LOW"
    INDEX_COMPRESS_FOR_ADVANCED_LOW = "ADVANCED_LOW"

    #: A constant which can be used with the index_compress_for property of a Tablespace.
    #: This constant has a value of "ADVANCED_HIGH"
    INDEX_COMPRESS_FOR_ADVANCED_HIGH = "ADVANCED_HIGH"

    #: A constant which can be used with the default_in_memory_service property of a Tablespace.
    #: This constant has a value of "DEFAULT"
    DEFAULT_IN_MEMORY_SERVICE_DEFAULT = "DEFAULT"

    #: A constant which can be used with the default_in_memory_service property of a Tablespace.
    #: This constant has a value of "NONE"
    DEFAULT_IN_MEMORY_SERVICE_NONE = "NONE"

    #: A constant which can be used with the default_in_memory_service property of a Tablespace.
    #: This constant has a value of "ALL"
    DEFAULT_IN_MEMORY_SERVICE_ALL = "ALL"

    #: A constant which can be used with the default_in_memory_service property of a Tablespace.
    #: This constant has a value of "USER_DEFINED"
    DEFAULT_IN_MEMORY_SERVICE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the lost_write_protect property of a Tablespace.
    #: This constant has a value of "ENABLED"
    LOST_WRITE_PROTECT_ENABLED = "ENABLED"

    #: A constant which can be used with the lost_write_protect property of a Tablespace.
    #: This constant has a value of "PROTECT_OFF"
    LOST_WRITE_PROTECT_PROTECT_OFF = "PROTECT_OFF"

    #: A constant which can be used with the lost_write_protect property of a Tablespace.
    #: This constant has a value of "SUSPEND"
    LOST_WRITE_PROTECT_SUSPEND = "SUSPEND"

    def __init__(self, **kwargs):
        """
        Initializes a new Tablespace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Tablespace.
        :type name: str

        :param type:
            The value to assign to the type property of this Tablespace.
            Allowed values for this property are: "UNDO", "LOST_WRITE_PROTECTION", "PERMANENT", "TEMPORARY"
        :type type: str

        :param status:
            The value to assign to the status property of this Tablespace.
            Allowed values for this property are: "ONLINE", "OFFLINE", "READ_ONLY"
        :type status: str

        :param block_size_bytes:
            The value to assign to the block_size_bytes property of this Tablespace.
        :type block_size_bytes: float

        :param logging:
            The value to assign to the logging property of this Tablespace.
            Allowed values for this property are: "LOGGING", "NOLOGGING"
        :type logging: str

        :param is_force_logging:
            The value to assign to the is_force_logging property of this Tablespace.
        :type is_force_logging: bool

        :param extent_management:
            The value to assign to the extent_management property of this Tablespace.
            Allowed values for this property are: "LOCAL", "DICTIONARY"
        :type extent_management: str

        :param allocation_type:
            The value to assign to the allocation_type property of this Tablespace.
            Allowed values for this property are: "SYSTEM", "UNIFORM", "USER"
        :type allocation_type: str

        :param is_plugged_in:
            The value to assign to the is_plugged_in property of this Tablespace.
        :type is_plugged_in: bool

        :param segment_space_management:
            The value to assign to the segment_space_management property of this Tablespace.
            Allowed values for this property are: "MANUAL", "AUTO"
        :type segment_space_management: str

        :param default_table_compression:
            The value to assign to the default_table_compression property of this Tablespace.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type default_table_compression: str

        :param retention:
            The value to assign to the retention property of this Tablespace.
            Allowed values for this property are: "GUARANTEE", "NOGUARANTEE", "NOT_APPLY"
        :type retention: str

        :param is_bigfile:
            The value to assign to the is_bigfile property of this Tablespace.
        :type is_bigfile: bool

        :param predicate_evaluation:
            The value to assign to the predicate_evaluation property of this Tablespace.
            Allowed values for this property are: "HOST", "STORAGE"
        :type predicate_evaluation: str

        :param is_encrypted:
            The value to assign to the is_encrypted property of this Tablespace.
        :type is_encrypted: bool

        :param compress_for:
            The value to assign to the compress_for property of this Tablespace.
            Allowed values for this property are: "BASIC", "ADVANCED", "QUERY_LOW", "QUERY_HIGH", "ARCHIVE_LOW", "ARCHIVE_HIGH", "DIRECT_LOAD_ONLY", "FOR_ALL_OPERATIONS"
        :type compress_for: str

        :param default_in_memory:
            The value to assign to the default_in_memory property of this Tablespace.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type default_in_memory: str

        :param default_in_memory_priority:
            The value to assign to the default_in_memory_priority property of this Tablespace.
            Allowed values for this property are: "LOW", "MEDIUM", "HIGH", "CRITICAL", "NONE"
        :type default_in_memory_priority: str

        :param default_in_memory_distribute:
            The value to assign to the default_in_memory_distribute property of this Tablespace.
            Allowed values for this property are: "AUTO", "BY_ROWID_RANGE", "BY_PARTITION", "BY_SUBPARTITION"
        :type default_in_memory_distribute: str

        :param default_in_memory_compression:
            The value to assign to the default_in_memory_compression property of this Tablespace.
            Allowed values for this property are: "NO_MEMCOMPRESS", "FOR_DML", "FOR_QUERY_LOW", "FOR_QUERY_HIGH", "FOR_CAPACITY_LOW", "FOR_CAPACITY_HIGH"
        :type default_in_memory_compression: str

        :param default_in_memory_duplicate:
            The value to assign to the default_in_memory_duplicate property of this Tablespace.
            Allowed values for this property are: "NO_DUPLICATE", "DUPLICATE", "DUPLICATE_ALL"
        :type default_in_memory_duplicate: str

        :param shared:
            The value to assign to the shared property of this Tablespace.
            Allowed values for this property are: "SHARED", "LOCAL_ON_LEAF", "LOCAL_ON_ALL"
        :type shared: str

        :param default_index_compression:
            The value to assign to the default_index_compression property of this Tablespace.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type default_index_compression: str

        :param index_compress_for:
            The value to assign to the index_compress_for property of this Tablespace.
            Allowed values for this property are: "ADVANCED_LOW", "ADVANCED_HIGH"
        :type index_compress_for: str

        :param default_cell_memory:
            The value to assign to the default_cell_memory property of this Tablespace.
        :type default_cell_memory: str

        :param default_in_memory_service:
            The value to assign to the default_in_memory_service property of this Tablespace.
            Allowed values for this property are: "DEFAULT", "NONE", "ALL", "USER_DEFINED"
        :type default_in_memory_service: str

        :param default_in_memory_service_name:
            The value to assign to the default_in_memory_service_name property of this Tablespace.
        :type default_in_memory_service_name: str

        :param lost_write_protect:
            The value to assign to the lost_write_protect property of this Tablespace.
            Allowed values for this property are: "ENABLED", "PROTECT_OFF", "SUSPEND"
        :type lost_write_protect: str

        :param is_chunk_tablespace:
            The value to assign to the is_chunk_tablespace property of this Tablespace.
        :type is_chunk_tablespace: bool

        :param temp_group:
            The value to assign to the temp_group property of this Tablespace.
        :type temp_group: str

        :param max_size_kb:
            The value to assign to the max_size_kb property of this Tablespace.
        :type max_size_kb: float

        :param allocated_size_kb:
            The value to assign to the allocated_size_kb property of this Tablespace.
        :type allocated_size_kb: float

        :param user_size_kb:
            The value to assign to the user_size_kb property of this Tablespace.
        :type user_size_kb: float

        :param free_space_kb:
            The value to assign to the free_space_kb property of this Tablespace.
        :type free_space_kb: float

        :param used_space_kb:
            The value to assign to the used_space_kb property of this Tablespace.
        :type used_space_kb: float

        :param used_percent_available:
            The value to assign to the used_percent_available property of this Tablespace.
        :type used_percent_available: float

        :param used_percent_allocated:
            The value to assign to the used_percent_allocated property of this Tablespace.
        :type used_percent_allocated: float

        :param datafiles:
            The value to assign to the datafiles property of this Tablespace.
        :type datafiles: list[oci.database_management.models.Datafile]

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'status': 'str',
            'block_size_bytes': 'float',
            'logging': 'str',
            'is_force_logging': 'bool',
            'extent_management': 'str',
            'allocation_type': 'str',
            'is_plugged_in': 'bool',
            'segment_space_management': 'str',
            'default_table_compression': 'str',
            'retention': 'str',
            'is_bigfile': 'bool',
            'predicate_evaluation': 'str',
            'is_encrypted': 'bool',
            'compress_for': 'str',
            'default_in_memory': 'str',
            'default_in_memory_priority': 'str',
            'default_in_memory_distribute': 'str',
            'default_in_memory_compression': 'str',
            'default_in_memory_duplicate': 'str',
            'shared': 'str',
            'default_index_compression': 'str',
            'index_compress_for': 'str',
            'default_cell_memory': 'str',
            'default_in_memory_service': 'str',
            'default_in_memory_service_name': 'str',
            'lost_write_protect': 'str',
            'is_chunk_tablespace': 'bool',
            'temp_group': 'str',
            'max_size_kb': 'float',
            'allocated_size_kb': 'float',
            'user_size_kb': 'float',
            'free_space_kb': 'float',
            'used_space_kb': 'float',
            'used_percent_available': 'float',
            'used_percent_allocated': 'float',
            'datafiles': 'list[Datafile]'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'status': 'status',
            'block_size_bytes': 'blockSizeBytes',
            'logging': 'logging',
            'is_force_logging': 'isForceLogging',
            'extent_management': 'extentManagement',
            'allocation_type': 'allocationType',
            'is_plugged_in': 'isPluggedIn',
            'segment_space_management': 'segmentSpaceManagement',
            'default_table_compression': 'defaultTableCompression',
            'retention': 'retention',
            'is_bigfile': 'isBigfile',
            'predicate_evaluation': 'predicateEvaluation',
            'is_encrypted': 'isEncrypted',
            'compress_for': 'compressFor',
            'default_in_memory': 'defaultInMemory',
            'default_in_memory_priority': 'defaultInMemoryPriority',
            'default_in_memory_distribute': 'defaultInMemoryDistribute',
            'default_in_memory_compression': 'defaultInMemoryCompression',
            'default_in_memory_duplicate': 'defaultInMemoryDuplicate',
            'shared': 'shared',
            'default_index_compression': 'defaultIndexCompression',
            'index_compress_for': 'indexCompressFor',
            'default_cell_memory': 'defaultCellMemory',
            'default_in_memory_service': 'defaultInMemoryService',
            'default_in_memory_service_name': 'defaultInMemoryServiceName',
            'lost_write_protect': 'lostWriteProtect',
            'is_chunk_tablespace': 'isChunkTablespace',
            'temp_group': 'tempGroup',
            'max_size_kb': 'maxSizeKB',
            'allocated_size_kb': 'allocatedSizeKB',
            'user_size_kb': 'userSizeKB',
            'free_space_kb': 'freeSpaceKB',
            'used_space_kb': 'usedSpaceKB',
            'used_percent_available': 'usedPercentAvailable',
            'used_percent_allocated': 'usedPercentAllocated',
            'datafiles': 'datafiles'
        }

        self._name = None
        self._type = None
        self._status = None
        self._block_size_bytes = None
        self._logging = None
        self._is_force_logging = None
        self._extent_management = None
        self._allocation_type = None
        self._is_plugged_in = None
        self._segment_space_management = None
        self._default_table_compression = None
        self._retention = None
        self._is_bigfile = None
        self._predicate_evaluation = None
        self._is_encrypted = None
        self._compress_for = None
        self._default_in_memory = None
        self._default_in_memory_priority = None
        self._default_in_memory_distribute = None
        self._default_in_memory_compression = None
        self._default_in_memory_duplicate = None
        self._shared = None
        self._default_index_compression = None
        self._index_compress_for = None
        self._default_cell_memory = None
        self._default_in_memory_service = None
        self._default_in_memory_service_name = None
        self._lost_write_protect = None
        self._is_chunk_tablespace = None
        self._temp_group = None
        self._max_size_kb = None
        self._allocated_size_kb = None
        self._user_size_kb = None
        self._free_space_kb = None
        self._used_space_kb = None
        self._used_percent_available = None
        self._used_percent_allocated = None
        self._datafiles = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Tablespace.
        The name of the tablespace.


        :return: The name of this Tablespace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tablespace.
        The name of the tablespace.


        :param name: The name of this Tablespace.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Tablespace.
        The type of tablespace.

        Allowed values for this property are: "UNDO", "LOST_WRITE_PROTECTION", "PERMANENT", "TEMPORARY"


        :return: The type of this Tablespace.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Tablespace.
        The type of tablespace.


        :param type: The type of this Tablespace.
        :type: str
        """
        allowed_values = ["UNDO", "LOST_WRITE_PROTECTION", "PERMANENT", "TEMPORARY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def status(self):
        """
        Gets the status of this Tablespace.
        The status of the tablespace.

        Allowed values for this property are: "ONLINE", "OFFLINE", "READ_ONLY"


        :return: The status of this Tablespace.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Tablespace.
        The status of the tablespace.


        :param status: The status of this Tablespace.
        :type: str
        """
        allowed_values = ["ONLINE", "OFFLINE", "READ_ONLY"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def block_size_bytes(self):
        """
        Gets the block_size_bytes of this Tablespace.
        The tablespace block size.


        :return: The block_size_bytes of this Tablespace.
        :rtype: float
        """
        return self._block_size_bytes

    @block_size_bytes.setter
    def block_size_bytes(self, block_size_bytes):
        """
        Sets the block_size_bytes of this Tablespace.
        The tablespace block size.


        :param block_size_bytes: The block_size_bytes of this Tablespace.
        :type: float
        """
        self._block_size_bytes = block_size_bytes

    @property
    def logging(self):
        """
        Gets the logging of this Tablespace.
        The default logging attribute.

        Allowed values for this property are: "LOGGING", "NOLOGGING"


        :return: The logging of this Tablespace.
        :rtype: str
        """
        return self._logging

    @logging.setter
    def logging(self, logging):
        """
        Sets the logging of this Tablespace.
        The default logging attribute.


        :param logging: The logging of this Tablespace.
        :type: str
        """
        allowed_values = ["LOGGING", "NOLOGGING"]
        if not value_allowed_none_or_none_sentinel(logging, allowed_values):
            raise ValueError(
                "Invalid value for `logging`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._logging = logging

    @property
    def is_force_logging(self):
        """
        Gets the is_force_logging of this Tablespace.
        Indicates whether the tablespace is under Force Logging mode.


        :return: The is_force_logging of this Tablespace.
        :rtype: bool
        """
        return self._is_force_logging

    @is_force_logging.setter
    def is_force_logging(self, is_force_logging):
        """
        Sets the is_force_logging of this Tablespace.
        Indicates whether the tablespace is under Force Logging mode.


        :param is_force_logging: The is_force_logging of this Tablespace.
        :type: bool
        """
        self._is_force_logging = is_force_logging

    @property
    def extent_management(self):
        """
        Gets the extent_management of this Tablespace.
        Indicates whether the extents in the tablespace are Locally managed or Dictionary managed.

        Allowed values for this property are: "LOCAL", "DICTIONARY"


        :return: The extent_management of this Tablespace.
        :rtype: str
        """
        return self._extent_management

    @extent_management.setter
    def extent_management(self, extent_management):
        """
        Sets the extent_management of this Tablespace.
        Indicates whether the extents in the tablespace are Locally managed or Dictionary managed.


        :param extent_management: The extent_management of this Tablespace.
        :type: str
        """
        allowed_values = ["LOCAL", "DICTIONARY"]
        if not value_allowed_none_or_none_sentinel(extent_management, allowed_values):
            raise ValueError(
                "Invalid value for `extent_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._extent_management = extent_management

    @property
    def allocation_type(self):
        """
        Gets the allocation_type of this Tablespace.
        The type of extent allocation in effect for the tablespace.

        Allowed values for this property are: "SYSTEM", "UNIFORM", "USER"


        :return: The allocation_type of this Tablespace.
        :rtype: str
        """
        return self._allocation_type

    @allocation_type.setter
    def allocation_type(self, allocation_type):
        """
        Sets the allocation_type of this Tablespace.
        The type of extent allocation in effect for the tablespace.


        :param allocation_type: The allocation_type of this Tablespace.
        :type: str
        """
        allowed_values = ["SYSTEM", "UNIFORM", "USER"]
        if not value_allowed_none_or_none_sentinel(allocation_type, allowed_values):
            raise ValueError(
                "Invalid value for `allocation_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._allocation_type = allocation_type

    @property
    def is_plugged_in(self):
        """
        Gets the is_plugged_in of this Tablespace.
        Indicates whether the tablespace is plugged in.


        :return: The is_plugged_in of this Tablespace.
        :rtype: bool
        """
        return self._is_plugged_in

    @is_plugged_in.setter
    def is_plugged_in(self, is_plugged_in):
        """
        Sets the is_plugged_in of this Tablespace.
        Indicates whether the tablespace is plugged in.


        :param is_plugged_in: The is_plugged_in of this Tablespace.
        :type: bool
        """
        self._is_plugged_in = is_plugged_in

    @property
    def segment_space_management(self):
        """
        Gets the segment_space_management of this Tablespace.
        Indicates whether the free and used segment space in the tablespace is managed using free lists (MANUAL) or bitmaps (AUTO).

        Allowed values for this property are: "MANUAL", "AUTO"


        :return: The segment_space_management of this Tablespace.
        :rtype: str
        """
        return self._segment_space_management

    @segment_space_management.setter
    def segment_space_management(self, segment_space_management):
        """
        Sets the segment_space_management of this Tablespace.
        Indicates whether the free and used segment space in the tablespace is managed using free lists (MANUAL) or bitmaps (AUTO).


        :param segment_space_management: The segment_space_management of this Tablespace.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTO"]
        if not value_allowed_none_or_none_sentinel(segment_space_management, allowed_values):
            raise ValueError(
                "Invalid value for `segment_space_management`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._segment_space_management = segment_space_management

    @property
    def default_table_compression(self):
        """
        Gets the default_table_compression of this Tablespace.
        Indicates whether default table compression is enabled or disabled.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The default_table_compression of this Tablespace.
        :rtype: str
        """
        return self._default_table_compression

    @default_table_compression.setter
    def default_table_compression(self, default_table_compression):
        """
        Sets the default_table_compression of this Tablespace.
        Indicates whether default table compression is enabled or disabled.


        :param default_table_compression: The default_table_compression of this Tablespace.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(default_table_compression, allowed_values):
            raise ValueError(
                "Invalid value for `default_table_compression`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_table_compression = default_table_compression

    @property
    def retention(self):
        """
        Gets the retention of this Tablespace.
        Indicates whether undo retention guarantee is enabled for the tablespace.

        Allowed values for this property are: "GUARANTEE", "NOGUARANTEE", "NOT_APPLY"


        :return: The retention of this Tablespace.
        :rtype: str
        """
        return self._retention

    @retention.setter
    def retention(self, retention):
        """
        Sets the retention of this Tablespace.
        Indicates whether undo retention guarantee is enabled for the tablespace.


        :param retention: The retention of this Tablespace.
        :type: str
        """
        allowed_values = ["GUARANTEE", "NOGUARANTEE", "NOT_APPLY"]
        if not value_allowed_none_or_none_sentinel(retention, allowed_values):
            raise ValueError(
                "Invalid value for `retention`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._retention = retention

    @property
    def is_bigfile(self):
        """
        Gets the is_bigfile of this Tablespace.
        Indicates whether the tablespace is a Bigfile tablespace or a Smallfile tablespace.


        :return: The is_bigfile of this Tablespace.
        :rtype: bool
        """
        return self._is_bigfile

    @is_bigfile.setter
    def is_bigfile(self, is_bigfile):
        """
        Sets the is_bigfile of this Tablespace.
        Indicates whether the tablespace is a Bigfile tablespace or a Smallfile tablespace.


        :param is_bigfile: The is_bigfile of this Tablespace.
        :type: bool
        """
        self._is_bigfile = is_bigfile

    @property
    def predicate_evaluation(self):
        """
        Gets the predicate_evaluation of this Tablespace.
        Indicates whether predicates are evaluated by Host or by Storage.

        Allowed values for this property are: "HOST", "STORAGE"


        :return: The predicate_evaluation of this Tablespace.
        :rtype: str
        """
        return self._predicate_evaluation

    @predicate_evaluation.setter
    def predicate_evaluation(self, predicate_evaluation):
        """
        Sets the predicate_evaluation of this Tablespace.
        Indicates whether predicates are evaluated by Host or by Storage.


        :param predicate_evaluation: The predicate_evaluation of this Tablespace.
        :type: str
        """
        allowed_values = ["HOST", "STORAGE"]
        if not value_allowed_none_or_none_sentinel(predicate_evaluation, allowed_values):
            raise ValueError(
                "Invalid value for `predicate_evaluation`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._predicate_evaluation = predicate_evaluation

    @property
    def is_encrypted(self):
        """
        Gets the is_encrypted of this Tablespace.
        Indicates whether the tablespace is encrypted.


        :return: The is_encrypted of this Tablespace.
        :rtype: bool
        """
        return self._is_encrypted

    @is_encrypted.setter
    def is_encrypted(self, is_encrypted):
        """
        Sets the is_encrypted of this Tablespace.
        Indicates whether the tablespace is encrypted.


        :param is_encrypted: The is_encrypted of this Tablespace.
        :type: bool
        """
        self._is_encrypted = is_encrypted

    @property
    def compress_for(self):
        """
        Gets the compress_for of this Tablespace.
        The operation type for which default compression is enabled.

        Allowed values for this property are: "BASIC", "ADVANCED", "QUERY_LOW", "QUERY_HIGH", "ARCHIVE_LOW", "ARCHIVE_HIGH", "DIRECT_LOAD_ONLY", "FOR_ALL_OPERATIONS"


        :return: The compress_for of this Tablespace.
        :rtype: str
        """
        return self._compress_for

    @compress_for.setter
    def compress_for(self, compress_for):
        """
        Sets the compress_for of this Tablespace.
        The operation type for which default compression is enabled.


        :param compress_for: The compress_for of this Tablespace.
        :type: str
        """
        allowed_values = ["BASIC", "ADVANCED", "QUERY_LOW", "QUERY_HIGH", "ARCHIVE_LOW", "ARCHIVE_HIGH", "DIRECT_LOAD_ONLY", "FOR_ALL_OPERATIONS"]
        if not value_allowed_none_or_none_sentinel(compress_for, allowed_values):
            raise ValueError(
                "Invalid value for `compress_for`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._compress_for = compress_for

    @property
    def default_in_memory(self):
        """
        Gets the default_in_memory of this Tablespace.
        Indicates whether the In-Memory Column Store (IM column store) is by default enabled or disabled for tables in the tablespace.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The default_in_memory of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory

    @default_in_memory.setter
    def default_in_memory(self, default_in_memory):
        """
        Sets the default_in_memory of this Tablespace.
        Indicates whether the In-Memory Column Store (IM column store) is by default enabled or disabled for tables in the tablespace.


        :param default_in_memory: The default_in_memory of this Tablespace.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(default_in_memory, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory = default_in_memory

    @property
    def default_in_memory_priority(self):
        """
        Gets the default_in_memory_priority of this Tablespace.
        Indicates the default priority for In-Memory Column Store (IM column store) population for the tablespace.

        Allowed values for this property are: "LOW", "MEDIUM", "HIGH", "CRITICAL", "NONE"


        :return: The default_in_memory_priority of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_priority

    @default_in_memory_priority.setter
    def default_in_memory_priority(self, default_in_memory_priority):
        """
        Sets the default_in_memory_priority of this Tablespace.
        Indicates the default priority for In-Memory Column Store (IM column store) population for the tablespace.


        :param default_in_memory_priority: The default_in_memory_priority of this Tablespace.
        :type: str
        """
        allowed_values = ["LOW", "MEDIUM", "HIGH", "CRITICAL", "NONE"]
        if not value_allowed_none_or_none_sentinel(default_in_memory_priority, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory_priority`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory_priority = default_in_memory_priority

    @property
    def default_in_memory_distribute(self):
        """
        Gets the default_in_memory_distribute of this Tablespace.
        Indicates how the IM column store is distributed by default for the tablespace in an Oracle Real Application Clusters (Oracle RAC) environment.

        Allowed values for this property are: "AUTO", "BY_ROWID_RANGE", "BY_PARTITION", "BY_SUBPARTITION"


        :return: The default_in_memory_distribute of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_distribute

    @default_in_memory_distribute.setter
    def default_in_memory_distribute(self, default_in_memory_distribute):
        """
        Sets the default_in_memory_distribute of this Tablespace.
        Indicates how the IM column store is distributed by default for the tablespace in an Oracle Real Application Clusters (Oracle RAC) environment.


        :param default_in_memory_distribute: The default_in_memory_distribute of this Tablespace.
        :type: str
        """
        allowed_values = ["AUTO", "BY_ROWID_RANGE", "BY_PARTITION", "BY_SUBPARTITION"]
        if not value_allowed_none_or_none_sentinel(default_in_memory_distribute, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory_distribute`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory_distribute = default_in_memory_distribute

    @property
    def default_in_memory_compression(self):
        """
        Gets the default_in_memory_compression of this Tablespace.
        Indicates the default compression level for the IM column store for the tablespace.

        Allowed values for this property are: "NO_MEMCOMPRESS", "FOR_DML", "FOR_QUERY_LOW", "FOR_QUERY_HIGH", "FOR_CAPACITY_LOW", "FOR_CAPACITY_HIGH"


        :return: The default_in_memory_compression of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_compression

    @default_in_memory_compression.setter
    def default_in_memory_compression(self, default_in_memory_compression):
        """
        Sets the default_in_memory_compression of this Tablespace.
        Indicates the default compression level for the IM column store for the tablespace.


        :param default_in_memory_compression: The default_in_memory_compression of this Tablespace.
        :type: str
        """
        allowed_values = ["NO_MEMCOMPRESS", "FOR_DML", "FOR_QUERY_LOW", "FOR_QUERY_HIGH", "FOR_CAPACITY_LOW", "FOR_CAPACITY_HIGH"]
        if not value_allowed_none_or_none_sentinel(default_in_memory_compression, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory_compression`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory_compression = default_in_memory_compression

    @property
    def default_in_memory_duplicate(self):
        """
        Gets the default_in_memory_duplicate of this Tablespace.
        Indicates the duplicate setting for the IM column store in an Oracle RAC environment.

        Allowed values for this property are: "NO_DUPLICATE", "DUPLICATE", "DUPLICATE_ALL"


        :return: The default_in_memory_duplicate of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_duplicate

    @default_in_memory_duplicate.setter
    def default_in_memory_duplicate(self, default_in_memory_duplicate):
        """
        Sets the default_in_memory_duplicate of this Tablespace.
        Indicates the duplicate setting for the IM column store in an Oracle RAC environment.


        :param default_in_memory_duplicate: The default_in_memory_duplicate of this Tablespace.
        :type: str
        """
        allowed_values = ["NO_DUPLICATE", "DUPLICATE", "DUPLICATE_ALL"]
        if not value_allowed_none_or_none_sentinel(default_in_memory_duplicate, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory_duplicate`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory_duplicate = default_in_memory_duplicate

    @property
    def shared(self):
        """
        Gets the shared of this Tablespace.
        Indicates whether the tablespace is for shared tablespace, or for local temporary tablespace for leaf (read-only) instances, or for local temporary tablespace for all instance types.

        Allowed values for this property are: "SHARED", "LOCAL_ON_LEAF", "LOCAL_ON_ALL"


        :return: The shared of this Tablespace.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this Tablespace.
        Indicates whether the tablespace is for shared tablespace, or for local temporary tablespace for leaf (read-only) instances, or for local temporary tablespace for all instance types.


        :param shared: The shared of this Tablespace.
        :type: str
        """
        allowed_values = ["SHARED", "LOCAL_ON_LEAF", "LOCAL_ON_ALL"]
        if not value_allowed_none_or_none_sentinel(shared, allowed_values):
            raise ValueError(
                "Invalid value for `shared`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._shared = shared

    @property
    def default_index_compression(self):
        """
        Gets the default_index_compression of this Tablespace.
        Indicates whether default index compression is enabled or disabled.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The default_index_compression of this Tablespace.
        :rtype: str
        """
        return self._default_index_compression

    @default_index_compression.setter
    def default_index_compression(self, default_index_compression):
        """
        Sets the default_index_compression of this Tablespace.
        Indicates whether default index compression is enabled or disabled.


        :param default_index_compression: The default_index_compression of this Tablespace.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(default_index_compression, allowed_values):
            raise ValueError(
                "Invalid value for `default_index_compression`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_index_compression = default_index_compression

    @property
    def index_compress_for(self):
        """
        Gets the index_compress_for of this Tablespace.
        The operation type for which default index compression is enabled.

        Allowed values for this property are: "ADVANCED_LOW", "ADVANCED_HIGH"


        :return: The index_compress_for of this Tablespace.
        :rtype: str
        """
        return self._index_compress_for

    @index_compress_for.setter
    def index_compress_for(self, index_compress_for):
        """
        Sets the index_compress_for of this Tablespace.
        The operation type for which default index compression is enabled.


        :param index_compress_for: The index_compress_for of this Tablespace.
        :type: str
        """
        allowed_values = ["ADVANCED_LOW", "ADVANCED_HIGH"]
        if not value_allowed_none_or_none_sentinel(index_compress_for, allowed_values):
            raise ValueError(
                "Invalid value for `index_compress_for`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._index_compress_for = index_compress_for

    @property
    def default_cell_memory(self):
        """
        Gets the default_cell_memory of this Tablespace.
        This specifies the default value for the CELLMEMORY attribute that tables created in the tablespace will inherit unless the behavior is overridden explicitly. This column is intended for use with Oracle Exadata.


        :return: The default_cell_memory of this Tablespace.
        :rtype: str
        """
        return self._default_cell_memory

    @default_cell_memory.setter
    def default_cell_memory(self, default_cell_memory):
        """
        Sets the default_cell_memory of this Tablespace.
        This specifies the default value for the CELLMEMORY attribute that tables created in the tablespace will inherit unless the behavior is overridden explicitly. This column is intended for use with Oracle Exadata.


        :param default_cell_memory: The default_cell_memory of this Tablespace.
        :type: str
        """
        self._default_cell_memory = default_cell_memory

    @property
    def default_in_memory_service(self):
        """
        Gets the default_in_memory_service of this Tablespace.
        Indicates how the IM column store is populated on various instances by default for the tablespace.

        Allowed values for this property are: "DEFAULT", "NONE", "ALL", "USER_DEFINED"


        :return: The default_in_memory_service of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_service

    @default_in_memory_service.setter
    def default_in_memory_service(self, default_in_memory_service):
        """
        Sets the default_in_memory_service of this Tablespace.
        Indicates how the IM column store is populated on various instances by default for the tablespace.


        :param default_in_memory_service: The default_in_memory_service of this Tablespace.
        :type: str
        """
        allowed_values = ["DEFAULT", "NONE", "ALL", "USER_DEFINED"]
        if not value_allowed_none_or_none_sentinel(default_in_memory_service, allowed_values):
            raise ValueError(
                "Invalid value for `default_in_memory_service`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._default_in_memory_service = default_in_memory_service

    @property
    def default_in_memory_service_name(self):
        """
        Gets the default_in_memory_service_name of this Tablespace.
        Indicates the service name for the service on which the IM column store should be populated by default for the tablespace. This column has a value only when the corresponding DEF_INMEMORY_SERVICE is USER_DEFINED. In all other cases, this column is null.


        :return: The default_in_memory_service_name of this Tablespace.
        :rtype: str
        """
        return self._default_in_memory_service_name

    @default_in_memory_service_name.setter
    def default_in_memory_service_name(self, default_in_memory_service_name):
        """
        Sets the default_in_memory_service_name of this Tablespace.
        Indicates the service name for the service on which the IM column store should be populated by default for the tablespace. This column has a value only when the corresponding DEF_INMEMORY_SERVICE is USER_DEFINED. In all other cases, this column is null.


        :param default_in_memory_service_name: The default_in_memory_service_name of this Tablespace.
        :type: str
        """
        self._default_in_memory_service_name = default_in_memory_service_name

    @property
    def lost_write_protect(self):
        """
        Gets the lost_write_protect of this Tablespace.
        The lost write protection setting for the tablespace.

        Allowed values for this property are: "ENABLED", "PROTECT_OFF", "SUSPEND"


        :return: The lost_write_protect of this Tablespace.
        :rtype: str
        """
        return self._lost_write_protect

    @lost_write_protect.setter
    def lost_write_protect(self, lost_write_protect):
        """
        Sets the lost_write_protect of this Tablespace.
        The lost write protection setting for the tablespace.


        :param lost_write_protect: The lost_write_protect of this Tablespace.
        :type: str
        """
        allowed_values = ["ENABLED", "PROTECT_OFF", "SUSPEND"]
        if not value_allowed_none_or_none_sentinel(lost_write_protect, allowed_values):
            raise ValueError(
                "Invalid value for `lost_write_protect`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lost_write_protect = lost_write_protect

    @property
    def is_chunk_tablespace(self):
        """
        Gets the is_chunk_tablespace of this Tablespace.
        Indicates whether this is a chunk tablespace.


        :return: The is_chunk_tablespace of this Tablespace.
        :rtype: bool
        """
        return self._is_chunk_tablespace

    @is_chunk_tablespace.setter
    def is_chunk_tablespace(self, is_chunk_tablespace):
        """
        Sets the is_chunk_tablespace of this Tablespace.
        Indicates whether this is a chunk tablespace.


        :param is_chunk_tablespace: The is_chunk_tablespace of this Tablespace.
        :type: bool
        """
        self._is_chunk_tablespace = is_chunk_tablespace

    @property
    def temp_group(self):
        """
        Gets the temp_group of this Tablespace.
        The temporary tablespace group.


        :return: The temp_group of this Tablespace.
        :rtype: str
        """
        return self._temp_group

    @temp_group.setter
    def temp_group(self, temp_group):
        """
        Sets the temp_group of this Tablespace.
        The temporary tablespace group.


        :param temp_group: The temp_group of this Tablespace.
        :type: str
        """
        self._temp_group = temp_group

    @property
    def max_size_kb(self):
        """
        Gets the max_size_kb of this Tablespace.
        The maximum tablespace size in KB. If the tablespace contains any data files with Autoextend enabled, then this column displays the amount of underlying free storage space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all its data files is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have a value of approximately 20 GB. If the tablespace contains only data files with autoextend disabled, then this column displays the allocated space for the entire tablespace, that is, the combined size of all data files in the tablespace.


        :return: The max_size_kb of this Tablespace.
        :rtype: float
        """
        return self._max_size_kb

    @max_size_kb.setter
    def max_size_kb(self, max_size_kb):
        """
        Sets the max_size_kb of this Tablespace.
        The maximum tablespace size in KB. If the tablespace contains any data files with Autoextend enabled, then this column displays the amount of underlying free storage space for the tablespace. For example, if the current tablespace size is 1 GB, the combined maximum size of all its data files is 32 GB, and its underlying storage (for example, ASM or file system storage) has 20 GB of free space, then this column will have a value of approximately 20 GB. If the tablespace contains only data files with autoextend disabled, then this column displays the allocated space for the entire tablespace, that is, the combined size of all data files in the tablespace.


        :param max_size_kb: The max_size_kb of this Tablespace.
        :type: float
        """
        self._max_size_kb = max_size_kb

    @property
    def allocated_size_kb(self):
        """
        Gets the allocated_size_kb of this Tablespace.
        The allocated tablespace size in KB.


        :return: The allocated_size_kb of this Tablespace.
        :rtype: float
        """
        return self._allocated_size_kb

    @allocated_size_kb.setter
    def allocated_size_kb(self, allocated_size_kb):
        """
        Sets the allocated_size_kb of this Tablespace.
        The allocated tablespace size in KB.


        :param allocated_size_kb: The allocated_size_kb of this Tablespace.
        :type: float
        """
        self._allocated_size_kb = allocated_size_kb

    @property
    def user_size_kb(self):
        """
        Gets the user_size_kb of this Tablespace.
        The size of the tablespace available for user data in KB. The difference between tablespace size and user data size is used for storing metadata.


        :return: The user_size_kb of this Tablespace.
        :rtype: float
        """
        return self._user_size_kb

    @user_size_kb.setter
    def user_size_kb(self, user_size_kb):
        """
        Sets the user_size_kb of this Tablespace.
        The size of the tablespace available for user data in KB. The difference between tablespace size and user data size is used for storing metadata.


        :param user_size_kb: The user_size_kb of this Tablespace.
        :type: float
        """
        self._user_size_kb = user_size_kb

    @property
    def free_space_kb(self):
        """
        Gets the free_space_kb of this Tablespace.
        The free space available in the tablespace in KB.


        :return: The free_space_kb of this Tablespace.
        :rtype: float
        """
        return self._free_space_kb

    @free_space_kb.setter
    def free_space_kb(self, free_space_kb):
        """
        Sets the free_space_kb of this Tablespace.
        The free space available in the tablespace in KB.


        :param free_space_kb: The free_space_kb of this Tablespace.
        :type: float
        """
        self._free_space_kb = free_space_kb

    @property
    def used_space_kb(self):
        """
        Gets the used_space_kb of this Tablespace.
        The total space used by the tablespace in KB.


        :return: The used_space_kb of this Tablespace.
        :rtype: float
        """
        return self._used_space_kb

    @used_space_kb.setter
    def used_space_kb(self, used_space_kb):
        """
        Sets the used_space_kb of this Tablespace.
        The total space used by the tablespace in KB.


        :param used_space_kb: The used_space_kb of this Tablespace.
        :type: float
        """
        self._used_space_kb = used_space_kb

    @property
    def used_percent_available(self):
        """
        Gets the used_percent_available of this Tablespace.
        The percentage of used space out of the maximum available space in the tablespace.


        :return: The used_percent_available of this Tablespace.
        :rtype: float
        """
        return self._used_percent_available

    @used_percent_available.setter
    def used_percent_available(self, used_percent_available):
        """
        Sets the used_percent_available of this Tablespace.
        The percentage of used space out of the maximum available space in the tablespace.


        :param used_percent_available: The used_percent_available of this Tablespace.
        :type: float
        """
        self._used_percent_available = used_percent_available

    @property
    def used_percent_allocated(self):
        """
        Gets the used_percent_allocated of this Tablespace.
        The percentage of used space out of the total allocated space in the tablespace.


        :return: The used_percent_allocated of this Tablespace.
        :rtype: float
        """
        return self._used_percent_allocated

    @used_percent_allocated.setter
    def used_percent_allocated(self, used_percent_allocated):
        """
        Sets the used_percent_allocated of this Tablespace.
        The percentage of used space out of the total allocated space in the tablespace.


        :param used_percent_allocated: The used_percent_allocated of this Tablespace.
        :type: float
        """
        self._used_percent_allocated = used_percent_allocated

    @property
    def datafiles(self):
        """
        Gets the datafiles of this Tablespace.
        A list of the data files associated with the tablespace.


        :return: The datafiles of this Tablespace.
        :rtype: list[oci.database_management.models.Datafile]
        """
        return self._datafiles

    @datafiles.setter
    def datafiles(self, datafiles):
        """
        Sets the datafiles of this Tablespace.
        A list of the data files associated with the tablespace.


        :param datafiles: The datafiles of this Tablespace.
        :type: list[oci.database_management.models.Datafile]
        """
        self._datafiles = datafiles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
