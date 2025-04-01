# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .auth_configuration import AuthConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IamAuthConfiguration(AuthConfiguration):
    """
    Configuration of IAM AuthN/Z for online prediction
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IamAuthConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.IamAuthConfiguration.type` attribute
        of this class is ``IAM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this IamAuthConfiguration.
            Allowed values for this property are: "IDCS", "IAM", "IDCS_CUSTOM_SERVICE"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }
        self.attribute_map = {
            'type': 'type'
        }
        self._type = None
        self._type = 'IAM'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
