# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry, circuit_breaker  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import opsi_type_mapping
missing = Sentinel("Missing")


class OperationsInsightsClient(object):
    """
    Use the Operations Insights API to perform data extraction operations to obtain database
    resource utilization, performance statistics, and reference information. For more information,
    see [About Oracle Cloud Infrastructure Operations Insights](https://docs.cloud.oracle.com/en-us/iaas/operations-insights/doc/operations-insights.html).
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

        :param obj circuit_breaker_strategy: (optional)
            A circuit breaker strategy to apply to all calls made by this service client (i.e. at the client level).
            This client uses :py:data:`~oci.circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY` as default if no circuit breaker strategy is provided.
            The specifics of circuit breaker strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__.

        :param function circuit_breaker_callback: (optional)
            Callback function to receive any exceptions triggerred by the circuit breaker.

        :param allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this client should allow control characters in the response object. By default, the client will not
            allow control characters to be in the response object.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'base_path': '/20200630',
            'service_endpoint_template': 'https://operationsinsights.{region}.oci.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'circuit_breaker_strategy': kwargs.get('circuit_breaker_strategy', circuit_breaker.GLOBAL_CIRCUIT_BREAKER_STRATEGY)
        }
        if 'timeout' in kwargs:
            base_client_init_kwargs['timeout'] = kwargs.get('timeout')
        if base_client_init_kwargs.get('circuit_breaker_strategy') is None:
            base_client_init_kwargs['circuit_breaker_strategy'] = circuit_breaker.DEFAULT_CIRCUIT_BREAKER_STRATEGY
        if 'allow_control_chars' in kwargs:
            base_client_init_kwargs['allow_control_chars'] = kwargs.get('allow_control_chars')
        self.base_client = BaseClient("operations_insights", config, signer, opsi_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')
        self.circuit_breaker_callback = kwargs.get('circuit_breaker_callback')

    def add_exadata_insight_members(self, add_exadata_insight_members_details, exadata_insight_id, **kwargs):
        """
        Add new members (e.g. databases and hosts) to an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started.


        :param oci.opsi.models.AddExadataInsightMembersDetails add_exadata_insight_members_details: (required)
            Details for the members (e.g. databases and hosts) of an Exadata system to be added in Operations Insights.

        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/add_exadata_insight_members.py.html>`__ to see an example of how to use add_exadata_insight_members API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}/actions/addMembers"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_exadata_insight_members got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_exadata_insight_members_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=add_exadata_insight_members_details)

    def change_database_insight_compartment(self, database_insight_id, change_database_insight_compartment_details, **kwargs):
        """
        Moves a DatabaseInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param oci.opsi.models.ChangeDatabaseInsightCompartmentDetails change_database_insight_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_database_insight_compartment.py.html>`__ to see an example of how to use change_database_insight_compartment API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_database_insight_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_insight_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_database_insight_compartment_details)

    def change_enterprise_manager_bridge_compartment(self, enterprise_manager_bridge_id, change_enterprise_manager_bridge_compartment_details, **kwargs):
        """
        Moves a EnterpriseManagerBridge resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param oci.opsi.models.ChangeEnterpriseManagerBridgeCompartmentDetails change_enterprise_manager_bridge_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_enterprise_manager_bridge_compartment.py.html>`__ to see an example of how to use change_enterprise_manager_bridge_compartment API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_enterprise_manager_bridge_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_enterprise_manager_bridge_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_enterprise_manager_bridge_compartment_details)

    def change_exadata_insight_compartment(self, exadata_insight_id, change_exadata_insight_compartment_details, **kwargs):
        """
        Moves an Exadata insight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.


        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param oci.opsi.models.ChangeExadataInsightCompartmentDetails change_exadata_insight_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_exadata_insight_compartment.py.html>`__ to see an example of how to use change_exadata_insight_compartment API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_exadata_insight_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_exadata_insight_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_exadata_insight_compartment_details)

    def change_host_insight_compartment(self, host_insight_id, change_host_insight_compartment_details, **kwargs):
        """
        Moves a HostInsight resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param oci.opsi.models.ChangeHostInsightCompartmentDetails change_host_insight_compartment_details: (required)
            The information to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/change_host_insight_compartment.py.html>`__ to see an example of how to use change_host_insight_compartment API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_host_insight_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_host_insight_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_host_insight_compartment_details)

    def create_awr_hub(self, create_awr_hub_details, **kwargs):
        """
        Create a AWR hub resource for the tenant in Operations Insights.
        This resource will be created in root compartment.


        :param oci.opsi.models.CreateAwrHubDetails create_awr_hub_details: (required)
            Details using which an AWR hub resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.AwrHub`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_awr_hub.py.html>`__ to see an example of how to use create_awr_hub API.
        """
        resource_path = "/awrHubs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_awr_hub got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_awr_hub_details,
                response_type="AwrHub")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_awr_hub_details,
                response_type="AwrHub")

    def create_database_insight(self, create_database_insight_details, **kwargs):
        """
        Create a Database Insight resource for a database in Operations Insights. The database will be enabled in Operations Insights. Database metric collection and analysis will be started.


        :param oci.opsi.models.CreateDatabaseInsightDetails create_database_insight_details: (required)
            Details for the database for which a Database Insight resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_database_insight.py.html>`__ to see an example of how to use create_database_insight API.
        """
        resource_path = "/databaseInsights"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_database_insight_details,
                response_type="DatabaseInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_database_insight_details,
                response_type="DatabaseInsight")

    def create_enterprise_manager_bridge(self, create_enterprise_manager_bridge_details, **kwargs):
        """
        Create a Enterprise Manager bridge in Operations Insights.


        :param oci.opsi.models.CreateEnterpriseManagerBridgeDetails create_enterprise_manager_bridge_details: (required)
            Details for the Enterprise Manager bridge to be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridge`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_enterprise_manager_bridge.py.html>`__ to see an example of how to use create_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_enterprise_manager_bridge_details,
                response_type="EnterpriseManagerBridge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_enterprise_manager_bridge_details,
                response_type="EnterpriseManagerBridge")

    def create_exadata_insight(self, create_exadata_insight_details, **kwargs):
        """
        Create an Exadata insight resource for an Exadata system in Operations Insights. The Exadata system will be enabled in Operations Insights. Exadata-related metric collection and analysis will be started.


        :param oci.opsi.models.CreateExadataInsightDetails create_exadata_insight_details: (required)
            Details for the Exadata system for which an Exadata insight resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ExadataInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_exadata_insight.py.html>`__ to see an example of how to use create_exadata_insight API.
        """
        resource_path = "/exadataInsights"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_exadata_insight_details,
                response_type="ExadataInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_exadata_insight_details,
                response_type="ExadataInsight")

    def create_host_insight(self, create_host_insight_details, **kwargs):
        """
        Create a Host Insight resource for a host in Operations Insights. The host will be enabled in Operations Insights. Host metric collection and analysis will be started.


        :param oci.opsi.models.CreateHostInsightDetails create_host_insight_details: (required)
            Details for the host for which a Host Insight resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_host_insight.py.html>`__ to see an example of how to use create_host_insight API.
        """
        resource_path = "/hostInsights"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_host_insight_details,
                response_type="HostInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_host_insight_details,
                response_type="HostInsight")

    def create_operations_insights_warehouse(self, create_operations_insights_warehouse_details, **kwargs):
        """
        Create a Operations Insights Warehouse resource for the tenant in Operations Insights. New ADW will be provisioned for this tenant.
        There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.


        :param oci.opsi.models.CreateOperationsInsightsWarehouseDetails create_operations_insights_warehouse_details: (required)
            Details using which an Operations Insights Warehouse resource will be created in Operations Insights.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouse`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_operations_insights_warehouse.py.html>`__ to see an example of how to use create_operations_insights_warehouse API.
        """
        resource_path = "/operationsInsightsWarehouses"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_operations_insights_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_operations_insights_warehouse_details,
                response_type="OperationsInsightsWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_operations_insights_warehouse_details,
                response_type="OperationsInsightsWarehouse")

    def create_operations_insights_warehouse_user(self, create_operations_insights_warehouse_user_details, **kwargs):
        """
        Create a Operations Insights Warehouse user resource for the tenant in Operations Insights.
        This resource will be created in root compartment.


        :param oci.opsi.models.CreateOperationsInsightsWarehouseUserDetails create_operations_insights_warehouse_user_details: (required)
            Parameter using which an Operations Insights Warehouse user resource will be created.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouseUser`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/create_operations_insights_warehouse_user.py.html>`__ to see an example of how to use create_operations_insights_warehouse_user API.
        """
        resource_path = "/operationsInsightsWarehouseUsers"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_retry_token",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_operations_insights_warehouse_user got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_operations_insights_warehouse_user_details,
                response_type="OperationsInsightsWarehouseUser")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_operations_insights_warehouse_user_details,
                response_type="OperationsInsightsWarehouseUser")

    def delete_awr_hub(self, awr_hub_id, **kwargs):
        """
        Deletes an AWR hub.


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_awr_hub.py.html>`__ to see an example of how to use delete_awr_hub API.
        """
        resource_path = "/awrHubs/{awrHubId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_awr_hub got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_database_insight(self, database_insight_id, **kwargs):
        """
        Deletes a database insight. The database insight will be deleted and cannot be enabled again.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_database_insight.py.html>`__ to see an example of how to use delete_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_enterprise_manager_bridge(self, enterprise_manager_bridge_id, **kwargs):
        """
        Deletes an Operations Insights Enterprise Manager bridge. If any database insight is still referencing this bridge, the operation will fail.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_enterprise_manager_bridge.py.html>`__ to see an example of how to use delete_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_exadata_insight(self, exadata_insight_id, **kwargs):
        """
        Deletes an Exadata insight. The Exadata insight will be deleted and cannot be enabled again.


        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_exadata_insight.py.html>`__ to see an example of how to use delete_exadata_insight API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_host_insight(self, host_insight_id, **kwargs):
        """
        Deletes a host insight. The host insight will be deleted and cannot be enabled again.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_host_insight.py.html>`__ to see an example of how to use delete_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_operations_insights_warehouse(self, operations_insights_warehouse_id, **kwargs):
        """
        Deletes an Operations Insights Warehouse. There is only expected to be 1 warehouse per tenant.
        The warehouse is expected to be in the root compartment.
        User must delete AWR Hub resource for this warehouse before calling this operation.
        User must delete the warehouse users before calling this operation.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_operations_insights_warehouse.py.html>`__ to see an example of how to use delete_operations_insights_warehouse API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_operations_insights_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_operations_insights_warehouse_user(self, operations_insights_warehouse_user_id, **kwargs):
        """
        Deletes an Operations Insights Warehouse User.


        :param str operations_insights_warehouse_user_id: (required)
            Unique Operations Insights Warehouse User identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/delete_operations_insights_warehouse_user.py.html>`__ to see an example of how to use delete_operations_insights_warehouse_user API.
        """
        resource_path = "/operationsInsightsWarehouseUsers/{operationsInsightsWarehouseUserId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_operations_insights_warehouse_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseUserId": operations_insights_warehouse_user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def disable_database_insight(self, database_insight_id, **kwargs):
        """
        Disables a database in Operations Insights. Database metric collection and analysis will be stopped.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/disable_database_insight.py.html>`__ to see an example of how to use disable_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/disable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "disable_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def disable_exadata_insight(self, exadata_insight_id, **kwargs):
        """
        Disables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be stopped.


        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/disable_exadata_insight.py.html>`__ to see an example of how to use disable_exadata_insight API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}/actions/disable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "disable_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def disable_host_insight(self, host_insight_id, **kwargs):
        """
        Disables a host in Operations Insights. Host metric collection and analysis will be stopped.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/disable_host_insight.py.html>`__ to see an example of how to use disable_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/disable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "disable_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def download_operations_insights_warehouse_wallet(self, operations_insights_warehouse_id, download_operations_insights_warehouse_wallet_details, **kwargs):
        """
        Download the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param oci.opsi.models.DownloadOperationsInsightsWarehouseWalletDetails download_operations_insights_warehouse_wallet_details: (required)
            The information to be updated.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/download_operations_insights_warehouse_wallet.py.html>`__ to see an example of how to use download_operations_insights_warehouse_wallet API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}/actions/downloadWarehouseWallet"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "download_operations_insights_warehouse_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/octet-stream",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=download_operations_insights_warehouse_wallet_details,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=download_operations_insights_warehouse_wallet_details,
                response_type="stream")

    def enable_database_insight(self, enable_database_insight_details, database_insight_id, **kwargs):
        """
        Enables a database in Operations Insights. Database metric collection and analysis will be started.


        :param oci.opsi.models.EnableDatabaseInsightDetails enable_database_insight_details: (required)
            Details for the database to be enabled in Operations Insights.

        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/enable_database_insight.py.html>`__ to see an example of how to use enable_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}/actions/enable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "enable_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_database_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_database_insight_details)

    def enable_exadata_insight(self, enable_exadata_insight_details, exadata_insight_id, **kwargs):
        """
        Enables an Exadata system in Operations Insights. Exadata-related metric collection and analysis will be started.


        :param oci.opsi.models.EnableExadataInsightDetails enable_exadata_insight_details: (required)
            Details for the Exadata system to be enabled in Operations Insights.

        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/enable_exadata_insight.py.html>`__ to see an example of how to use enable_exadata_insight API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}/actions/enable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "enable_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_exadata_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_exadata_insight_details)

    def enable_host_insight(self, enable_host_insight_details, host_insight_id, **kwargs):
        """
        Enables a host in Operations Insights. Host metric collection and analysis will be started.


        :param oci.opsi.models.EnableHostInsightDetails enable_host_insight_details: (required)
            Details for the host to be enabled in Operations Insights.

        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/enable_host_insight.py.html>`__ to see an example of how to use enable_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}/actions/enable"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "enable_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_host_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=enable_host_insight_details)

    def get_awr_hub(self, awr_hub_id, **kwargs):
        """
        Gets details of an AWR hub.


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.AwrHub`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_awr_hub.py.html>`__ to see an example of how to use get_awr_hub API.
        """
        resource_path = "/awrHubs/{awrHubId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_awr_hub got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AwrHub")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AwrHub")

    def get_awr_report(self, awr_hub_id, awr_source_database_identifier, **kwargs):
        """
        Gets the AWR report for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not be greater than 7 days.
        Either beginSnapshotIdentifierGreaterThanOrEqualTo & endSnapshotIdentifierLessThanOrEqualTo params Or timeGreaterThanOrEqualTo & timeLessThanOrEqualTo params are required.


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param str awr_source_database_identifier: (required)
            AWR source database identifier.

        :param str report_format: (optional)
            The format of the AWR report. Default report format is HTML.

            Allowed values are: "HTML", "TEXT"

        :param str instance_number: (optional)
            The optional single value query parameter to filter by database instance number.

        :param int begin_snapshot_identifier_greater_than_or_equal_to: (optional)
            The optional greater than or equal to filter on the snapshot ID.

        :param int end_snapshot_identifier_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the snapshot Identifier.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.AwrReport`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_awr_report.py.html>`__ to see an example of how to use get_awr_report API.
        """
        resource_path = "/awrHubs/{awrHubId}/awrReport"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "report_format",
            "instance_number",
            "begin_snapshot_identifier_greater_than_or_equal_to",
            "end_snapshot_identifier_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_awr_report got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'report_format' in kwargs:
            report_format_allowed_values = ["HTML", "TEXT"]
            if kwargs['report_format'] not in report_format_allowed_values:
                raise ValueError(
                    "Invalid value for `report_format`, must be one of {0}".format(report_format_allowed_values)
                )

        query_params = {
            "awrSourceDatabaseIdentifier": awr_source_database_identifier,
            "reportFormat": kwargs.get("report_format", missing),
            "instanceNumber": kwargs.get("instance_number", missing),
            "beginSnapshotIdentifierGreaterThanOrEqualTo": kwargs.get("begin_snapshot_identifier_greater_than_or_equal_to", missing),
            "endSnapshotIdentifierLessThanOrEqualTo": kwargs.get("end_snapshot_identifier_less_than_or_equal_to", missing),
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrReport")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrReport")

    def get_database_insight(self, database_insight_id, **kwargs):
        """
        Gets details of a database insight.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_database_insight.py.html>`__ to see an example of how to use get_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DatabaseInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DatabaseInsight")

    def get_enterprise_manager_bridge(self, enterprise_manager_bridge_id, **kwargs):
        """
        Gets details of an Operations Insights Enterprise Manager bridge.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridge`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_enterprise_manager_bridge.py.html>`__ to see an example of how to use get_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridge")

    def get_exadata_insight(self, exadata_insight_id, **kwargs):
        """
        Gets details of an Exadata insight.


        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ExadataInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_exadata_insight.py.html>`__ to see an example of how to use get_exadata_insight API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ExadataInsight")

    def get_host_insight(self, host_insight_id, **kwargs):
        """
        Gets details of a host insight.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsight`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_host_insight.py.html>`__ to see an example of how to use get_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HostInsight")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HostInsight")

    def get_operations_insights_warehouse(self, operations_insights_warehouse_id, **kwargs):
        """
        Gets details of an Operations Insights Warehouse.
        There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouse`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_operations_insights_warehouse.py.html>`__ to see an example of how to use get_operations_insights_warehouse API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_operations_insights_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouse")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouse")

    def get_operations_insights_warehouse_user(self, operations_insights_warehouse_user_id, **kwargs):
        """
        Gets details of an Operations Insights Warehouse User.


        :param str operations_insights_warehouse_user_id: (required)
            Unique Operations Insights Warehouse User identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouseUser`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_operations_insights_warehouse_user.py.html>`__ to see an example of how to use get_operations_insights_warehouse_user API.
        """
        resource_path = "/operationsInsightsWarehouseUsers/{operationsInsightsWarehouseUserId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_operations_insights_warehouse_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseUserId": operations_insights_warehouse_user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseUser")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseUser")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Gets the status of the work request with the given ID.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/get_work_request.py.html>`__ to see an example of how to use get_work_request API.
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")

    def ingest_database_configuration(self, ingest_database_configuration_details, **kwargs):
        """
        This is a generic ingest endpoint for all database configuration metrics.


        :param oci.opsi.models.IngestDatabaseConfigurationDetails ingest_database_configuration_details: (required)
            Payload for one or more database configuration metrics for a particular database.

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestDatabaseConfigurationResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_database_configuration.py.html>`__ to see an example of how to use ingest_database_configuration API.
        """
        resource_path = "/databaseInsights/actions/ingestDatabaseConfiguration"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_database_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_database_configuration_details,
                response_type="IngestDatabaseConfigurationResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_database_configuration_details,
                response_type="IngestDatabaseConfigurationResponseDetails")

    def ingest_host_configuration(self, id, ingest_host_configuration_details, **kwargs):
        """
        This is a generic ingest endpoint for all the host configuration metrics


        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestHostConfigurationDetails ingest_host_configuration_details: (required)
            Payload for one or more host configuration metrics for a particular host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestHostConfigurationResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_host_configuration.py.html>`__ to see an example of how to use ingest_host_configuration API.
        """
        resource_path = "/hostInsights/actions/ingestHostConfiguration"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_host_configuration got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "id": id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_configuration_details,
                response_type="IngestHostConfigurationResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_configuration_details,
                response_type="IngestHostConfigurationResponseDetails")

    def ingest_host_metrics(self, id, ingest_host_metrics_details, **kwargs):
        """
        This is a generic ingest endpoint for all the host performance metrics


        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.IngestHostMetricsDetails ingest_host_metrics_details: (required)
            Payload for one or more host performance metrics for a particular host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestHostMetricsResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_host_metrics.py.html>`__ to see an example of how to use ingest_host_metrics API.
        """
        resource_path = "/hostInsights/actions/ingestHostMetrics"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_host_metrics got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "id": id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_metrics_details,
                response_type="IngestHostMetricsResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_host_metrics_details,
                response_type="IngestHostMetricsResponseDetails")

    def ingest_sql_bucket(self, ingest_sql_bucket_details, **kwargs):
        """
        The sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
        Either databaseId or id must be specified.


        :param oci.opsi.models.IngestSqlBucketDetails ingest_sql_bucket_details: (required)
            Collection of SQL bucket objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlBucketResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_bucket.py.html>`__ to see an example of how to use ingest_sql_bucket API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlBucket"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_bucket got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_bucket_details,
                response_type="IngestSqlBucketResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_bucket_details,
                response_type="IngestSqlBucketResponseDetails")

    def ingest_sql_plan_lines(self, ingest_sql_plan_lines_details, **kwargs):
        """
        The SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
        Either databaseId or id must be specified.


        :param oci.opsi.models.IngestSqlPlanLinesDetails ingest_sql_plan_lines_details: (required)
            Collection of SQL plan line objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlPlanLinesResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_plan_lines.py.html>`__ to see an example of how to use ingest_sql_plan_lines API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlPlanLines"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_plan_lines got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_plan_lines_details,
                response_type="IngestSqlPlanLinesResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_plan_lines_details,
                response_type="IngestSqlPlanLinesResponseDetails")

    def ingest_sql_stats(self, ingest_sql_stats_details, **kwargs):
        """
        The SQL Stats endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
        Either databaseId or id must be specified.


        :param oci.opsi.models.IngestSqlStatsDetails ingest_sql_stats_details: (required)
            Collection of SQL stats objects for a particular database.

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlStatsResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_stats.py.html>`__ to see an example of how to use ingest_sql_stats API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlStatsMetric"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_stats got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_stats_details,
                response_type="IngestSqlStatsResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_stats_details,
                response_type="IngestSqlStatsResponseDetails")

    def ingest_sql_text(self, ingest_sql_text_details, **kwargs):
        """
        The SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
        Either databaseId or id must be specified.
        Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior to ingestion.


        :param oci.opsi.models.IngestSqlTextDetails ingest_sql_text_details: (required)
            Collection of SQL text objects for a particular database.

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request that can be retried in case of a timeout or
            server error without risk of executing the same action again. Retry tokens expire after 24
            hours.

            *Note:* Retry tokens can be invalidated before the 24 hour time limit due to conflicting
            operations, such as a resource being deleted or purged from the system.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.IngestSqlTextResponseDetails`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/ingest_sql_text.py.html>`__ to see an example of how to use ingest_sql_text API.
        """
        resource_path = "/databaseInsights/actions/ingestSqlText"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "database_id",
            "id",
            "opc_request_id",
            "if_match",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "ingest_sql_text got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_text_details,
                response_type="IngestSqlTextResponseDetails")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=ingest_sql_text_details,
                response_type="IngestSqlTextResponseDetails")

    def list_awr_hubs(self, operations_insights_warehouse_id, **kwargs):
        """
        Gets a list of AWR hubs. Either compartmentId or id must be specified. All these resources are expected to be in root compartment.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name.

        :param str id: (optional)
            Unique Awr Hub identifier

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.AwrHubSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_awr_hubs.py.html>`__ to see an example of how to use list_awr_hubs API.
        """
        resource_path = "/awrHubs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "display_name",
            "id",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_awr_hubs got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "operationsInsightsWarehouseId": operations_insights_warehouse_id,
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrHubSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrHubSummaryCollection")

    def list_awr_snapshots(self, awr_hub_id, awr_source_database_identifier, **kwargs):
        """
        Lists AWR snapshots for the specified source database in the AWR hub. The difference between the timeGreaterThanOrEqualTo and timeLessThanOrEqualTo should not exceed an elapsed range of 1 day.
        The timeGreaterThanOrEqualTo & timeLessThanOrEqualTo params are optional. If these params are not provided, by default last 1 day snapshots will be returned.


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param str awr_source_database_identifier: (required)
            AWR source database identifier.

        :param datetime time_greater_than_or_equal_to: (optional)
            The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

        :param datetime time_less_than_or_equal_to: (optional)
            The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example 2020-12-03T19:00:53Z

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The option to sort the AWR snapshot summary data. Default sort is by timeBegin.

            Allowed values are: "timeBegin", "snapshotId"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.AwrSnapshotCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_awr_snapshots.py.html>`__ to see an example of how to use list_awr_snapshots API.
        """
        resource_path = "/awrHubs/{awrHubId}/awrSnapshots"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_awr_snapshots got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeBegin", "snapshotId"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "awrSourceDatabaseIdentifier": awr_source_database_identifier,
            "timeGreaterThanOrEqualTo": kwargs.get("time_greater_than_or_equal_to", missing),
            "timeLessThanOrEqualTo": kwargs.get("time_less_than_or_equal_to", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrSnapshotCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="AwrSnapshotCollection")

    def list_database_configurations(self, **kwargs):
        """
        Gets a list of database insight configurations based on the query parameters specified. Either compartmentId or databaseInsightId query parameter must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of database insight configurations in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Database configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "databaseName", "databaseDisplayName", "databaseType"

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseConfigurationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_database_configurations.py.html>`__ to see an example of how to use list_database_configurations API.
        """
        resource_path = "/databaseInsights/databaseConfigurations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "database_id",
            "exadata_insight_id",
            "cdb_name",
            "database_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "host_name",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_database_configurations got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["databaseName", "databaseDisplayName", "databaseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseConfigurationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseConfigurationCollection")

    def list_database_insights(self, **kwargs):
        """
        Gets a list of database insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of database insights in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] status: (optional)
            Resource Status

            Allowed values are: "DISABLED", "ENABLED", "TERMINATED"

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] fields: (optional)
            Specifies the fields to return in a database summary response. By default all fields are returned if omitted.

            Allowed values are: "compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Database insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "databaseName", "databaseDisplayName", "databaseType"

        :param str exadata_insight_id: (optional)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.DatabaseInsightsCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_database_insights.py.html>`__ to see an example of how to use list_database_insights API.
        """
        resource_path = "/databaseInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "status",
            "lifecycle_state",
            "database_type",
            "database_id",
            "fields",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "exadata_insight_id",
            "compartment_id_in_subtree",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_database_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'fields' in kwargs:
            fields_allowed_values = ["compartmentId", "databaseName", "databaseDisplayName", "databaseType", "databaseVersion", "databaseHostNames", "freeformTags", "definedTags"]
            for fields_item in kwargs['fields']:
                if fields_item not in fields_allowed_values:
                    raise ValueError(
                        "Invalid value for `fields`, must be one of {0}".format(fields_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["databaseName", "databaseDisplayName", "databaseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "fields": self.base_client.generate_collection_format_param(kwargs.get("fields", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "exadataInsightId": kwargs.get("exadata_insight_id", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseInsightsCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="DatabaseInsightsCollection")

    def list_enterprise_manager_bridges(self, **kwargs):
        """
        Gets a list of Operations Insights Enterprise Manager bridges. Either compartmentId or id must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of bridges in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name.

        :param str id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "displayName"

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.EnterpriseManagerBridgeCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_enterprise_manager_bridges.py.html>`__ to see an example of how to use list_enterprise_manager_bridges API.
        """
        resource_path = "/enterpriseManagerBridges"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "display_name",
            "id",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "compartment_id_in_subtree",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_enterprise_manager_bridges got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridgeCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="EnterpriseManagerBridgeCollection")

    def list_exadata_configurations(self, **kwargs):
        """
        Gets a list of exadata insight configurations. Either compartmentId or exadataInsightsId query parameter must be specified.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Exadata configuration list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "exadataName", "exadataDisplayName", "exadataType"

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ExadataConfigurationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_exadata_configurations.py.html>`__ to see an example of how to use list_exadata_configurations API.
        """
        resource_path = "/exadataInsights/exadataConfigurations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "exadata_insight_id",
            "exadata_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_exadata_configurations got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["exadataName", "exadataDisplayName", "exadataType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataConfigurationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataConfigurationCollection")

    def list_exadata_insights(self, **kwargs):
        """
        Gets a list of Exadata insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of Exadata insights in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] id: (optional)
            Optional list of Exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] status: (optional)
            Resource Status

            Allowed values are: "DISABLED", "ENABLED", "TERMINATED"

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Exadata insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified. Default order for timeCreated is descending. Default order for exadataName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "exadataName"

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ExadataInsightSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_exadata_insights.py.html>`__ to see an example of how to use list_exadata_insights API.
        """
        resource_path = "/exadataInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "status",
            "lifecycle_state",
            "exadata_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "compartment_id_in_subtree",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_exadata_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "exadataName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataInsightSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataInsightSummaryCollection")

    def list_host_configurations(self, **kwargs):
        """
        Gets a list of host insight configurations based on the query parameters specified. Either compartmentId or hostInsightId query parameter must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of host insight configurations in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Host configuration list sort options.

            Allowed values are: "hostName", "platformType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostConfigurationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_host_configurations.py.html>`__ to see an example of how to use list_host_configurations API.
        """
        resource_path = "/hostInsights/hostConfigurations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "enterprise_manager_bridge_id",
            "id",
            "exadata_insight_id",
            "platform_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_host_configurations got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["hostName", "platformType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostConfigurationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostConfigurationCollection")

    def list_host_insights(self, **kwargs):
        """
        Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.
        When both compartmentId and compartmentIdInSubtree are specified, a list of host insights in that compartment and in all sub-compartments will be returned.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] status: (optional)
            Resource Status

            Allowed values are: "DISABLED", "ENABLED", "TERMINATED"

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"

        :param list[str] host_type: (optional)
            Filter by one or more host types.
            Possible value is EXTERNAL-HOST.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.

            Allowed values are: "hostName", "hostType"

        :param str enterprise_manager_bridge_id: (optional)
            Unique Enterprise Manager bridge identifier

        :param str exadata_insight_id: (optional)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostInsightSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_host_insights.py.html>`__ to see an example of how to use list_host_insights API.
        """
        resource_path = "/hostInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "id",
            "status",
            "lifecycle_state",
            "host_type",
            "platform_type",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "enterprise_manager_bridge_id",
            "exadata_insight_id",
            "compartment_id_in_subtree",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_host_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
            for status_item in kwargs['status']:
                if status_item not in status_allowed_values:
                    raise ValueError(
                        "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                    )

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["hostName", "hostType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "status": self.base_client.generate_collection_format_param(kwargs.get("status", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "hostType": self.base_client.generate_collection_format_param(kwargs.get("host_type", missing), 'multi'),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "enterpriseManagerBridgeId": kwargs.get("enterprise_manager_bridge_id", missing),
            "exadataInsightId": kwargs.get("exadata_insight_id", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostInsightSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostInsightSummaryCollection")

    def list_hosted_entities(self, compartment_id, id, **kwargs):
        """
        Get a list of hosted entities details.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (required)
            Required `OCID`__ of the host insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param str exadata_insight_id: (optional)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Hosted entity list sort options.

            Allowed values are: "entityName", "entityType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.HostedEntityCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_hosted_entities.py.html>`__ to see an example of how to use list_hosted_entities API.
        """
        resource_path = "/hostInsights/hostedEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "exadata_insight_id",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_hosted_entities got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["entityName", "entityType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": id,
            "exadataInsightId": kwargs.get("exadata_insight_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostedEntityCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="HostedEntityCollection")

    def list_importable_agent_entities(self, compartment_id, **kwargs):
        """
        Gets a list of agent entities available to add a new hostInsight.  An agent entity is \"available\"
        and will be shown if all the following conditions are true:
           1.  The agent OCID is not already being used for an existing hostInsight.
           2.  The agent availabilityStatus = 'ACTIVE'
           3.  The agent lifecycleState = 'ACTIVE'


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Hosted entity list sort options.

            Allowed values are: "entityName", "entityType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ImportableAgentEntitySummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_importable_agent_entities.py.html>`__ to see an example of how to use list_importable_agent_entities API.
        """
        resource_path = "/importableAgentEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_importable_agent_entities got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["entityName", "entityType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ImportableAgentEntitySummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ImportableAgentEntitySummaryCollection")

    def list_importable_enterprise_manager_entities(self, enterprise_manager_bridge_id, **kwargs):
        """
        Gets a list of importable entities for an Operations Insights Enterprise Manager bridge that have not been imported before.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param list[str] enterprise_manager_entity_type: (optional)
            Filter by one or more Enterprise Manager entity types. Currently, the supported types are \"oracle_pdb\", \"oracle_database\", \"host\", \"oracle_dbmachine\", \"oracle_exa_cloud_service\", and \"oracle_oci_exadata_cloud_service\". If this parameter is not specified, targets of all supported entity types are returned by default.

        :param str enterprise_manager_identifier: (optional)
            Used in combination with enterpriseManagerParentEntityIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular Enterprise Manager parent entity.

        :param str enterprise_manager_parent_entity_identifier: (optional)
            Used in combination with enterpriseManagerIdentifier to return the members of a particular Enterprise Manager parent entity. Both enterpriseManagerIdentifier and enterpriseManagerParentEntityIdentifier must be specified to identify a particular  Enterprise Manager parent entity.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ImportableEnterpriseManagerEntityCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_importable_enterprise_manager_entities.py.html>`__ to see an example of how to use list_importable_enterprise_manager_entities API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}/importableEnterpriseManagerEntities"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "limit",
            "page",
            "enterprise_manager_entity_type",
            "enterprise_manager_identifier",
            "enterprise_manager_parent_entity_identifier",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_importable_enterprise_manager_entities got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "enterpriseManagerEntityType": self.base_client.generate_collection_format_param(kwargs.get("enterprise_manager_entity_type", missing), 'multi'),
            "enterpriseManagerIdentifier": kwargs.get("enterprise_manager_identifier", missing),
            "enterpriseManagerParentEntityIdentifier": kwargs.get("enterprise_manager_parent_entity_identifier", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ImportableEnterpriseManagerEntityCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="ImportableEnterpriseManagerEntityCollection")

    def list_operations_insights_warehouse_users(self, operations_insights_warehouse_id, **kwargs):
        """
        Gets a list of Operations Insights Warehouse users. Either compartmentId or id must be specified. All these resources are expected to be in root compartment.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name.

        :param str id: (optional)
            Unique Operations Insights Warehouse User identifier

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouseUserSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_operations_insights_warehouse_users.py.html>`__ to see an example of how to use list_operations_insights_warehouse_users API.
        """
        resource_path = "/operationsInsightsWarehouseUsers"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "display_name",
            "id",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_operations_insights_warehouse_users got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "operationsInsightsWarehouseId": operations_insights_warehouse_id,
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseUserSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseUserSummaryCollection")

    def list_operations_insights_warehouses(self, **kwargs):
        """
        Gets a list of Operations Insights warehouses. Either compartmentId or id must be specified.
        There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.


        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str display_name: (optional)
            A filter to return only resources that match the entire display name.

        :param str id: (optional)
            Unique Operations Insights Warehouse identifier

        :param list[str] lifecycle_state: (optional)
            Lifecycle states

            Allowed values are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.

            Allowed values are: "timeCreated", "displayName"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.OperationsInsightsWarehouseSummaryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_operations_insights_warehouses.py.html>`__ to see an example of how to use list_operations_insights_warehouses API.
        """
        resource_path = "/operationsInsightsWarehouses"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "display_name",
            "id",
            "lifecycle_state",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_operations_insights_warehouses got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeCreated", "displayName"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "displayName": kwargs.get("display_name", missing),
            "id": kwargs.get("id", missing),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseSummaryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="OperationsInsightsWarehouseSummaryCollection")

    def list_sql_plans(self, compartment_id, sql_identifier, plan_hash, **kwargs):
        """
        Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single plan.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param oci.opsi.models.list[int] plan_hash: (required)
            Unique plan hash for a SQL Plan of a particular SQL Statement.
            Example: `9820154385`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_plans.py.html>`__ to see an example of how to use list_sql_plans API.
        """
        resource_path = "/databaseInsights/sqlPlans"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_plans got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "planHash": self.base_client.generate_collection_format_param(plan_hash, 'multi'),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanCollection")

    def list_sql_searches(self, compartment_id, sql_identifier, **kwargs):
        """
        Search SQL by SQL Identifier across databases in a compartment and in all sub-compartments if specified.
        And get the SQL Text and the details of the databases executing the SQL for a given time period.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlSearchCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_searches.py.html>`__ to see an example of how to use list_sql_searches API.
        """
        resource_path = "/databaseInsights/sqlSearches"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_searches got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlSearchCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlSearchCollection")

    def list_sql_texts(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the full SQL Text for a SQL in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param oci.opsi.models.list[str] sql_identifier: (required)
            One or more unique SQL_IDs for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the assosicated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlTextCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_sql_texts.py.html>`__ to see an example of how to use list_sql_texts API.
        """
        resource_path = "/databaseInsights/sqlTexts"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_sql_texts got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "sqlIdentifier": self.base_client.generate_collection_format_param(sql_identifier, 'multi'),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlTextCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlTextCollection")

    def list_work_request_errors(self, work_request_id, **kwargs):
        """
        Return a (paginated) list of errors for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

            Allowed values are: "timeAccepted"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestErrorCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_request_errors.py.html>`__ to see an example of how to use list_work_request_errors API.
        """
        resource_path = "/workRequests/{workRequestId}/errors"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_request_errors got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeAccepted"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestErrorCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestErrorCollection")

    def list_work_request_logs(self, work_request_id, **kwargs):
        """
        Return a (paginated) list of logs for a given work request.


        :param str work_request_id: (required)
            The ID of the asynchronous request.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

            Allowed values are: "timeAccepted"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestLogEntryCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_request_logs.py.html>`__ to see an example of how to use list_work_request_logs API.
        """
        resource_path = "/workRequests/{workRequestId}/logs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_request_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeAccepted"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestLogEntryCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestLogEntryCollection")

    def list_work_requests(self, **kwargs):
        """
        Lists the work requests in a compartment. Either compartmentId or id must be specified. Only one of id, resourceId or relatedResourceId can be specified optionally.


        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            The ID of the asynchronous work request.

        :param str status: (optional)
            A filter to return only resources their lifecycleState matches the given OperationStatus.

            Allowed values are: "ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"

        :param str resource_id: (optional)
            The ID of the resource affected by the work request.

        :param str related_resource_id: (optional)
            The ID of the related resource for the resource affected by the work request, e.g. the related Exadata Insight OCID of the Database Insight work request

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.

            Allowed values are: "timeAccepted"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.WorkRequestCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/list_work_requests.py.html>`__ to see an example of how to use list_work_requests API.
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "page",
            "limit",
            "compartment_id",
            "id",
            "status",
            "resource_id",
            "related_resource_id",
            "sort_order",
            "sort_by"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        if 'status' in kwargs:
            status_allowed_values = ["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
            if kwargs['status'] not in status_allowed_values:
                raise ValueError(
                    "Invalid value for `status`, must be one of {0}".format(status_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["timeAccepted"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "compartmentId": kwargs.get("compartment_id", missing),
            "id": kwargs.get("id", missing),
            "status": kwargs.get("status", missing),
            "resourceId": kwargs.get("resource_id", missing),
            "relatedResourceId": kwargs.get("related_resource_id", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="WorkRequestCollection")

    def rotate_operations_insights_warehouse_wallet(self, operations_insights_warehouse_id, **kwargs):
        """
        Rotate the ADW wallet for Operations Insights Warehouse using which the Hub data is exposed.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/rotate_operations_insights_warehouse_wallet.py.html>`__ to see an example of how to use rotate_operations_insights_warehouse_wallet API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}/actions/rotateWarehouseWallet"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "rotate_operations_insights_warehouse_wallet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def summarize_awr_sources_summaries(self, awr_hub_id, **kwargs):
        """
        Gets a list of summary of AWR Sources.


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str name: (optional)
            Name for an Awr source database

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_by: (optional)
            The order in which Awr sources summary records are listed

            Allowed values are: "snapshotsUploaded", "name"

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeAwrSourcesSummariesCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_awr_sources_summaries.py.html>`__ to see an example of how to use summarize_awr_sources_summaries API.
        """
        resource_path = "/awrHubs/{awrHubId}/awrSourcesSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "name",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_awr_sources_summaries got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["snapshotsUploaded", "name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "name": kwargs.get("name", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeAwrSourcesSummariesCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeAwrSourcesSummariesCollection")

    def summarize_database_insight_resource_capacity_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity, baseCapacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp , capacity or baseCapacity

            Allowed values are: "endTimestamp", "capacity", "baseCapacity"

        :param str tablespace_name: (optional)
            Tablespace name for a database

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_capacity_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_capacity_trend API.
        """
        resource_path = "/databaseInsights/resourceCapacityTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "utilization_level",
            "page",
            "sort_order",
            "sort_by",
            "tablespace_name",
            "host_name",
            "is_database_instance_level_metrics",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "capacity", "baseCapacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "tablespaceName": kwargs.get("tablespace_name", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceCapacityTrendAggregationCollection")

    def summarize_database_insight_resource_forecast_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Get Forecast predictions for CPU and Storage resources since a time in the past.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str tablespace_name: (optional)
            Tablespace name for a database

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_forecast_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_forecast_trend API.
        """
        resource_path = "/databaseInsights/resourceForecastTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
            "page",
            "host_name",
            "tablespace_name",
            "is_database_instance_level_metrics",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "confidence": kwargs.get("confidence", missing),
            "page": kwargs.get("page", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "tablespaceName": kwargs.get("tablespace_name", missing),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceForecastTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceForecastTrendAggregation")

    def summarize_database_insight_resource_statistics(self, compartment_id, resource_metric, **kwargs):
        """
        Lists the Resource statistics (usage,capacity, usage change percent, utilization percent, base capacity, isAutoScalingEnabled)
        for each database filtered by utilization level in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str insight_by: (optional)
            Return data of a specific insight
            Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast,
            Low Utilization Forecast

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource statistics records are listed

            Allowed values are: "utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_statistics.py.html>`__ to see an example of how to use summarize_database_insight_resource_statistics API.
        """
        resource_path = "/databaseInsights/resourceStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "percentile",
            "insight_by",
            "forecast_days",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "host_name",
            "is_database_instance_level_metrics",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "usageChangePercent", "databaseName", "databaseType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "percentile": kwargs.get("percentile", missing),
            "insightBy": kwargs.get("insight_by", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceStatisticsAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceStatisticsAggregationCollection")

    def summarize_database_insight_resource_usage(self, compartment_id, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per database within the specified time period.
        For each database, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_usage.py.html>`__ to see an example of how to use summarize_database_insight_resource_usage API.
        """
        resource_path = "/databaseInsights/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "host_name",
            "is_database_instance_level_metrics",
            "page",
            "percentile",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "page": kwargs.get("page", missing),
            "percentile": kwargs.get("percentile", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageAggregation")

    def summarize_database_insight_resource_usage_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, usage, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp, usage or capacity

            Allowed values are: "endTimestamp", "usage", "capacity"

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_usage_trend.py.html>`__ to see an example of how to use summarize_database_insight_resource_usage_trend API.
        """
        resource_path = "/databaseInsights/resourceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "page",
            "sort_order",
            "sort_by",
            "host_name",
            "is_database_instance_level_metrics",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "usage", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUsageTrendAggregationCollection")

    def summarize_database_insight_resource_utilization_insight(self, compartment_id, resource_metric, **kwargs):
        """
        Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY and IO.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param bool is_database_instance_level_metrics: (optional)
            Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
            When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
            whole database which contains an instance on this host.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_resource_utilization_insight.py.html>`__ to see an example of how to use summarize_database_insight_resource_utilization_insight API.
        """
        resource_path = "/databaseInsights/resourceUtilizationInsight"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "forecast_days",
            "host_name",
            "is_database_instance_level_metrics",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "forecastDays": kwargs.get("forecast_days", missing),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "isDatabaseInstanceLevelMetrics": kwargs.get("is_database_instance_level_metrics", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUtilizationInsightAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightResourceUtilizationInsightAggregation")

    def summarize_database_insight_tablespace_usage_trend(self, compartment_id, **kwargs):
        """
        Returns response with usage time series data (endTimestamp, usage, capacity) with breakdown by tablespaceName for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_database_insight_tablespace_usage_trend.py.html>`__ to see an example of how to use summarize_database_insight_tablespace_usage_trend API.
        """
        resource_path = "/databaseInsights/tablespaceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_id",
            "id",
            "page",
            "limit",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_database_insight_tablespace_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeDatabaseInsightTablespaceUsageTrendAggregationCollection")

    def summarize_exadata_insight_resource_capacity_trend(self, resource_type, resource_metric, exadata_insight_id, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system for a resource metric.
        Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters.
        Top five resources are returned if total exceeds the limit specified.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId, cdbName and hostName query parameter applies to ResourceType DATABASE.
        Valid values for ResourceType HOST are CPU and MEMORY. HostName is returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT
        and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER.
        Valid values for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field.


        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str exadata_insight_id: (required)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_insight_id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] host_insight_id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] storage_server_name: (optional)
            Optional storage server name on an exadata system.

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource capacity trend records are listed

            Allowed values are: "id", "name"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceCapacityTrendCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_capacity_trend.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_capacity_trend API.
        """
        resource_path = "/exadataInsights/resourceCapacityTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_insight_id",
            "host_insight_id",
            "storage_server_name",
            "exadata_type",
            "cdb_name",
            "host_name",
            "page",
            "limit",
            "sort_order",
            "sort_by",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "name"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": exadata_insight_id,
            "databaseInsightId": self.base_client.generate_collection_format_param(kwargs.get("database_insight_id", missing), 'multi'),
            "hostInsightId": self.base_client.generate_collection_format_param(kwargs.get("host_insight_id", missing), 'multi'),
            "storageServerName": self.base_client.generate_collection_format_param(kwargs.get("storage_server_name", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceCapacityTrendCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceCapacityTrendCollection")

    def summarize_exadata_insight_resource_capacity_trend_aggregated(self, resource_type, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity) for the time period specified for an exadata system or fleet aggregation for a resource metric.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
        Valid values for ResourceType HOST are CPU and MEMORY.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.


        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp or capacity.

            Allowed values are: "endTimestamp", "capacity"

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceCapacityTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_capacity_trend_aggregated.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_capacity_trend_aggregated API.
        """
        resource_path = "/exadataInsights/resourceCapacityTrendAggregated"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "cdb_name",
            "host_name",
            "page",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_capacity_trend_aggregated got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceCapacityTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceCapacityTrendAggregation")

    def summarize_exadata_insight_resource_forecast_trend(self, resource_type, resource_metric, exadata_insight_id, **kwargs):
        """
        Get historical usage and forecast predictions for an exadata system with breakdown by databases, hosts or storage servers.
        Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters.
        Top five resources are returned if total exceeds the limit specified.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId , cdbName and hostName query parameter applies to ResourceType DATABASE.
        Valid values for ResourceType HOST are CPU and MEMORY. HostName s returned in name field. HostInsightId and hostName query parameter applies to ResourceType HOST.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and THROUGHPUT
        and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER.
        Valid value for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field.


        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str exadata_insight_id: (required)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] database_insight_id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] host_insight_id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] storage_server_name: (optional)
            Optional storage server name on an exadata system.

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_start_day: (optional)
            Number of days used for utilization forecast analysis.

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource Forecast trend records are listed

            Allowed values are: "id", "name", "daysToReachCapacity"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceForecastTrendCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_forecast_trend.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_forecast_trend API.
        """
        resource_path = "/exadataInsights/resourceForecastTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_insight_id",
            "host_insight_id",
            "storage_server_name",
            "exadata_type",
            "statistic",
            "forecast_start_day",
            "forecast_days",
            "forecast_model",
            "cdb_name",
            "host_name",
            "limit",
            "confidence",
            "sort_order",
            "sort_by",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "name", "daysToReachCapacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": exadata_insight_id,
            "databaseInsightId": self.base_client.generate_collection_format_param(kwargs.get("database_insight_id", missing), 'multi'),
            "hostInsightId": self.base_client.generate_collection_format_param(kwargs.get("host_insight_id", missing), 'multi'),
            "storageServerName": self.base_client.generate_collection_format_param(kwargs.get("storage_server_name", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastStartDay": kwargs.get("forecast_start_day", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "confidence": kwargs.get("confidence", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceForecastTrendCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceForecastTrendCollection")

    def summarize_exadata_insight_resource_forecast_trend_aggregated(self, resource_type, resource_metric, **kwargs):
        """
        Get aggregated historical usage and forecast predictions for resources. Either compartmentId or exadataInsightsId query parameter must be specified.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
        Valid values for ResourceType HOST are CPU and MEMORY.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.


        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str compartment_id: (optional)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_start_day: (optional)
            Number of days used for utilization forecast analysis.

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_forecast_trend_aggregated.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_forecast_trend_aggregated API.
        """
        resource_path = "/exadataInsights/resourceForecastTrendAggregated"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "compartment_id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "statistic",
            "forecast_start_day",
            "forecast_days",
            "forecast_model",
            "cdb_name",
            "host_name",
            "confidence",
            "page",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_forecast_trend_aggregated got unknown kwargs: {!r}".format(extra_kwargs))

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing),
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastStartDay": kwargs.get("forecast_start_day", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "confidence": kwargs.get("confidence", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceForecastTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceForecastTrendAggregation")

    def summarize_exadata_insight_resource_statistics(self, exadata_insight_id, resource_type, resource_metric, **kwargs):
        """
        Lists the Resource statistics (usage, capacity, usage change percent, utilization percent) for each resource based on resourceMetric filtered by utilization level.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
        Valid values for ResourceType HOST are CPU and MEMORY.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS, THROUGHPUT.
        Valid value for ResourceType DISKGROUP is STORAGE.


        :param str exadata_insight_id: (required)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource statistics records are listed

            Allowed values are: "utilizationPercent", "usage", "usageChangePercent"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_statistics.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_statistics API.
        """
        resource_path = "/exadataInsights/resourceStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_type",
            "cdb_name",
            "host_name",
            "percentile",
            "sort_order",
            "sort_by",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "usageChangePercent"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "exadataInsightId": exadata_insight_id,
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "percentile": kwargs.get("percentile", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceStatisticsAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceStatisticsAggregationCollection")

    def summarize_exadata_insight_resource_usage(self, compartment_id, resource_type, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per resource within the specified time period.
        For each resource, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
        Valid values for ResourceType HOST are CPU and MEMORY.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource usage summary records are listed

            Allowed values are: "utilizationPercent", "usage", "capacity", "usageChangePercent"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceUsageCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_usage.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_usage API.
        """
        resource_path = "/exadataInsights/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "cdb_name",
            "host_name",
            "sort_order",
            "sort_by",
            "page",
            "limit",
            "percentile",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "capacity", "usageChangePercent"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "percentile": kwargs.get("percentile", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUsageCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUsageCollection")

    def summarize_exadata_insight_resource_usage_aggregated(self, compartment_id, resource_type, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per database within the specified time period.
        For each database, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.
        Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
        Valid values for ResourceType HOST are CPU and MEMORY.
        Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_usage_aggregated.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_usage_aggregated API.
        """
        resource_path = "/exadataInsights/resourceUsageSummaryAggregated"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "cdb_name",
            "host_name",
            "page",
            "percentile",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_usage_aggregated got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "percentile": kwargs.get("percentile", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUsageAggregation")

    def summarize_exadata_insight_resource_utilization_insight(self, compartment_id, resource_type, resource_metric, **kwargs):
        """
        Gets current utilization, projected utilization and days to reach projectedUtilization for an exadata system over specified time period. Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Valid values for ResourceType HOST are CPU and MEMORY. Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_type: (required)
            Filter by resource.
            Supported values are HOST , STORAGE_SERVER and DATABASE

        :param str resource_metric: (required)
            Filter by resource metric.
            Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param int forecast_start_day: (optional)
            Number of days used for utilization forecast analysis.

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by hostname.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeExadataInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_insight_resource_utilization_insight.py.html>`__ to see an example of how to use summarize_exadata_insight_resource_utilization_insight API.
        """
        resource_path = "/exadataInsights/resourceUtilizationInsight"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "forecast_start_day",
            "forecast_days",
            "cdb_name",
            "host_name",
            "limit",
            "page",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "resourceType": resource_type,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "forecastStartDay": kwargs.get("forecast_start_day", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUtilizationInsightAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeExadataInsightResourceUtilizationInsightAggregation")

    def summarize_exadata_members(self, exadata_insight_id, **kwargs):
        """
        Lists the software and hardware inventory of the Exadata System.


        :param str exadata_insight_id: (required)
            `OCID`__ of exadata insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_type: (optional)
            Filter by one or more Exadata types.
            Possible value are DBMACHINE, EXACS, and EXACC.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which exadata member records are listed

            Allowed values are: "name", "displayName", "entityType"

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.ExadataMemberCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_exadata_members.py.html>`__ to see an example of how to use summarize_exadata_members API.
        """
        resource_path = "/exadataInsights/exadataMembers"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "exadata_type",
            "sort_order",
            "sort_by",
            "limit",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_exadata_members got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "displayName", "entityType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "exadataInsightId": exadata_insight_id,
            "exadataType": self.base_client.generate_collection_format_param(kwargs.get("exadata_type", missing), 'multi'),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataMemberCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="ExadataMemberCollection")

    def summarize_host_insight_resource_capacity_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp or capacity

            Allowed values are: "endTimestamp", "capacity"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceCapacityTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_capacity_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_capacity_trend API.
        """
        resource_path = "/hostInsights/resourceCapacityTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "utilization_level",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_capacity_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceCapacityTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceCapacityTrendAggregationCollection")

    def summarize_host_insight_resource_forecast_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Get Forecast predictions for CPU or memory resources since a time in the past.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str statistic: (optional)
            Choose the type of statistic metric data to be used for forecasting.

            Allowed values are: "AVG", "MAX"

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str forecast_model: (optional)
            Choose algorithm model for the forecasting.
            Possible values:
              - LINEAR: Uses linear regression algorithm for forecasting.
              - ML_AUTO: Automatically detects best algorithm to use for forecasting.
              - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm.

            Allowed values are: "LINEAR", "ML_AUTO", "ML_NO_AUTO"

        :param str utilization_level: (optional)
            Filter by utilization level by the following buckets:
              - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
              - LOW_UTILIZATION: DBs with utilization lower than 25.
              - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
              - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50.

            Allowed values are: "HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"

        :param int confidence: (optional)
            This parameter is used to change data's confidence level, this data is ingested by the
            forecast algorithm.
            Confidence is the probability of an interval to contain the expected population parameter.
            Manipulation of this value will lead to different results.
            If not set, default confidence value is 95%.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceForecastTrendAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_forecast_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_forecast_trend API.
        """
        resource_path = "/hostInsights/resourceForecastTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_forecast_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'statistic' in kwargs:
            statistic_allowed_values = ["AVG", "MAX"]
            if kwargs['statistic'] not in statistic_allowed_values:
                raise ValueError(
                    "Invalid value for `statistic`, must be one of {0}".format(statistic_allowed_values)
                )

        if 'forecast_model' in kwargs:
            forecast_model_allowed_values = ["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            if kwargs['forecast_model'] not in forecast_model_allowed_values:
                raise ValueError(
                    "Invalid value for `forecast_model`, must be one of {0}".format(forecast_model_allowed_values)
                )

        if 'utilization_level' in kwargs:
            utilization_level_allowed_values = ["HIGH_UTILIZATION", "LOW_UTILIZATION", "MEDIUM_HIGH_UTILIZATION", "MEDIUM_LOW_UTILIZATION"]
            if kwargs['utilization_level'] not in utilization_level_allowed_values:
                raise ValueError(
                    "Invalid value for `utilization_level`, must be one of {0}".format(utilization_level_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "statistic": kwargs.get("statistic", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "forecastModel": kwargs.get("forecast_model", missing),
            "utilizationLevel": kwargs.get("utilization_level", missing),
            "confidence": kwargs.get("confidence", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceForecastTrendAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceForecastTrendAggregation")

    def summarize_host_insight_resource_statistics(self, compartment_id, resource_metric, **kwargs):
        """
        Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered
        by utilization level in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str insight_by: (optional)
            Return data of a specific insight
            Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast,
            Low Utilization Forecast

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The order in which resource statistics records are listed.

            Allowed values are: "utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceStatisticsAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_statistics.py.html>`__ to see an example of how to use summarize_host_insight_resource_statistics API.
        """
        resource_path = "/hostInsights/resourceStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "percentile",
            "insight_by",
            "forecast_days",
            "limit",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["utilizationPercent", "usage", "usageChangePercent", "hostName", "platformType"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "percentile": kwargs.get("percentile", missing),
            "insightBy": kwargs.get("insight_by", missing),
            "forecastDays": kwargs.get("forecast_days", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceStatisticsAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceStatisticsAggregationCollection")

    def summarize_host_insight_resource_usage(self, compartment_id, resource_metric, **kwargs):
        """
        A cumulative distribution function is used to rank the usage data points per host within the specified time period.
        For each host, the minimum data point with a ranking > the percentile value is included in the summation.
        Linear regression functions are used to calculate the usage change percentage.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param int percentile: (optional)
            Percentile values of daily usage to be used for computing the aggregate resource usage.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_usage.py.html>`__ to see an example of how to use summarize_host_insight_resource_usage API.
        """
        resource_path = "/hostInsights/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "page",
            "percentile",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "percentile": kwargs.get("percentile", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageAggregation")

    def summarize_host_insight_resource_usage_trend(self, compartment_id, resource_metric, **kwargs):
        """
        Returns response with time series data (endTimestamp, usage, capacity) for the time period specified.
        The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            Sorts using end timestamp, usage or capacity

            Allowed values are: "endTimestamp", "usage", "capacity"

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUsageTrendAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_usage_trend.py.html>`__ to see an example of how to use summarize_host_insight_resource_usage_trend API.
        """
        resource_path = "/hostInsights/resourceUsageTrend"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "page",
            "sort_order",
            "sort_by",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_usage_trend got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["endTimestamp", "usage", "capacity"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageTrendAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUsageTrendAggregationCollection")

    def summarize_host_insight_resource_utilization_insight(self, compartment_id, resource_metric, **kwargs):
        """
        Gets resources with current utilization (high and low) and projected utilization (high and low) for a resource type over specified time period.
        If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str resource_metric: (required)
            Filter by host resource metric.
            Supported values are CPU, MEMORY, and LOGICAL_MEMORY.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param list[str] platform_type: (optional)
            Filter by one or more platform types.
            Supported platformType(s) for MACS-managed external host insight: [LINUX].
            Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

            Allowed values are: "LINUX", "SOLARIS", "SUNOS"

        :param list[str] id: (optional)
            Optional list of host insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param int forecast_days: (optional)
            Number of days used for utilization forecast analysis.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeHostInsightResourceUtilizationInsightAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_host_insight_resource_utilization_insight.py.html>`__ to see an example of how to use summarize_host_insight_resource_utilization_insight API.
        """
        resource_path = "/hostInsights/resourceUtilizationInsight"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "forecast_days",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_host_insight_resource_utilization_insight got unknown kwargs: {!r}".format(extra_kwargs))

        if 'platform_type' in kwargs:
            platform_type_allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
            for platform_type_item in kwargs['platform_type']:
                if platform_type_item not in platform_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `platform_type`, must be one of {0}".format(platform_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "resourceMetric": resource_metric,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "platformType": self.base_client.generate_collection_format_param(kwargs.get("platform_type", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "forecastDays": kwargs.get("forecast_days", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUtilizationInsightAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SummarizeHostInsightResourceUtilizationInsightAggregation")

    def summarize_operations_insights_warehouse_resource_usage(self, operations_insights_warehouse_id, **kwargs):
        """
        Gets the details of resources used by an Operations Insights Warehouse.
        There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SummarizeOperationsInsightsWarehouseResourceUsageAggregation`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_operations_insights_warehouse_resource_usage.py.html>`__ to see an example of how to use summarize_operations_insights_warehouse_resource_usage API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}/resourceUsageSummary"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_operations_insights_warehouse_resource_usage got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SummarizeOperationsInsightsWarehouseResourceUsageAggregation")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="SummarizeOperationsInsightsWarehouseResourceUsageAggregation")

    def summarize_sql_insights(self, compartment_id, **kwargs):
        """
        Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given
        time period across the given databases or database types in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param float database_time_pct_greater_than: (optional)
            Filter sqls by percentage of db time.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_insights.py.html>`__ to see an example of how to use summarize_sql_insights API.
        """
        resource_path = "/databaseInsights/sqlInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "host_name",
            "database_time_pct_greater_than",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_insights got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "databaseTimePctGreaterThan": kwargs.get("database_time_pct_greater_than", missing),
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlInsightAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlInsightAggregationCollection")

    def summarize_sql_plan_insights(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance insights on the execution plans for a given SQL for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlPlanInsightAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_plan_insights.py.html>`__ to see an example of how to use summarize_sql_plan_insights API.
        """
        resource_path = "/databaseInsights/sqlPlanInsights"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_plan_insights got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanInsightAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlPlanInsightAggregationCollection")

    def summarize_sql_response_time_distributions(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlResponseTimeDistributionAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_response_time_distributions.py.html>`__ to see an example of how to use summarize_sql_response_time_distributions API.
        """
        resource_path = "/databaseInsights/sqlResponseTimeDistributions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_response_time_distributions got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlResponseTimeDistributionAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlResponseTimeDistributionAggregationCollection")

    def summarize_sql_statistics(self, compartment_id, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given
        time period across the given databases or database types in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] database_type: (optional)
            Filter by one or more database type.
            Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.

            Allowed values are: "ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param float database_time_pct_greater_than: (optional)
            Filter sqls by percentage of db time.

        :param list[str] sql_identifier: (optional)
            One or more unique SQL_IDs for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param int limit: (optional)
            For list pagination. The maximum number of results per page, or items to
            return in a paginated \"List\" call.
            For important details about how pagination works, see
            `List Pagination`__.
            Example: `50`

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param str sort_order: (optional)
            The sort order to use, either ascending (`ASC`) or descending (`DESC`).

            Allowed values are: "ASC", "DESC"

        :param str sort_by: (optional)
            The field to use when sorting SQL statistics.
            Example: databaseTimeInSec

            Allowed values are: "databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"

        :param list[str] category: (optional)
            Filter sqls by one or more performance categories.

            Allowed values are: "DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "IMPROVING", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics.py.html>`__ to see an example of how to use summarize_sql_statistics API.
        """
        resource_path = "/databaseInsights/sqlStatistics"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "host_name",
            "database_time_pct_greater_than",
            "sql_identifier",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "limit",
            "page",
            "opc_request_id",
            "sort_order",
            "sort_by",
            "category",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics got unknown kwargs: {!r}".format(extra_kwargs))

        if 'database_type' in kwargs:
            database_type_allowed_values = ["ADW-S", "ATP-S", "ADW-D", "ATP-D", "EXTERNAL-PDB", "EXTERNAL-NONCDB"]
            for database_type_item in kwargs['database_type']:
                if database_type_item not in database_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `database_type`, must be one of {0}".format(database_type_allowed_values)
                    )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["databaseTimeInSec", "executionsPerHour", "executionsCount", "cpuTimeInSec", "ioTimeInSec", "inefficientWaitTimeInSec", "responseTimeInSec", "planCount", "variability", "averageActiveSessions", "databaseTimePct", "inefficiencyInPct", "changeInCpuTimeInPct", "changeInIoTimeInPct", "changeInInefficientWaitTimeInPct", "changeInResponseTimeInPct", "changeInAverageActiveSessionsInPct", "changeInExecutionsPerHourInPct", "changeInInefficiencyInPct"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'category' in kwargs:
            category_allowed_values = ["DEGRADING", "VARIANT", "INEFFICIENT", "CHANGING_PLANS", "IMPROVING", "DEGRADING_VARIANT", "DEGRADING_INEFFICIENT", "DEGRADING_CHANGING_PLANS", "DEGRADING_INCREASING_IO", "DEGRADING_INCREASING_CPU", "DEGRADING_INCREASING_INEFFICIENT_WAIT", "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO", "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU", "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "VARIANT_INEFFICIENT", "VARIANT_CHANGING_PLANS", "VARIANT_INCREASING_IO", "VARIANT_INCREASING_CPU", "VARIANT_INCREASING_INEFFICIENT_WAIT", "VARIANT_CHANGING_PLANS_AND_INCREASING_IO", "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU", "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS", "INEFFICIENT_INCREASING_INEFFICIENT_WAIT", "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"]
            for category_item in kwargs['category']:
                if category_item not in category_allowed_values:
                    raise ValueError(
                        "Invalid value for `category`, must be one of {0}".format(category_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "databaseType": self.base_client.generate_collection_format_param(kwargs.get("database_type", missing), 'multi'),
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "databaseTimePctGreaterThan": kwargs.get("database_time_pct_greater_than", missing),
            "sqlIdentifier": self.base_client.generate_collection_format_param(kwargs.get("sql_identifier", missing), 'multi'),
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "category": self.base_client.generate_collection_format_param(kwargs.get("category", missing), 'multi'),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticAggregationCollection")

    def summarize_sql_statistics_time_series(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a
        given time period in a compartment and in all sub-compartments if specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param list[str] database_id: (optional)
            Optional list of database `OCIDs`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] id: (optional)
            Optional list of database `OCIDs`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] exadata_insight_id: (optional)
            Optional list of exadata insight resource `OCIDs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param list[str] cdb_name: (optional)
            Filter by one or more cdb name.

        :param list[str] host_name: (optional)
            Filter by one or more hostname.

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param list[str] defined_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_equals: (optional)
            A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
            The key for each tag is \"{tagName}.{value}\".  All inputs are case-insensitive.
            Multiple values for the same tag name are interpreted as \"OR\".  Values for different tag names are interpreted as \"AND\".

        :param list[str] defined_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
            Each item in the list has the format \"{namespace}.{tagName}.true\" (for checking existence of a defined tag)
            or \"{namespace}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \"OR\".
            Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \"AND\".

        :param list[str] freeform_tag_exists: (optional)
            A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
            The key for each tag is \"{tagName}.true\".  All inputs are case-insensitive.
            Currently, only existence (\"true\" at the end) is supported. Absence (\"false\" at the end) is not supported.
            Multiple values for different tag names are interpreted as \"AND\".

        :param bool compartment_id_in_subtree: (optional)
            A flag to search all resources within a given compartment and all sub-compartments.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics_time_series.py.html>`__ to see an example of how to use summarize_sql_statistics_time_series API.
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeries"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "host_name",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics_time_series got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": self.base_client.generate_collection_format_param(kwargs.get("database_id", missing), 'multi'),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "exadataInsightId": self.base_client.generate_collection_format_param(kwargs.get("exadata_insight_id", missing), 'multi'),
            "cdbName": self.base_client.generate_collection_format_param(kwargs.get("cdb_name", missing), 'multi'),
            "hostName": self.base_client.generate_collection_format_param(kwargs.get("host_name", missing), 'multi'),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing),
            "definedTagEquals": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_equals", missing), 'multi'),
            "freeformTagEquals": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_equals", missing), 'multi'),
            "definedTagExists": self.base_client.generate_collection_format_param(kwargs.get("defined_tag_exists", missing), 'multi'),
            "freeformTagExists": self.base_client.generate_collection_format_param(kwargs.get("freeform_tag_exists", missing), 'multi'),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesAggregationCollection")

    def summarize_sql_statistics_time_series_by_plan(self, compartment_id, sql_identifier, **kwargs):
        """
        Query SQL Warehouse to get the performance statistics time series for a given SQL by execution plans for a given time period.
        Either databaseId or id must be specified.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str sql_identifier: (required)
            Unique SQL_ID for a SQL Statement.
            Example: `6rgjh9bjmy2s7`

        :param str database_id: (optional)
            Optional `OCID`__ of the associated DBaaS entity.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str id: (optional)
            `OCID`__ of the database insight resource.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str analysis_time_interval: (optional)
            Specify time period in ISO 8601 format with respect to current time.
            Default is last 30 days represented by P30D.
            If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
            Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to current time (P25M).

        :param datetime time_interval_start: (optional)
            Analysis start time in UTC in ISO 8601 format(inclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            The minimum allowed value is 2 years prior to the current day.
            timeIntervalStart and timeIntervalEnd parameters are used together.
            If analysisTimeInterval is specified, this parameter is ignored.

        :param datetime time_interval_end: (optional)
            Analysis end time in UTC in ISO 8601 format(exclusive).
            Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
            timeIntervalStart and timeIntervalEnd are used together.
            If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.

        :param str page: (optional)
            For list pagination. The value of the `opc-next-page` response header from
            the previous \"List\" call. For important details about how pagination works,
            see `List Pagination`__.

            __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm#nine

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.opsi.models.SqlStatisticsTimeSeriesByPlanAggregationCollection`
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/summarize_sql_statistics_time_series_by_plan.py.html>`__ to see an example of how to use summarize_sql_statistics_time_series_by_plan API.
        """
        resource_path = "/databaseInsights/sqlStatisticsTimeSeriesByPlan"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "database_id",
            "id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "summarize_sql_statistics_time_series_by_plan got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "databaseId": kwargs.get("database_id", missing),
            "id": kwargs.get("id", missing),
            "sqlIdentifier": sql_identifier,
            "analysisTimeInterval": kwargs.get("analysis_time_interval", missing),
            "timeIntervalStart": kwargs.get("time_interval_start", missing),
            "timeIntervalEnd": kwargs.get("time_interval_end", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesByPlanAggregationCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="SqlStatisticsTimeSeriesByPlanAggregationCollection")

    def update_awr_hub(self, awr_hub_id, update_awr_hub_details, **kwargs):
        """
        Updates the configuration of a hub .


        :param str awr_hub_id: (required)
            Unique Awr Hub identifier

        :param oci.opsi.models.UpdateAwrHubDetails update_awr_hub_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_awr_hub.py.html>`__ to see an example of how to use update_awr_hub API.
        """
        resource_path = "/awrHubs/{awrHubId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_awr_hub got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "awrHubId": awr_hub_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_awr_hub_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_awr_hub_details)

    def update_database_insight(self, database_insight_id, update_database_insight_details, **kwargs):
        """
        Updates configuration of a database insight.


        :param str database_insight_id: (required)
            Unique database insight identifier

        :param oci.opsi.models.UpdateDatabaseInsightDetails update_database_insight_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_database_insight.py.html>`__ to see an example of how to use update_database_insight API.
        """
        resource_path = "/databaseInsights/{databaseInsightId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_database_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "databaseInsightId": database_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_database_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_database_insight_details)

    def update_enterprise_manager_bridge(self, enterprise_manager_bridge_id, update_enterprise_manager_bridge_details, **kwargs):
        """
        Updates configuration of an Operations Insights Enterprise Manager bridge.


        :param str enterprise_manager_bridge_id: (required)
            Unique Enterprise Manager bridge identifier

        :param oci.opsi.models.UpdateEnterpriseManagerBridgeDetails update_enterprise_manager_bridge_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_enterprise_manager_bridge.py.html>`__ to see an example of how to use update_enterprise_manager_bridge API.
        """
        resource_path = "/enterpriseManagerBridges/{enterpriseManagerBridgeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_enterprise_manager_bridge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "enterpriseManagerBridgeId": enterprise_manager_bridge_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_enterprise_manager_bridge_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_enterprise_manager_bridge_details)

    def update_exadata_insight(self, exadata_insight_id, update_exadata_insight_details, **kwargs):
        """
        Updates configuration of an Exadata insight.


        :param str exadata_insight_id: (required)
            Unique Exadata insight identifier

        :param oci.opsi.models.UpdateExadataInsightDetails update_exadata_insight_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_exadata_insight.py.html>`__ to see an example of how to use update_exadata_insight API.
        """
        resource_path = "/exadataInsights/{exadataInsightId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_exadata_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "exadataInsightId": exadata_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_exadata_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_exadata_insight_details)

    def update_host_insight(self, host_insight_id, update_host_insight_details, **kwargs):
        """
        Updates configuration of a host insight.


        :param str host_insight_id: (required)
            Unique host insight identifier

        :param oci.opsi.models.UpdateHostInsightDetails update_host_insight_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_host_insight.py.html>`__ to see an example of how to use update_host_insight API.
        """
        resource_path = "/hostInsights/{hostInsightId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_host_insight got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "hostInsightId": host_insight_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_host_insight_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_host_insight_details)

    def update_operations_insights_warehouse(self, operations_insights_warehouse_id, update_operations_insights_warehouse_details, **kwargs):
        """
        Updates the configuration of an Operations Insights Warehouse.
        There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.


        :param str operations_insights_warehouse_id: (required)
            Unique Operations Insights Warehouse identifier

        :param oci.opsi.models.UpdateOperationsInsightsWarehouseDetails update_operations_insights_warehouse_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_operations_insights_warehouse.py.html>`__ to see an example of how to use update_operations_insights_warehouse API.
        """
        resource_path = "/operationsInsightsWarehouses/{operationsInsightsWarehouseId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_operations_insights_warehouse got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseId": operations_insights_warehouse_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_operations_insights_warehouse_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_operations_insights_warehouse_details)

    def update_operations_insights_warehouse_user(self, operations_insights_warehouse_user_id, update_operations_insights_warehouse_user_details, **kwargs):
        """
        Updates the configuration of an Operations Insights Warehouse User.


        :param str operations_insights_warehouse_user_id: (required)
            Unique Operations Insights Warehouse User identifier

        :param oci.opsi.models.UpdateOperationsInsightsWarehouseUserDetails update_operations_insights_warehouse_user_details: (required)
            The configuration to be updated.

        :param str if_match: (optional)
            Used for optimistic concurrency control. In the update or delete call for a resource, set the `if-match`
            parameter to the value of the etag from a previous get, create, or update response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request. If you need to contact
            Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. This operation will not retry by default, users can also use the convenient :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY` provided by the SDK to enable retries for it.
            The specifics of the default retry strategy are described `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :param bool allow_control_chars: (optional)
            allow_control_chars is a boolean to indicate whether or not this request should allow control characters in the response object.
            By default, the response will not allow control characters in strings

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`

        :example:
        Click `here <https://docs.cloud.oracle.com/en-us/iaas/tools/python-sdk-examples/latest/opsi/update_operations_insights_warehouse_user.py.html>`__ to see an example of how to use update_operations_insights_warehouse_user API.
        """
        resource_path = "/operationsInsightsWarehouseUsers/{operationsInsightsWarehouseUserId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "allow_control_chars",
            "retry_strategy",
            "if_match",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_operations_insights_warehouse_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "operationsInsightsWarehouseUserId": operations_insights_warehouse_user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.base_client.get_preferred_retry_strategy(
            operation_retry_strategy=kwargs.get('retry_strategy'),
            client_retry_strategy=self.retry_strategy
        )

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_client_retries_header(header_params)
                retry_strategy.add_circuit_breaker_callback(self.circuit_breaker_callback)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_operations_insights_warehouse_user_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_operations_insights_warehouse_user_details)
