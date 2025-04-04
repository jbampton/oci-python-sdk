# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190506


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaPrivateEndpointScanProxy(object):
    """
    Details pertaining to a scan proxy instance created for a scan listener FQDN/IPs
    """

    #: A constant which can be used with the scan_listener_type property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "FQDN"
    SCAN_LISTENER_TYPE_FQDN = "FQDN"

    #: A constant which can be used with the scan_listener_type property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "IP"
    SCAN_LISTENER_TYPE_IP = "IP"

    #: A constant which can be used with the protocol property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the lifecycle_state property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OdaPrivateEndpointScanProxy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OdaPrivateEndpointScanProxy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaPrivateEndpointScanProxy.
        :type id: str

        :param scan_listener_type:
            The value to assign to the scan_listener_type property of this OdaPrivateEndpointScanProxy.
            Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scan_listener_type: str

        :param protocol:
            The value to assign to the protocol property of this OdaPrivateEndpointScanProxy.
            Allowed values for this property are: "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param scan_listener_infos:
            The value to assign to the scan_listener_infos property of this OdaPrivateEndpointScanProxy.
        :type scan_listener_infos: list[oci.oda.models.ScanListenerInfo]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaPrivateEndpointScanProxy.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this OdaPrivateEndpointScanProxy.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'scan_listener_type': 'str',
            'protocol': 'str',
            'scan_listener_infos': 'list[ScanListenerInfo]',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'scan_listener_type': 'scanListenerType',
            'protocol': 'protocol',
            'scan_listener_infos': 'scanListenerInfos',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }
        self._id = None
        self._scan_listener_type = None
        self._protocol = None
        self._scan_listener_infos = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaPrivateEndpointScanProxy.
        The `OCID`__ of the ODA Private Endpoint Scan Proxy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this OdaPrivateEndpointScanProxy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaPrivateEndpointScanProxy.
        The `OCID`__ of the ODA Private Endpoint Scan Proxy.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this OdaPrivateEndpointScanProxy.
        :type: str
        """
        self._id = id

    @property
    def scan_listener_type(self):
        """
        **[Required]** Gets the scan_listener_type of this OdaPrivateEndpointScanProxy.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs

        Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The scan_listener_type of this OdaPrivateEndpointScanProxy.
        :rtype: str
        """
        return self._scan_listener_type

    @scan_listener_type.setter
    def scan_listener_type(self, scan_listener_type):
        """
        Sets the scan_listener_type of this OdaPrivateEndpointScanProxy.
        Type indicating whether Scan listener is specified by its FQDN or list of IPs


        :param scan_listener_type: The scan_listener_type of this OdaPrivateEndpointScanProxy.
        :type: str
        """
        allowed_values = ["FQDN", "IP"]
        if not value_allowed_none_or_none_sentinel(scan_listener_type, allowed_values):
            scan_listener_type = 'UNKNOWN_ENUM_VALUE'
        self._scan_listener_type = scan_listener_type

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this OdaPrivateEndpointScanProxy.
        The protocol used for communication between client, scanProxy and RAC's scan listeners

        Allowed values for this property are: "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this OdaPrivateEndpointScanProxy.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this OdaPrivateEndpointScanProxy.
        The protocol used for communication between client, scanProxy and RAC's scan listeners


        :param protocol: The protocol of this OdaPrivateEndpointScanProxy.
        :type: str
        """
        allowed_values = ["TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def scan_listener_infos(self):
        """
        **[Required]** Gets the scan_listener_infos of this OdaPrivateEndpointScanProxy.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :return: The scan_listener_infos of this OdaPrivateEndpointScanProxy.
        :rtype: list[oci.oda.models.ScanListenerInfo]
        """
        return self._scan_listener_infos

    @scan_listener_infos.setter
    def scan_listener_infos(self, scan_listener_infos):
        """
        Sets the scan_listener_infos of this OdaPrivateEndpointScanProxy.
        The FQDN/IPs and port information of customer's Real Application Cluster (RAC)'s SCAN listeners.


        :param scan_listener_infos: The scan_listener_infos of this OdaPrivateEndpointScanProxy.
        :type: list[oci.oda.models.ScanListenerInfo]
        """
        self._scan_listener_infos = scan_listener_infos

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OdaPrivateEndpointScanProxy.
        The current state of the ODA Private Endpoint Scan Proxy.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OdaPrivateEndpointScanProxy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaPrivateEndpointScanProxy.
        The current state of the ODA Private Endpoint Scan Proxy.


        :param lifecycle_state: The lifecycle_state of this OdaPrivateEndpointScanProxy.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this OdaPrivateEndpointScanProxy.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OdaPrivateEndpointScanProxy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaPrivateEndpointScanProxy.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OdaPrivateEndpointScanProxy.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
