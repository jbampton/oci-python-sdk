# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Storage(object):
    """
    This is the storage configuration and status of a tenancy in Logan Analytics application
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Storage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_archiving_enabled:
            The value to assign to the is_archiving_enabled property of this Storage.
        :type is_archiving_enabled: bool

        :param archiving_configuration:
            The value to assign to the archiving_configuration property of this Storage.
        :type archiving_configuration: oci.log_analytics.models.ArchivingConfiguration

        """
        self.swagger_types = {
            'is_archiving_enabled': 'bool',
            'archiving_configuration': 'ArchivingConfiguration'
        }

        self.attribute_map = {
            'is_archiving_enabled': 'isArchivingEnabled',
            'archiving_configuration': 'archivingConfiguration'
        }

        self._is_archiving_enabled = None
        self._archiving_configuration = None

    @property
    def is_archiving_enabled(self):
        """
        **[Required]** Gets the is_archiving_enabled of this Storage.
        This indicates if old data can be archived for a tenancy


        :return: The is_archiving_enabled of this Storage.
        :rtype: bool
        """
        return self._is_archiving_enabled

    @is_archiving_enabled.setter
    def is_archiving_enabled(self, is_archiving_enabled):
        """
        Sets the is_archiving_enabled of this Storage.
        This indicates if old data can be archived for a tenancy


        :param is_archiving_enabled: The is_archiving_enabled of this Storage.
        :type: bool
        """
        self._is_archiving_enabled = is_archiving_enabled

    @property
    def archiving_configuration(self):
        """
        **[Required]** Gets the archiving_configuration of this Storage.

        :return: The archiving_configuration of this Storage.
        :rtype: oci.log_analytics.models.ArchivingConfiguration
        """
        return self._archiving_configuration

    @archiving_configuration.setter
    def archiving_configuration(self, archiving_configuration):
        """
        Sets the archiving_configuration of this Storage.

        :param archiving_configuration: The archiving_configuration of this Storage.
        :type: oci.log_analytics.models.ArchivingConfiguration
        """
        self._archiving_configuration = archiving_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
