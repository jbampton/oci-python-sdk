# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssignEncryptionKeyDetails(object):
    """
    This is the input used to assign customer encryption key.
    """

    #: A constant which can be used with the key_type property of a AssignEncryptionKeyDetails.
    #: This constant has a value of "ACTIVE_DATA"
    KEY_TYPE_ACTIVE_DATA = "ACTIVE_DATA"

    #: A constant which can be used with the key_type property of a AssignEncryptionKeyDetails.
    #: This constant has a value of "ARCHIVAL_DATA"
    KEY_TYPE_ARCHIVAL_DATA = "ARCHIVAL_DATA"

    #: A constant which can be used with the key_type property of a AssignEncryptionKeyDetails.
    #: This constant has a value of "ALL"
    KEY_TYPE_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new AssignEncryptionKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_id:
            The value to assign to the key_id property of this AssignEncryptionKeyDetails.
        :type key_id: str

        :param key_type:
            The value to assign to the key_type property of this AssignEncryptionKeyDetails.
            Allowed values for this property are: "ACTIVE_DATA", "ARCHIVAL_DATA", "ALL"
        :type key_type: str

        """
        self.swagger_types = {
            'key_id': 'str',
            'key_type': 'str'
        }
        self.attribute_map = {
            'key_id': 'keyId',
            'key_type': 'keyType'
        }
        self._key_id = None
        self._key_type = None

    @property
    def key_id(self):
        """
        **[Required]** Gets the key_id of this AssignEncryptionKeyDetails.
        This is the key OCID for encryption key.


        :return: The key_id of this AssignEncryptionKeyDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this AssignEncryptionKeyDetails.
        This is the key OCID for encryption key.


        :param key_id: The key_id of this AssignEncryptionKeyDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_type(self):
        """
        **[Required]** Gets the key_type of this AssignEncryptionKeyDetails.
        This is the type of data to be encrypted. It can be either active or archival.

        Allowed values for this property are: "ACTIVE_DATA", "ARCHIVAL_DATA", "ALL"


        :return: The key_type of this AssignEncryptionKeyDetails.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this AssignEncryptionKeyDetails.
        This is the type of data to be encrypted. It can be either active or archival.


        :param key_type: The key_type of this AssignEncryptionKeyDetails.
        :type: str
        """
        allowed_values = ["ACTIVE_DATA", "ARCHIVAL_DATA", "ALL"]
        if not value_allowed_none_or_none_sentinel(key_type, allowed_values):
            raise ValueError(
                f"Invalid value for `key_type`, must be None or one of {allowed_values}"
            )
        self._key_type = key_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
