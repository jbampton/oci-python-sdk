# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectedDatabase(object):
    """
    A protected database is an Oracle Cloud Database whose
    backups are managed by Oracle Database Autonomous Recovery Service. Each protected database
    requires a recovery service subnet and a protection policy to use Recovery Service as
    the backup destination for centralized backup and recovery
    """

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "XS"
    DATABASE_SIZE_XS = "XS"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "S"
    DATABASE_SIZE_S = "S"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "M"
    DATABASE_SIZE_M = "M"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "L"
    DATABASE_SIZE_L = "L"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "XL"
    DATABASE_SIZE_XL = "XL"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "XXL"
    DATABASE_SIZE_XXL = "XXL"

    #: A constant which can be used with the database_size property of a ProtectedDatabase.
    #: This constant has a value of "AUTO"
    DATABASE_SIZE_AUTO = "AUTO"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ProtectedDatabase.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the health property of a ProtectedDatabase.
    #: This constant has a value of "PROTECTED"
    HEALTH_PROTECTED = "PROTECTED"

    #: A constant which can be used with the health property of a ProtectedDatabase.
    #: This constant has a value of "WARNING"
    HEALTH_WARNING = "WARNING"

    #: A constant which can be used with the health property of a ProtectedDatabase.
    #: This constant has a value of "ALERT"
    HEALTH_ALERT = "ALERT"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectedDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProtectedDatabase.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ProtectedDatabase.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProtectedDatabase.
        :type compartment_id: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this ProtectedDatabase.
        :type db_unique_name: str

        :param vpc_user_name:
            The value to assign to the vpc_user_name property of this ProtectedDatabase.
        :type vpc_user_name: str

        :param database_size:
            The value to assign to the database_size property of this ProtectedDatabase.
            Allowed values for this property are: "XS", "S", "M", "L", "XL", "XXL", "AUTO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_size: str

        :param protection_policy_id:
            The value to assign to the protection_policy_id property of this ProtectedDatabase.
        :type protection_policy_id: str

        :param recovery_service_subnets:
            The value to assign to the recovery_service_subnets property of this ProtectedDatabase.
        :type recovery_service_subnets: list[oci.recovery.models.RecoveryServiceSubnetDetails]

        :param database_id:
            The value to assign to the database_id property of this ProtectedDatabase.
        :type database_id: str

        :param database_size_in_gbs:
            The value to assign to the database_size_in_gbs property of this ProtectedDatabase.
        :type database_size_in_gbs: int

        :param change_rate:
            The value to assign to the change_rate property of this ProtectedDatabase.
        :type change_rate: float

        :param compression_ratio:
            The value to assign to the compression_ratio property of this ProtectedDatabase.
        :type compression_ratio: float

        :param is_redo_logs_shipped:
            The value to assign to the is_redo_logs_shipped property of this ProtectedDatabase.
        :type is_redo_logs_shipped: bool

        :param time_created:
            The value to assign to the time_created property of this ProtectedDatabase.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProtectedDatabase.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProtectedDatabase.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param health:
            The value to assign to the health property of this ProtectedDatabase.
            Allowed values for this property are: "PROTECTED", "WARNING", "ALERT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type health: str

        :param is_read_only_resource:
            The value to assign to the is_read_only_resource property of this ProtectedDatabase.
        :type is_read_only_resource: bool

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ProtectedDatabase.
        :type lifecycle_details: str

        :param health_details:
            The value to assign to the health_details property of this ProtectedDatabase.
        :type health_details: str

        :param metrics:
            The value to assign to the metrics property of this ProtectedDatabase.
        :type metrics: oci.recovery.models.Metrics

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProtectedDatabase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ProtectedDatabase.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ProtectedDatabase.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'db_unique_name': 'str',
            'vpc_user_name': 'str',
            'database_size': 'str',
            'protection_policy_id': 'str',
            'recovery_service_subnets': 'list[RecoveryServiceSubnetDetails]',
            'database_id': 'str',
            'database_size_in_gbs': 'int',
            'change_rate': 'float',
            'compression_ratio': 'float',
            'is_redo_logs_shipped': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'health': 'str',
            'is_read_only_resource': 'bool',
            'lifecycle_details': 'str',
            'health_details': 'str',
            'metrics': 'Metrics',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'db_unique_name': 'dbUniqueName',
            'vpc_user_name': 'vpcUserName',
            'database_size': 'databaseSize',
            'protection_policy_id': 'protectionPolicyId',
            'recovery_service_subnets': 'recoveryServiceSubnets',
            'database_id': 'databaseId',
            'database_size_in_gbs': 'databaseSizeInGBs',
            'change_rate': 'changeRate',
            'compression_ratio': 'compressionRatio',
            'is_redo_logs_shipped': 'isRedoLogsShipped',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'health': 'health',
            'is_read_only_resource': 'isReadOnlyResource',
            'lifecycle_details': 'lifecycleDetails',
            'health_details': 'healthDetails',
            'metrics': 'metrics',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._db_unique_name = None
        self._vpc_user_name = None
        self._database_size = None
        self._protection_policy_id = None
        self._recovery_service_subnets = None
        self._database_id = None
        self._database_size_in_gbs = None
        self._change_rate = None
        self._compression_ratio = None
        self._is_redo_logs_shipped = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._health = None
        self._is_read_only_resource = None
        self._lifecycle_details = None
        self._health_details = None
        self._metrics = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProtectedDatabase.
        The OCID of the protected database.


        :return: The id of this ProtectedDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProtectedDatabase.
        The OCID of the protected database.


        :param id: The id of this ProtectedDatabase.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ProtectedDatabase.
        The protected database name. You can change the displayName. Avoid entering confidential information.


        :return: The display_name of this ProtectedDatabase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ProtectedDatabase.
        The protected database name. You can change the displayName. Avoid entering confidential information.


        :param display_name: The display_name of this ProtectedDatabase.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProtectedDatabase.
        The OCID of the compartment that contains the protected database.


        :return: The compartment_id of this ProtectedDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProtectedDatabase.
        The OCID of the compartment that contains the protected database.


        :param compartment_id: The compartment_id of this ProtectedDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_unique_name(self):
        """
        **[Required]** Gets the db_unique_name of this ProtectedDatabase.
        The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.


        :return: The db_unique_name of this ProtectedDatabase.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this ProtectedDatabase.
        The dbUniqueName for the protected database in Recovery Service. You cannot change the unique name.


        :param db_unique_name: The db_unique_name of this ProtectedDatabase.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def vpc_user_name(self):
        """
        **[Required]** Gets the vpc_user_name of this ProtectedDatabase.
        The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.


        :return: The vpc_user_name of this ProtectedDatabase.
        :rtype: str
        """
        return self._vpc_user_name

    @vpc_user_name.setter
    def vpc_user_name(self, vpc_user_name):
        """
        Sets the vpc_user_name of this ProtectedDatabase.
        The virtual private catalog (VPC) user credentials that authenticates the protected database to access Recovery Service.


        :param vpc_user_name: The vpc_user_name of this ProtectedDatabase.
        :type: str
        """
        self._vpc_user_name = vpc_user_name

    @property
    def database_size(self):
        """
        **[Required]** Gets the database_size of this ProtectedDatabase.
        The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.

        Allowed values for this property are: "XS", "S", "M", "L", "XL", "XXL", "AUTO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_size of this ProtectedDatabase.
        :rtype: str
        """
        return self._database_size

    @database_size.setter
    def database_size(self, database_size):
        """
        Sets the database_size of this ProtectedDatabase.
        The size of the protected database. XS - Less than 5GB, S - 5GB to 50GB, M - 50GB to 500GB, L - 500GB to 1TB, XL - 1TB to 5TB, XXL - Greater than 5TB.


        :param database_size: The database_size of this ProtectedDatabase.
        :type: str
        """
        allowed_values = ["XS", "S", "M", "L", "XL", "XXL", "AUTO"]
        if not value_allowed_none_or_none_sentinel(database_size, allowed_values):
            database_size = 'UNKNOWN_ENUM_VALUE'
        self._database_size = database_size

    @property
    def protection_policy_id(self):
        """
        **[Required]** Gets the protection_policy_id of this ProtectedDatabase.
        The OCID of the protection policy associated with the protected database.


        :return: The protection_policy_id of this ProtectedDatabase.
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        """
        Sets the protection_policy_id of this ProtectedDatabase.
        The OCID of the protection policy associated with the protected database.


        :param protection_policy_id: The protection_policy_id of this ProtectedDatabase.
        :type: str
        """
        self._protection_policy_id = protection_policy_id

    @property
    def recovery_service_subnets(self):
        """
        **[Required]** Gets the recovery_service_subnets of this ProtectedDatabase.
        List of recovery service subnet resources associated with the protected database.


        :return: The recovery_service_subnets of this ProtectedDatabase.
        :rtype: list[oci.recovery.models.RecoveryServiceSubnetDetails]
        """
        return self._recovery_service_subnets

    @recovery_service_subnets.setter
    def recovery_service_subnets(self, recovery_service_subnets):
        """
        Sets the recovery_service_subnets of this ProtectedDatabase.
        List of recovery service subnet resources associated with the protected database.


        :param recovery_service_subnets: The recovery_service_subnets of this ProtectedDatabase.
        :type: list[oci.recovery.models.RecoveryServiceSubnetDetails]
        """
        self._recovery_service_subnets = recovery_service_subnets

    @property
    def database_id(self):
        """
        Gets the database_id of this ProtectedDatabase.
        The OCID of the protected database.


        :return: The database_id of this ProtectedDatabase.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this ProtectedDatabase.
        The OCID of the protected database.


        :param database_id: The database_id of this ProtectedDatabase.
        :type: str
        """
        self._database_id = database_id

    @property
    def database_size_in_gbs(self):
        """
        Gets the database_size_in_gbs of this ProtectedDatabase.
        The size of the database in GBs, in gigabytes.


        :return: The database_size_in_gbs of this ProtectedDatabase.
        :rtype: int
        """
        return self._database_size_in_gbs

    @database_size_in_gbs.setter
    def database_size_in_gbs(self, database_size_in_gbs):
        """
        Sets the database_size_in_gbs of this ProtectedDatabase.
        The size of the database in GBs, in gigabytes.


        :param database_size_in_gbs: The database_size_in_gbs of this ProtectedDatabase.
        :type: int
        """
        self._database_size_in_gbs = database_size_in_gbs

    @property
    def change_rate(self):
        """
        Gets the change_rate of this ProtectedDatabase.
        The percentage of data changes that exist in the database between successive incremental backups.


        :return: The change_rate of this ProtectedDatabase.
        :rtype: float
        """
        return self._change_rate

    @change_rate.setter
    def change_rate(self, change_rate):
        """
        Sets the change_rate of this ProtectedDatabase.
        The percentage of data changes that exist in the database between successive incremental backups.


        :param change_rate: The change_rate of this ProtectedDatabase.
        :type: float
        """
        self._change_rate = change_rate

    @property
    def compression_ratio(self):
        """
        Gets the compression_ratio of this ProtectedDatabase.
        The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.


        :return: The compression_ratio of this ProtectedDatabase.
        :rtype: float
        """
        return self._compression_ratio

    @compression_ratio.setter
    def compression_ratio(self, compression_ratio):
        """
        Sets the compression_ratio of this ProtectedDatabase.
        The compression ratio of the protected database. The compression ratio represents the ratio of compressed block size to expanded block size.


        :param compression_ratio: The compression_ratio of this ProtectedDatabase.
        :type: float
        """
        self._compression_ratio = compression_ratio

    @property
    def is_redo_logs_shipped(self):
        """
        Gets the is_redo_logs_shipped of this ProtectedDatabase.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional
        configuration is needed on client side.


        :return: The is_redo_logs_shipped of this ProtectedDatabase.
        :rtype: bool
        """
        return self._is_redo_logs_shipped

    @is_redo_logs_shipped.setter
    def is_redo_logs_shipped(self, is_redo_logs_shipped):
        """
        Sets the is_redo_logs_shipped of this ProtectedDatabase.
        The value TRUE indicates that the protected database is configured to use Real-time data protection, and redo-data is sent from the protected database to Recovery Service.
        Real-time data protection substantially reduces the window of potential data loss that exists between successive archived redo log backups. For this to be effective, additional
        configuration is needed on client side.


        :param is_redo_logs_shipped: The is_redo_logs_shipped of this ProtectedDatabase.
        :type: bool
        """
        self._is_redo_logs_shipped = is_redo_logs_shipped

    @property
    def time_created(self):
        """
        Gets the time_created of this ProtectedDatabase.
        An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'


        :return: The time_created of this ProtectedDatabase.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProtectedDatabase.
        An RFC3339 formatted datetime string that indicates the created time for a protected database. For example: '2020-05-22T21:10:29.600Z'


        :param time_created: The time_created of this ProtectedDatabase.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ProtectedDatabase.
        An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'


        :return: The time_updated of this ProtectedDatabase.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProtectedDatabase.
        An RFC3339 formatted datetime string that indicates the last updated time for a protected database. For example: '2020-05-22T21:10:29.600Z'


        :param time_updated: The time_updated of this ProtectedDatabase.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ProtectedDatabase.
        The current state of the Protected Database.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ProtectedDatabase.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProtectedDatabase.
        The current state of the Protected Database.


        :param lifecycle_state: The lifecycle_state of this ProtectedDatabase.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def health(self):
        """
        Gets the health of this ProtectedDatabase.
        Indicates the protection status of the database. Allowed values are:
         - HEALTHY
         - WARNING
         - ALERT

        A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The potential data loss exposure since the last backup is:
         - Less than 10 seconds, if Real-time data protection is enabled
         - Less than 70 minutes if Real-time data protection is disabled

        A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential data loss exposure since the last backup is:
         - Greater than 10 seconds, if Real-time data protection is enabled
         - Greater than 60 minutes, if if Real-time data protection is disabled

        An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.

        Allowed values for this property are: "PROTECTED", "WARNING", "ALERT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The health of this ProtectedDatabase.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Sets the health of this ProtectedDatabase.
        Indicates the protection status of the database. Allowed values are:
         - HEALTHY
         - WARNING
         - ALERT

        A 'HEALTHY' status indicates that Recovery Service can ensure database recovery to any point in time within the entire recovery window. The potential data loss exposure since the last backup is:
         - Less than 10 seconds, if Real-time data protection is enabled
         - Less than 70 minutes if Real-time data protection is disabled

        A 'WARNING' status indicates that Recovery Service can ensure database recovery within the current recovery window - 1 day. The potential data loss exposure since the last backup is:
         - Greater than 10 seconds, if Real-time data protection is enabled
         - Greater than 60 minutes, if if Real-time data protection is disabled

        An 'ALERT' status indicates that Recovery Service cannot recover the database within the current recovery window.


        :param health: The health of this ProtectedDatabase.
        :type: str
        """
        allowed_values = ["PROTECTED", "WARNING", "ALERT"]
        if not value_allowed_none_or_none_sentinel(health, allowed_values):
            health = 'UNKNOWN_ENUM_VALUE'
        self._health = health

    @property
    def is_read_only_resource(self):
        """
        Gets the is_read_only_resource of this ProtectedDatabase.
        Indicates whether the protected database is created by Recovery Service or created manually.
        Set to <b>TRUE</b> for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource.
        Set to <b>FALSE</b> for a user-defined protected database.


        :return: The is_read_only_resource of this ProtectedDatabase.
        :rtype: bool
        """
        return self._is_read_only_resource

    @is_read_only_resource.setter
    def is_read_only_resource(self, is_read_only_resource):
        """
        Sets the is_read_only_resource of this ProtectedDatabase.
        Indicates whether the protected database is created by Recovery Service or created manually.
        Set to <b>TRUE</b> for a service-defined protected database. When you enable the OCI-managed automatic backups option for a database and set Recovery Service as the backup destination, then Recovery Service creates the associated protected database resource.
        Set to <b>FALSE</b> for a user-defined protected database.


        :param is_read_only_resource: The is_read_only_resource of this ProtectedDatabase.
        :type: bool
        """
        self._is_read_only_resource = is_read_only_resource

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ProtectedDatabase.
        Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this ProtectedDatabase.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ProtectedDatabase.
        Detailed description about the current lifecycle state of the protected database. For example, it can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this ProtectedDatabase.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def health_details(self):
        """
        Gets the health_details of this ProtectedDatabase.
        A message describing the current health of the protected database.


        :return: The health_details of this ProtectedDatabase.
        :rtype: str
        """
        return self._health_details

    @health_details.setter
    def health_details(self, health_details):
        """
        Sets the health_details of this ProtectedDatabase.
        A message describing the current health of the protected database.


        :param health_details: The health_details of this ProtectedDatabase.
        :type: str
        """
        self._health_details = health_details

    @property
    def metrics(self):
        """
        Gets the metrics of this ProtectedDatabase.

        :return: The metrics of this ProtectedDatabase.
        :rtype: oci.recovery.models.Metrics
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this ProtectedDatabase.

        :param metrics: The metrics of this ProtectedDatabase.
        :type: oci.recovery.models.Metrics
        """
        self._metrics = metrics

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ProtectedDatabase.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this ProtectedDatabase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProtectedDatabase.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this ProtectedDatabase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ProtectedDatabase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ProtectedDatabase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProtectedDatabase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ProtectedDatabase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ProtectedDatabase.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ProtectedDatabase.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ProtectedDatabase.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ProtectedDatabase.
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
