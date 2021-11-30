# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryFindingCounts(object):
    """
    The finding counts data for the SQL Tuning Advisor summary report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryFindingCounts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recommended_sql_profile:
            The value to assign to the recommended_sql_profile property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type recommended_sql_profile: int

        :param implemented_sql_profile:
            The value to assign to the implemented_sql_profile property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type implemented_sql_profile: int

        :param index:
            The value to assign to the index property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type index: int

        :param restructure:
            The value to assign to the restructure property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type restructure: int

        :param statistics:
            The value to assign to the statistics property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type statistics: int

        :param alternate_plan:
            The value to assign to the alternate_plan property of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type alternate_plan: int

        """
        self.swagger_types = {
            'recommended_sql_profile': 'int',
            'implemented_sql_profile': 'int',
            'index': 'int',
            'restructure': 'int',
            'statistics': 'int',
            'alternate_plan': 'int'
        }

        self.attribute_map = {
            'recommended_sql_profile': 'recommendedSqlProfile',
            'implemented_sql_profile': 'implementedSqlProfile',
            'index': 'index',
            'restructure': 'restructure',
            'statistics': 'statistics',
            'alternate_plan': 'alternatePlan'
        }

        self._recommended_sql_profile = None
        self._implemented_sql_profile = None
        self._index = None
        self._restructure = None
        self._statistics = None
        self._alternate_plan = None

    @property
    def recommended_sql_profile(self):
        """
        **[Required]** Gets the recommended_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with recommended SQL profiles.


        :return: The recommended_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._recommended_sql_profile

    @recommended_sql_profile.setter
    def recommended_sql_profile(self, recommended_sql_profile):
        """
        Sets the recommended_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with recommended SQL profiles.


        :param recommended_sql_profile: The recommended_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._recommended_sql_profile = recommended_sql_profile

    @property
    def implemented_sql_profile(self):
        """
        **[Required]** Gets the implemented_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with implemented SQL profiles.


        :return: The implemented_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._implemented_sql_profile

    @implemented_sql_profile.setter
    def implemented_sql_profile(self, implemented_sql_profile):
        """
        Sets the implemented_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with implemented SQL profiles.


        :param implemented_sql_profile: The implemented_sql_profile of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._implemented_sql_profile = implemented_sql_profile

    @property
    def index(self):
        """
        **[Required]** Gets the index of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with index recommendations.


        :return: The index of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with index recommendations.


        :param index: The index of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._index = index

    @property
    def restructure(self):
        """
        **[Required]** Gets the restructure of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with restructure SQL recommendations.


        :return: The restructure of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._restructure

    @restructure.setter
    def restructure(self, restructure):
        """
        Sets the restructure of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with restructure SQL recommendations.


        :param restructure: The restructure of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._restructure = restructure

    @property
    def statistics(self):
        """
        **[Required]** Gets the statistics of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with stale/missing optimizer statistics recommendations.


        :return: The statistics of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with stale/missing optimizer statistics recommendations.


        :param statistics: The statistics of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._statistics = statistics

    @property
    def alternate_plan(self):
        """
        **[Required]** Gets the alternate_plan of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with alternative plan recommendations.


        :return: The alternate_plan of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :rtype: int
        """
        return self._alternate_plan

    @alternate_plan.setter
    def alternate_plan(self, alternate_plan):
        """
        Sets the alternate_plan of this SqlTuningAdvisorTaskSummaryFindingCounts.
        The count of distinct SQL statements with alternative plan recommendations.


        :param alternate_plan: The alternate_plan of this SqlTuningAdvisorTaskSummaryFindingCounts.
        :type: int
        """
        self._alternate_plan = alternate_plan

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
