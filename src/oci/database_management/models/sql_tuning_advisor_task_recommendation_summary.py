# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskRecommendationSummary(object):
    """
    A recommendation for a given object in a SQL Tuning Task.
    """

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "STATISTICS"
    RECOMMENDATION_TYPE_STATISTICS = "STATISTICS"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "INDEX"
    RECOMMENDATION_TYPE_INDEX = "INDEX"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "SQL_PROFILE"
    RECOMMENDATION_TYPE_SQL_PROFILE = "SQL_PROFILE"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "RESTRUCTURE_SQL"
    RECOMMENDATION_TYPE_RESTRUCTURE_SQL = "RESTRUCTURE_SQL"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "ALTERNATIVE_PLANS"
    RECOMMENDATION_TYPE_ALTERNATIVE_PLANS = "ALTERNATIVE_PLANS"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "ERROR"
    RECOMMENDATION_TYPE_ERROR = "ERROR"

    #: A constant which can be used with the recommendation_type property of a SqlTuningAdvisorTaskRecommendationSummary.
    #: This constant has a value of "MISCELLANEOUS"
    RECOMMENDATION_TYPE_MISCELLANEOUS = "MISCELLANEOUS"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskRecommendationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_advisor_task_id:
            The value to assign to the sql_tuning_advisor_task_id property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type sql_tuning_advisor_task_id: int

        :param sql_tuning_advisor_task_object_id:
            The value to assign to the sql_tuning_advisor_task_object_id property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type sql_tuning_advisor_task_object_id: int

        :param recommendation_key:
            The value to assign to the recommendation_key property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type recommendation_key: int

        :param recommendation_type:
            The value to assign to the recommendation_type property of this SqlTuningAdvisorTaskRecommendationSummary.
            Allowed values for this property are: "STATISTICS", "INDEX", "SQL_PROFILE", "RESTRUCTURE_SQL", "ALTERNATIVE_PLANS", "ERROR", "MISCELLANEOUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recommendation_type: str

        :param finding:
            The value to assign to the finding property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type finding: str

        :param recommendation:
            The value to assign to the recommendation property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type recommendation: str

        :param rationale:
            The value to assign to the rationale property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type rationale: str

        :param benefit:
            The value to assign to the benefit property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type benefit: float

        :param implement_action_sql:
            The value to assign to the implement_action_sql property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type implement_action_sql: str

        :param is_parallel_execution:
            The value to assign to the is_parallel_execution property of this SqlTuningAdvisorTaskRecommendationSummary.
        :type is_parallel_execution: bool

        """
        self.swagger_types = {
            'sql_tuning_advisor_task_id': 'int',
            'sql_tuning_advisor_task_object_id': 'int',
            'recommendation_key': 'int',
            'recommendation_type': 'str',
            'finding': 'str',
            'recommendation': 'str',
            'rationale': 'str',
            'benefit': 'float',
            'implement_action_sql': 'str',
            'is_parallel_execution': 'bool'
        }
        self.attribute_map = {
            'sql_tuning_advisor_task_id': 'sqlTuningAdvisorTaskId',
            'sql_tuning_advisor_task_object_id': 'sqlTuningAdvisorTaskObjectId',
            'recommendation_key': 'recommendationKey',
            'recommendation_type': 'recommendationType',
            'finding': 'finding',
            'recommendation': 'recommendation',
            'rationale': 'rationale',
            'benefit': 'benefit',
            'implement_action_sql': 'implementActionSql',
            'is_parallel_execution': 'isParallelExecution'
        }
        self._sql_tuning_advisor_task_id = None
        self._sql_tuning_advisor_task_object_id = None
        self._recommendation_key = None
        self._recommendation_type = None
        self._finding = None
        self._recommendation = None
        self._rationale = None
        self._benefit = None
        self._implement_action_sql = None
        self._is_parallel_execution = None

    @property
    def sql_tuning_advisor_task_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskRecommendationSummary.
        The unique identifier of the task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_id

    @sql_tuning_advisor_task_id.setter
    def sql_tuning_advisor_task_id(self, sql_tuning_advisor_task_id):
        """
        Sets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskRecommendationSummary.
        The unique identifier of the task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_id: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_id = sql_tuning_advisor_task_id

    @property
    def sql_tuning_advisor_task_object_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskRecommendationSummary.
        The key of the object to which these recommendations apply. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_object_id

    @sql_tuning_advisor_task_object_id.setter
    def sql_tuning_advisor_task_object_id(self, sql_tuning_advisor_task_object_id):
        """
        Sets the sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskRecommendationSummary.
        The key of the object to which these recommendations apply. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_object_id: The sql_tuning_advisor_task_object_id of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_object_id = sql_tuning_advisor_task_object_id

    @property
    def recommendation_key(self):
        """
        **[Required]** Gets the recommendation_key of this SqlTuningAdvisorTaskRecommendationSummary.
        The unique identifier of the recommendation in the scope of the task.


        :return: The recommendation_key of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: int
        """
        return self._recommendation_key

    @recommendation_key.setter
    def recommendation_key(self, recommendation_key):
        """
        Sets the recommendation_key of this SqlTuningAdvisorTaskRecommendationSummary.
        The unique identifier of the recommendation in the scope of the task.


        :param recommendation_key: The recommendation_key of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: int
        """
        self._recommendation_key = recommendation_key

    @property
    def recommendation_type(self):
        """
        **[Required]** Gets the recommendation_type of this SqlTuningAdvisorTaskRecommendationSummary.
        Type of recommendation.

        Allowed values for this property are: "STATISTICS", "INDEX", "SQL_PROFILE", "RESTRUCTURE_SQL", "ALTERNATIVE_PLANS", "ERROR", "MISCELLANEOUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recommendation_type of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: str
        """
        return self._recommendation_type

    @recommendation_type.setter
    def recommendation_type(self, recommendation_type):
        """
        Sets the recommendation_type of this SqlTuningAdvisorTaskRecommendationSummary.
        Type of recommendation.


        :param recommendation_type: The recommendation_type of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: str
        """
        allowed_values = ["STATISTICS", "INDEX", "SQL_PROFILE", "RESTRUCTURE_SQL", "ALTERNATIVE_PLANS", "ERROR", "MISCELLANEOUS"]
        if not value_allowed_none_or_none_sentinel(recommendation_type, allowed_values):
            recommendation_type = 'UNKNOWN_ENUM_VALUE'
        self._recommendation_type = recommendation_type

    @property
    def finding(self):
        """
        Gets the finding of this SqlTuningAdvisorTaskRecommendationSummary.
        Summary of the issue found in the SQL statement.


        :return: The finding of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: str
        """
        return self._finding

    @finding.setter
    def finding(self, finding):
        """
        Sets the finding of this SqlTuningAdvisorTaskRecommendationSummary.
        Summary of the issue found in the SQL statement.


        :param finding: The finding of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: str
        """
        self._finding = finding

    @property
    def recommendation(self):
        """
        Gets the recommendation of this SqlTuningAdvisorTaskRecommendationSummary.
        The recommendation for a specific finding.


        :return: The recommendation of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: str
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """
        Sets the recommendation of this SqlTuningAdvisorTaskRecommendationSummary.
        The recommendation for a specific finding.


        :param recommendation: The recommendation of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: str
        """
        self._recommendation = recommendation

    @property
    def rationale(self):
        """
        Gets the rationale of this SqlTuningAdvisorTaskRecommendationSummary.
        Describes the reasoning behind the recommendation and how it relates to the finding.


        :return: The rationale of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: str
        """
        return self._rationale

    @rationale.setter
    def rationale(self, rationale):
        """
        Sets the rationale of this SqlTuningAdvisorTaskRecommendationSummary.
        Describes the reasoning behind the recommendation and how it relates to the finding.


        :param rationale: The rationale of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: str
        """
        self._rationale = rationale

    @property
    def benefit(self):
        """
        Gets the benefit of this SqlTuningAdvisorTaskRecommendationSummary.
        The percentage benefit of this implementation.


        :return: The benefit of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: float
        """
        return self._benefit

    @benefit.setter
    def benefit(self, benefit):
        """
        Sets the benefit of this SqlTuningAdvisorTaskRecommendationSummary.
        The percentage benefit of this implementation.


        :param benefit: The benefit of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: float
        """
        self._benefit = benefit

    @property
    def implement_action_sql(self):
        """
        Gets the implement_action_sql of this SqlTuningAdvisorTaskRecommendationSummary.
        Action sql to be implemented based on the recommendation result.


        :return: The implement_action_sql of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: str
        """
        return self._implement_action_sql

    @implement_action_sql.setter
    def implement_action_sql(self, implement_action_sql):
        """
        Sets the implement_action_sql of this SqlTuningAdvisorTaskRecommendationSummary.
        Action sql to be implemented based on the recommendation result.


        :param implement_action_sql: The implement_action_sql of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: str
        """
        self._implement_action_sql = implement_action_sql

    @property
    def is_parallel_execution(self):
        """
        Gets the is_parallel_execution of this SqlTuningAdvisorTaskRecommendationSummary.
        Indicates whether a SQL Profile recommendation uses parallel execution.


        :return: The is_parallel_execution of this SqlTuningAdvisorTaskRecommendationSummary.
        :rtype: bool
        """
        return self._is_parallel_execution

    @is_parallel_execution.setter
    def is_parallel_execution(self, is_parallel_execution):
        """
        Sets the is_parallel_execution of this SqlTuningAdvisorTaskRecommendationSummary.
        Indicates whether a SQL Profile recommendation uses parallel execution.


        :param is_parallel_execution: The is_parallel_execution of this SqlTuningAdvisorTaskRecommendationSummary.
        :type: bool
        """
        self._is_parallel_execution = is_parallel_execution

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
