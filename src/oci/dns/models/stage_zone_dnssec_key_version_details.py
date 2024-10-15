# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180115


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StageZoneDnssecKeyVersionDetails(object):
    """
    Details for staging a `DnssecKeyVersion` on a zone.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StageZoneDnssecKeyVersionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param predecessor_dnssec_key_version_uuid:
            The value to assign to the predecessor_dnssec_key_version_uuid property of this StageZoneDnssecKeyVersionDetails.
        :type predecessor_dnssec_key_version_uuid: str

        """
        self.swagger_types = {
            'predecessor_dnssec_key_version_uuid': 'str'
        }

        self.attribute_map = {
            'predecessor_dnssec_key_version_uuid': 'predecessorDnssecKeyVersionUuid'
        }

        self._predecessor_dnssec_key_version_uuid = None

    @property
    def predecessor_dnssec_key_version_uuid(self):
        """
        **[Required]** Gets the predecessor_dnssec_key_version_uuid of this StageZoneDnssecKeyVersionDetails.
        The UUID of the `DnssecKeyVersion` for which a new successor should be generated.


        :return: The predecessor_dnssec_key_version_uuid of this StageZoneDnssecKeyVersionDetails.
        :rtype: str
        """
        return self._predecessor_dnssec_key_version_uuid

    @predecessor_dnssec_key_version_uuid.setter
    def predecessor_dnssec_key_version_uuid(self, predecessor_dnssec_key_version_uuid):
        """
        Sets the predecessor_dnssec_key_version_uuid of this StageZoneDnssecKeyVersionDetails.
        The UUID of the `DnssecKeyVersion` for which a new successor should be generated.


        :param predecessor_dnssec_key_version_uuid: The predecessor_dnssec_key_version_uuid of this StageZoneDnssecKeyVersionDetails.
        :type: str
        """
        self._predecessor_dnssec_key_version_uuid = predecessor_dnssec_key_version_uuid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
