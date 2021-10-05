# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdvisorReport(object):
    """
    Pre-Migration advisor report details.
    """

    #: A constant which can be used with the result property of a AdvisorReport.
    #: This constant has a value of "FATAL"
    RESULT_FATAL = "FATAL"

    #: A constant which can be used with the result property of a AdvisorReport.
    #: This constant has a value of "BLOCKER"
    RESULT_BLOCKER = "BLOCKER"

    #: A constant which can be used with the result property of a AdvisorReport.
    #: This constant has a value of "WARNING"
    RESULT_WARNING = "WARNING"

    #: A constant which can be used with the result property of a AdvisorReport.
    #: This constant has a value of "INFORMATIONAL"
    RESULT_INFORMATIONAL = "INFORMATIONAL"

    #: A constant which can be used with the result property of a AdvisorReport.
    #: This constant has a value of "PASS"
    RESULT_PASS = "PASS"

    def __init__(self, **kwargs):
        """
        Initializes a new AdvisorReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_location_details:
            The value to assign to the report_location_details property of this AdvisorReport.
        :type report_location_details: oci.database_migration.models.AdvisorReportLocationDetails

        :param result:
            The value to assign to the result property of this AdvisorReport.
            Allowed values for this property are: "FATAL", "BLOCKER", "WARNING", "INFORMATIONAL", "PASS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result: str

        :param number_of_fatal:
            The value to assign to the number_of_fatal property of this AdvisorReport.
        :type number_of_fatal: int

        :param number_of_fatal_blockers:
            The value to assign to the number_of_fatal_blockers property of this AdvisorReport.
        :type number_of_fatal_blockers: int

        :param number_of_warnings:
            The value to assign to the number_of_warnings property of this AdvisorReport.
        :type number_of_warnings: int

        :param number_of_informational_results:
            The value to assign to the number_of_informational_results property of this AdvisorReport.
        :type number_of_informational_results: int

        """
        self.swagger_types = {
            'report_location_details': 'AdvisorReportLocationDetails',
            'result': 'str',
            'number_of_fatal': 'int',
            'number_of_fatal_blockers': 'int',
            'number_of_warnings': 'int',
            'number_of_informational_results': 'int'
        }

        self.attribute_map = {
            'report_location_details': 'reportLocationDetails',
            'result': 'result',
            'number_of_fatal': 'numberOfFatal',
            'number_of_fatal_blockers': 'numberOfFatalBlockers',
            'number_of_warnings': 'numberOfWarnings',
            'number_of_informational_results': 'numberOfInformationalResults'
        }

        self._report_location_details = None
        self._result = None
        self._number_of_fatal = None
        self._number_of_fatal_blockers = None
        self._number_of_warnings = None
        self._number_of_informational_results = None

    @property
    def report_location_details(self):
        """
        Gets the report_location_details of this AdvisorReport.

        :return: The report_location_details of this AdvisorReport.
        :rtype: oci.database_migration.models.AdvisorReportLocationDetails
        """
        return self._report_location_details

    @report_location_details.setter
    def report_location_details(self, report_location_details):
        """
        Sets the report_location_details of this AdvisorReport.

        :param report_location_details: The report_location_details of this AdvisorReport.
        :type: oci.database_migration.models.AdvisorReportLocationDetails
        """
        self._report_location_details = report_location_details

    @property
    def result(self):
        """
        **[Required]** Gets the result of this AdvisorReport.
        Pre-Migration advisor result.

        Allowed values for this property are: "FATAL", "BLOCKER", "WARNING", "INFORMATIONAL", "PASS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result of this AdvisorReport.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this AdvisorReport.
        Pre-Migration advisor result.


        :param result: The result of this AdvisorReport.
        :type: str
        """
        allowed_values = ["FATAL", "BLOCKER", "WARNING", "INFORMATIONAL", "PASS"]
        if not value_allowed_none_or_none_sentinel(result, allowed_values):
            result = 'UNKNOWN_ENUM_VALUE'
        self._result = result

    @property
    def number_of_fatal(self):
        """
        **[Required]** Gets the number_of_fatal of this AdvisorReport.
        Number of Fatal results in the advisor report.


        :return: The number_of_fatal of this AdvisorReport.
        :rtype: int
        """
        return self._number_of_fatal

    @number_of_fatal.setter
    def number_of_fatal(self, number_of_fatal):
        """
        Sets the number_of_fatal of this AdvisorReport.
        Number of Fatal results in the advisor report.


        :param number_of_fatal: The number_of_fatal of this AdvisorReport.
        :type: int
        """
        self._number_of_fatal = number_of_fatal

    @property
    def number_of_fatal_blockers(self):
        """
        **[Required]** Gets the number_of_fatal_blockers of this AdvisorReport.
        Number of Fatal Blocker results in the advisor report.


        :return: The number_of_fatal_blockers of this AdvisorReport.
        :rtype: int
        """
        return self._number_of_fatal_blockers

    @number_of_fatal_blockers.setter
    def number_of_fatal_blockers(self, number_of_fatal_blockers):
        """
        Sets the number_of_fatal_blockers of this AdvisorReport.
        Number of Fatal Blocker results in the advisor report.


        :param number_of_fatal_blockers: The number_of_fatal_blockers of this AdvisorReport.
        :type: int
        """
        self._number_of_fatal_blockers = number_of_fatal_blockers

    @property
    def number_of_warnings(self):
        """
        **[Required]** Gets the number_of_warnings of this AdvisorReport.
        Number of Warning results in the advisor report.


        :return: The number_of_warnings of this AdvisorReport.
        :rtype: int
        """
        return self._number_of_warnings

    @number_of_warnings.setter
    def number_of_warnings(self, number_of_warnings):
        """
        Sets the number_of_warnings of this AdvisorReport.
        Number of Warning results in the advisor report.


        :param number_of_warnings: The number_of_warnings of this AdvisorReport.
        :type: int
        """
        self._number_of_warnings = number_of_warnings

    @property
    def number_of_informational_results(self):
        """
        **[Required]** Gets the number_of_informational_results of this AdvisorReport.
        Number of Informational results in the advisor report.


        :return: The number_of_informational_results of this AdvisorReport.
        :rtype: int
        """
        return self._number_of_informational_results

    @number_of_informational_results.setter
    def number_of_informational_results(self, number_of_informational_results):
        """
        Sets the number_of_informational_results of this AdvisorReport.
        Number of Informational results in the advisor report.


        :param number_of_informational_results: The number_of_informational_results of this AdvisorReport.
        :type: int
        """
        self._number_of_informational_results = number_of_informational_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
