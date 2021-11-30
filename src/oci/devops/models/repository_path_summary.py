# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryPathSummary(object):
    """
    Object containing information about files and directories in a repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryPathSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RepositoryPathSummary.
        :type type: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this RepositoryPathSummary.
        :type size_in_bytes: int

        :param name:
            The value to assign to the name property of this RepositoryPathSummary.
        :type name: str

        :param path:
            The value to assign to the path property of this RepositoryPathSummary.
        :type path: str

        :param sha:
            The value to assign to the sha property of this RepositoryPathSummary.
        :type sha: str

        :param submodule_git_url:
            The value to assign to the submodule_git_url property of this RepositoryPathSummary.
        :type submodule_git_url: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryPathSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryPathSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'type': 'str',
            'size_in_bytes': 'int',
            'name': 'str',
            'path': 'str',
            'sha': 'str',
            'submodule_git_url': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'type': 'type',
            'size_in_bytes': 'sizeInBytes',
            'name': 'name',
            'path': 'path',
            'sha': 'sha',
            'submodule_git_url': 'submoduleGitUrl',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._type = None
        self._size_in_bytes = None
        self._name = None
        self._path = None
        self._sha = None
        self._submodule_git_url = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def type(self):
        """
        Gets the type of this RepositoryPathSummary.
        File or directory.


        :return: The type of this RepositoryPathSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RepositoryPathSummary.
        File or directory.


        :param type: The type of this RepositoryPathSummary.
        :type: str
        """
        self._type = type

    @property
    def size_in_bytes(self):
        """
        Gets the size_in_bytes of this RepositoryPathSummary.
        Size of file or directory.


        :return: The size_in_bytes of this RepositoryPathSummary.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this RepositoryPathSummary.
        Size of file or directory.


        :param size_in_bytes: The size_in_bytes of this RepositoryPathSummary.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def name(self):
        """
        Gets the name of this RepositoryPathSummary.
        Name of file or directory.


        :return: The name of this RepositoryPathSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RepositoryPathSummary.
        Name of file or directory.


        :param name: The name of this RepositoryPathSummary.
        :type: str
        """
        self._name = name

    @property
    def path(self):
        """
        Gets the path of this RepositoryPathSummary.
        Path to file or directory in a repository.


        :return: The path of this RepositoryPathSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this RepositoryPathSummary.
        Path to file or directory in a repository.


        :param path: The path of this RepositoryPathSummary.
        :type: str
        """
        self._path = path

    @property
    def sha(self):
        """
        Gets the sha of this RepositoryPathSummary.
        SHA-1 checksum of blob or tree.


        :return: The sha of this RepositoryPathSummary.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """
        Sets the sha of this RepositoryPathSummary.
        SHA-1 checksum of blob or tree.


        :param sha: The sha of this RepositoryPathSummary.
        :type: str
        """
        self._sha = sha

    @property
    def submodule_git_url(self):
        """
        Gets the submodule_git_url of this RepositoryPathSummary.
        The git URL of the submodule.


        :return: The submodule_git_url of this RepositoryPathSummary.
        :rtype: str
        """
        return self._submodule_git_url

    @submodule_git_url.setter
    def submodule_git_url(self, submodule_git_url):
        """
        Sets the submodule_git_url of this RepositoryPathSummary.
        The git URL of the submodule.


        :param submodule_git_url: The submodule_git_url of this RepositoryPathSummary.
        :type: str
        """
        self._submodule_git_url = submodule_git_url

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositoryPathSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositoryPathSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositoryPathSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositoryPathSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositoryPathSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositoryPathSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositoryPathSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositoryPathSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
