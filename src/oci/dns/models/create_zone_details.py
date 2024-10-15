# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115

from .create_zone_base_details import CreateZoneBaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateZoneDetails(CreateZoneBaseDetails):
    """
    The body for defining a new zone.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "PRIMARY"
    ZONE_TYPE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the zone_type property of a CreateZoneDetails.
    #: This constant has a value of "SECONDARY"
    ZONE_TYPE_SECONDARY = "SECONDARY"

    #: A constant which can be used with the scope property of a CreateZoneDetails.
    #: This constant has a value of "GLOBAL"
    SCOPE_GLOBAL = "GLOBAL"

    #: A constant which can be used with the scope property of a CreateZoneDetails.
    #: This constant has a value of "PRIVATE"
    SCOPE_PRIVATE = "PRIVATE"

    #: A constant which can be used with the dnssec_state property of a CreateZoneDetails.
    #: This constant has a value of "ENABLED"
    DNSSEC_STATE_ENABLED = "ENABLED"

    #: A constant which can be used with the dnssec_state property of a CreateZoneDetails.
    #: This constant has a value of "DISABLED"
    DNSSEC_STATE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateZoneDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.CreateZoneDetails.migration_source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param migration_source:
            The value to assign to the migration_source property of this CreateZoneDetails.
            Allowed values for this property are: "NONE", "DYNECT"
        :type migration_source: str

        :param name:
            The value to assign to the name property of this CreateZoneDetails.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateZoneDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateZoneDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateZoneDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param zone_type:
            The value to assign to the zone_type property of this CreateZoneDetails.
            Allowed values for this property are: "PRIMARY", "SECONDARY"
        :type zone_type: str

        :param view_id:
            The value to assign to the view_id property of this CreateZoneDetails.
        :type view_id: str

        :param scope:
            The value to assign to the scope property of this CreateZoneDetails.
            Allowed values for this property are: "GLOBAL", "PRIVATE"
        :type scope: str

        :param external_masters:
            The value to assign to the external_masters property of this CreateZoneDetails.
        :type external_masters: list[oci.dns.models.ExternalMaster]

        :param external_downstreams:
            The value to assign to the external_downstreams property of this CreateZoneDetails.
        :type external_downstreams: list[oci.dns.models.ExternalDownstream]

        :param dnssec_state:
            The value to assign to the dnssec_state property of this CreateZoneDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type dnssec_state: str

        """
        self.swagger_types = {
            'migration_source': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'zone_type': 'str',
            'view_id': 'str',
            'scope': 'str',
            'external_masters': 'list[ExternalMaster]',
            'external_downstreams': 'list[ExternalDownstream]',
            'dnssec_state': 'str'
        }

        self.attribute_map = {
            'migration_source': 'migrationSource',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'zone_type': 'zoneType',
            'view_id': 'viewId',
            'scope': 'scope',
            'external_masters': 'externalMasters',
            'external_downstreams': 'externalDownstreams',
            'dnssec_state': 'dnssecState'
        }

        self._migration_source = None
        self._name = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._zone_type = None
        self._view_id = None
        self._scope = None
        self._external_masters = None
        self._external_downstreams = None
        self._dnssec_state = None
        self._migration_source = 'NONE'

    @property
    def zone_type(self):
        """
        Gets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL
        zones.

        Allowed values for this property are: "PRIMARY", "SECONDARY"


        :return: The zone_type of this CreateZoneDetails.
        :rtype: str
        """
        return self._zone_type

    @zone_type.setter
    def zone_type(self, zone_type):
        """
        Sets the zone_type of this CreateZoneDetails.
        The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL
        zones.


        :param zone_type: The zone_type of this CreateZoneDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "SECONDARY"]
        if not value_allowed_none_or_none_sentinel(zone_type, allowed_values):
            raise ValueError(
                f"Invalid value for `zone_type`, must be None or one of {allowed_values}"
            )
        self._zone_type = zone_type

    @property
    def view_id(self):
        """
        Gets the view_id of this CreateZoneDetails.
        This value will be null for zones in the global DNS.


        :return: The view_id of this CreateZoneDetails.
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """
        Sets the view_id of this CreateZoneDetails.
        This value will be null for zones in the global DNS.


        :param view_id: The view_id of this CreateZoneDetails.
        :type: str
        """
        self._view_id = view_id

    @property
    def scope(self):
        """
        Gets the scope of this CreateZoneDetails.
        The scope of the zone.

        Allowed values for this property are: "GLOBAL", "PRIVATE"


        :return: The scope of this CreateZoneDetails.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this CreateZoneDetails.
        The scope of the zone.


        :param scope: The scope of this CreateZoneDetails.
        :type: str
        """
        allowed_values = ["GLOBAL", "PRIVATE"]
        if not value_allowed_none_or_none_sentinel(scope, allowed_values):
            raise ValueError(
                f"Invalid value for `scope`, must be None or one of {allowed_values}"
            )
        self._scope = scope

    @property
    def external_masters(self):
        """
        Gets the external_masters of this CreateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :return: The external_masters of this CreateZoneDetails.
        :rtype: list[oci.dns.models.ExternalMaster]
        """
        return self._external_masters

    @external_masters.setter
    def external_masters(self, external_masters):
        """
        Sets the external_masters of this CreateZoneDetails.
        External master servers for the zone. `externalMasters` becomes a
        required parameter when the `zoneType` value is `SECONDARY`.


        :param external_masters: The external_masters of this CreateZoneDetails.
        :type: list[oci.dns.models.ExternalMaster]
        """
        self._external_masters = external_masters

    @property
    def external_downstreams(self):
        """
        Gets the external_downstreams of this CreateZoneDetails.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :return: The external_downstreams of this CreateZoneDetails.
        :rtype: list[oci.dns.models.ExternalDownstream]
        """
        return self._external_downstreams

    @external_downstreams.setter
    def external_downstreams(self, external_downstreams):
        """
        Sets the external_downstreams of this CreateZoneDetails.
        External secondary servers for the zone.
        This field is currently not supported when `zoneType` is `SECONDARY` or `scope` is `PRIVATE`.


        :param external_downstreams: The external_downstreams of this CreateZoneDetails.
        :type: list[oci.dns.models.ExternalDownstream]
        """
        self._external_downstreams = external_downstreams

    @property
    def dnssec_state(self):
        """
        Gets the dnssec_state of this CreateZoneDetails.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The dnssec_state of this CreateZoneDetails.
        :rtype: str
        """
        return self._dnssec_state

    @dnssec_state.setter
    def dnssec_state(self, dnssec_state):
        """
        Sets the dnssec_state of this CreateZoneDetails.
        The state of DNSSEC on the zone.

        For DNSSEC to function, every parent zone in the DNS tree up to the top-level domain (or an independent
        trust anchor) must also have DNSSEC correctly set up.
        After enabling DNSSEC, you must add a DS record to the zone's parent zone containing the
        `KskDnssecKeyVersion` data. You can find the DS data in the `dsData` attribute of the `KskDnssecKeyVersion`.
        Then, use the `PromoteZoneDnssecKeyVersion` operation to promote the `KskDnssecKeyVersion`.

        New `KskDnssecKeyVersion`s are generated annually, a week before the existing `KskDnssecKeyVersion`'s expiration.
        To rollover a `KskDnssecKeyVersion`, you must replace the parent zone's DS record containing the old
        `KskDnssecKeyVersion` data with the data from the new `KskDnssecKeyVersion`.

        To remove the old DS record without causing service disruption, wait until the old DS record's TTL has
        expired, and the new DS record has propagated. After the DS replacement has been completed, then the
        `PromoteZoneDnssecKeyVersion` operation must be called.

        Metrics are emitted in the `oci_dns` namespace daily for each `KskDnssecKeyVersion` indicating how many
        days are left until expiration.
        We recommend that you set up alarms and notifications for KskDnssecKeyVersion expiration so that the
        necessary parent zone updates can be made and the `PromoteZoneDnssecKeyVersion` operation can be called.

        Enabling DNSSEC results in additional records in DNS responses which increases their size and can
        cause higher response latency.

        For more information, see `DNSSEC`__.

        __ https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnssec.htm


        :param dnssec_state: The dnssec_state of this CreateZoneDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(dnssec_state, allowed_values):
            raise ValueError(
                f"Invalid value for `dnssec_state`, must be None or one of {allowed_values}"
            )
        self._dnssec_state = dnssec_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
