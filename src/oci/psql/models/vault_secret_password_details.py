# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915

from .password_details import PasswordDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VaultSecretPasswordDetails(PasswordDetails):
    """
    Secret details for the database system password.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VaultSecretPasswordDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.psql.models.VaultSecretPasswordDetails.password_type` attribute
        of this class is ``VAULT_SECRET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password_type:
            The value to assign to the password_type property of this VaultSecretPasswordDetails.
            Allowed values for this property are: "PLAIN_TEXT", "VAULT_SECRET"
        :type password_type: str

        :param secret_id:
            The value to assign to the secret_id property of this VaultSecretPasswordDetails.
        :type secret_id: str

        :param secret_version:
            The value to assign to the secret_version property of this VaultSecretPasswordDetails.
        :type secret_version: str

        """
        self.swagger_types = {
            'password_type': 'str',
            'secret_id': 'str',
            'secret_version': 'str'
        }
        self.attribute_map = {
            'password_type': 'passwordType',
            'secret_id': 'secretId',
            'secret_version': 'secretVersion'
        }
        self._password_type = None
        self._secret_id = None
        self._secret_version = None
        self._password_type = 'VAULT_SECRET'

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this VaultSecretPasswordDetails.
        The `OCID`__ of the secret where the password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The secret_id of this VaultSecretPasswordDetails.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this VaultSecretPasswordDetails.
        The `OCID`__ of the secret where the password is stored.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param secret_id: The secret_id of this VaultSecretPasswordDetails.
        :type: str
        """
        self._secret_id = secret_id

    @property
    def secret_version(self):
        """
        **[Required]** Gets the secret_version of this VaultSecretPasswordDetails.
        The secret version of the stored password.


        :return: The secret_version of this VaultSecretPasswordDetails.
        :rtype: str
        """
        return self._secret_version

    @secret_version.setter
    def secret_version(self, secret_version):
        """
        Sets the secret_version of this VaultSecretPasswordDetails.
        The secret version of the stored password.


        :param secret_version: The secret_version of this VaultSecretPasswordDetails.
        :type: str
        """
        self._secret_version = secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
