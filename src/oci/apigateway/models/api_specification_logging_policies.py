# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationLoggingPolicies(object):
    """
    Policies controlling the pushing of logs to OCI Public Logging.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationLoggingPolicies object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_log:
            The value to assign to the access_log property of this ApiSpecificationLoggingPolicies.
        :type access_log: oci.apigateway.models.AccessLogPolicy

        :param execution_log:
            The value to assign to the execution_log property of this ApiSpecificationLoggingPolicies.
        :type execution_log: oci.apigateway.models.ExecutionLogPolicy

        """
        self.swagger_types = {
            'access_log': 'AccessLogPolicy',
            'execution_log': 'ExecutionLogPolicy'
        }
        self.attribute_map = {
            'access_log': 'accessLog',
            'execution_log': 'executionLog'
        }
        self._access_log = None
        self._execution_log = None

    @property
    def access_log(self):
        """
        Gets the access_log of this ApiSpecificationLoggingPolicies.

        :return: The access_log of this ApiSpecificationLoggingPolicies.
        :rtype: oci.apigateway.models.AccessLogPolicy
        """
        return self._access_log

    @access_log.setter
    def access_log(self, access_log):
        """
        Sets the access_log of this ApiSpecificationLoggingPolicies.

        :param access_log: The access_log of this ApiSpecificationLoggingPolicies.
        :type: oci.apigateway.models.AccessLogPolicy
        """
        self._access_log = access_log

    @property
    def execution_log(self):
        """
        Gets the execution_log of this ApiSpecificationLoggingPolicies.

        :return: The execution_log of this ApiSpecificationLoggingPolicies.
        :rtype: oci.apigateway.models.ExecutionLogPolicy
        """
        return self._execution_log

    @execution_log.setter
    def execution_log(self, execution_log):
        """
        Sets the execution_log of this ApiSpecificationLoggingPolicies.

        :param execution_log: The execution_log of this ApiSpecificationLoggingPolicies.
        :type: oci.apigateway.models.ExecutionLogPolicy
        """
        self._execution_log = execution_log

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
