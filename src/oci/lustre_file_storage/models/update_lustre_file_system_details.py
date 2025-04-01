# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLustreFileSystemDetails(object):
    """
    The data to update a Lustre file system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLustreFileSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateLustreFileSystemDetails.
        :type display_name: str

        :param file_system_description:
            The value to assign to the file_system_description property of this UpdateLustreFileSystemDetails.
        :type file_system_description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLustreFileSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLustreFileSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateLustreFileSystemDetails.
        :type nsg_ids: list[str]

        :param kms_key_id:
            The value to assign to the kms_key_id property of this UpdateLustreFileSystemDetails.
        :type kms_key_id: str

        :param capacity_in_gbs:
            The value to assign to the capacity_in_gbs property of this UpdateLustreFileSystemDetails.
        :type capacity_in_gbs: int

        :param root_squash_configuration:
            The value to assign to the root_squash_configuration property of this UpdateLustreFileSystemDetails.
        :type root_squash_configuration: oci.lustre_file_storage.models.RootSquashConfiguration

        """
        self.swagger_types = {
            'display_name': 'str',
            'file_system_description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'nsg_ids': 'list[str]',
            'kms_key_id': 'str',
            'capacity_in_gbs': 'int',
            'root_squash_configuration': 'RootSquashConfiguration'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'file_system_description': 'fileSystemDescription',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'nsg_ids': 'nsgIds',
            'kms_key_id': 'kmsKeyId',
            'capacity_in_gbs': 'capacityInGBs',
            'root_squash_configuration': 'rootSquashConfiguration'
        }
        self._display_name = None
        self._file_system_description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._nsg_ids = None
        self._kms_key_id = None
        self._capacity_in_gbs = None
        self._root_squash_configuration = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateLustreFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My Lustre file system`


        :return: The display_name of this UpdateLustreFileSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateLustreFileSystemDetails.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.

        Example: `My Lustre file system`


        :param display_name: The display_name of this UpdateLustreFileSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def file_system_description(self):
        """
        Gets the file_system_description of this UpdateLustreFileSystemDetails.
        Short description of the Lustre file system.
        Avoid entering confidential information.


        :return: The file_system_description of this UpdateLustreFileSystemDetails.
        :rtype: str
        """
        return self._file_system_description

    @file_system_description.setter
    def file_system_description(self, file_system_description):
        """
        Sets the file_system_description of this UpdateLustreFileSystemDetails.
        Short description of the Lustre file system.
        Avoid entering confidential information.


        :param file_system_description: The file_system_description of this UpdateLustreFileSystemDetails.
        :type: str
        """
        self._file_system_description = file_system_description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateLustreFileSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateLustreFileSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateLustreFileSystemDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateLustreFileSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateLustreFileSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateLustreFileSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateLustreFileSystemDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateLustreFileSystemDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateLustreFileSystemDetails.
        A list of Network Security Group `OCIDs`__ associated with this lustre file system.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the lustre file system from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateLustreFileSystemDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateLustreFileSystemDetails.
        A list of Network Security Group `OCIDs`__ associated with this lustre file system.
        A maximum of 5 is allowed.
        Setting this to an empty array after the list is created removes the lustre file system from all NSGs.
        For more information about NSGs, see `Security Rules`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateLustreFileSystemDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this UpdateLustreFileSystemDetails.
        The `OCID`__ of the KMS key used to encrypt the encryption keys associated with this file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The kms_key_id of this UpdateLustreFileSystemDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this UpdateLustreFileSystemDetails.
        The `OCID`__ of the KMS key used to encrypt the encryption keys associated with this file system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param kms_key_id: The kms_key_id of this UpdateLustreFileSystemDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def capacity_in_gbs(self):
        """
        Gets the capacity_in_gbs of this UpdateLustreFileSystemDetails.
        Capacity of the Lustre file system in GB. You can increase capacity only in multiples of 5 TB.


        :return: The capacity_in_gbs of this UpdateLustreFileSystemDetails.
        :rtype: int
        """
        return self._capacity_in_gbs

    @capacity_in_gbs.setter
    def capacity_in_gbs(self, capacity_in_gbs):
        """
        Sets the capacity_in_gbs of this UpdateLustreFileSystemDetails.
        Capacity of the Lustre file system in GB. You can increase capacity only in multiples of 5 TB.


        :param capacity_in_gbs: The capacity_in_gbs of this UpdateLustreFileSystemDetails.
        :type: int
        """
        self._capacity_in_gbs = capacity_in_gbs

    @property
    def root_squash_configuration(self):
        """
        Gets the root_squash_configuration of this UpdateLustreFileSystemDetails.

        :return: The root_squash_configuration of this UpdateLustreFileSystemDetails.
        :rtype: oci.lustre_file_storage.models.RootSquashConfiguration
        """
        return self._root_squash_configuration

    @root_squash_configuration.setter
    def root_squash_configuration(self, root_squash_configuration):
        """
        Sets the root_squash_configuration of this UpdateLustreFileSystemDetails.

        :param root_squash_configuration: The root_squash_configuration of this UpdateLustreFileSystemDetails.
        :type: oci.lustre_file_storage.models.RootSquashConfiguration
        """
        self._root_squash_configuration = root_squash_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
