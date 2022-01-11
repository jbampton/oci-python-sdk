# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiffResponseEntry(object):
    """
    Entry for description of change on a file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiffResponseEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param change_type:
            The value to assign to the change_type property of this DiffResponseEntry.
        :type change_type: str

        :param object_type:
            The value to assign to the object_type property of this DiffResponseEntry.
        :type object_type: str

        :param commit_id:
            The value to assign to the commit_id property of this DiffResponseEntry.
        :type commit_id: str

        :param old_path:
            The value to assign to the old_path property of this DiffResponseEntry.
        :type old_path: str

        :param new_path:
            The value to assign to the new_path property of this DiffResponseEntry.
        :type new_path: str

        :param old_id:
            The value to assign to the old_id property of this DiffResponseEntry.
        :type old_id: str

        :param new_id:
            The value to assign to the new_id property of this DiffResponseEntry.
        :type new_id: str

        :param url:
            The value to assign to the url property of this DiffResponseEntry.
        :type url: str

        :param added_lines_count:
            The value to assign to the added_lines_count property of this DiffResponseEntry.
        :type added_lines_count: int

        :param deleted_lines_count:
            The value to assign to the deleted_lines_count property of this DiffResponseEntry.
        :type deleted_lines_count: int

        :param are_conflicts_in_file:
            The value to assign to the are_conflicts_in_file property of this DiffResponseEntry.
        :type are_conflicts_in_file: bool

        """
        self.swagger_types = {
            'change_type': 'str',
            'object_type': 'str',
            'commit_id': 'str',
            'old_path': 'str',
            'new_path': 'str',
            'old_id': 'str',
            'new_id': 'str',
            'url': 'str',
            'added_lines_count': 'int',
            'deleted_lines_count': 'int',
            'are_conflicts_in_file': 'bool'
        }

        self.attribute_map = {
            'change_type': 'changeType',
            'object_type': 'objectType',
            'commit_id': 'commitId',
            'old_path': 'oldPath',
            'new_path': 'newPath',
            'old_id': 'oldId',
            'new_id': 'newId',
            'url': 'url',
            'added_lines_count': 'addedLinesCount',
            'deleted_lines_count': 'deletedLinesCount',
            'are_conflicts_in_file': 'areConflictsInFile'
        }

        self._change_type = None
        self._object_type = None
        self._commit_id = None
        self._old_path = None
        self._new_path = None
        self._old_id = None
        self._new_id = None
        self._url = None
        self._added_lines_count = None
        self._deleted_lines_count = None
        self._are_conflicts_in_file = None

    @property
    def change_type(self):
        """
        **[Required]** Gets the change_type of this DiffResponseEntry.
        Type of change made to file.


        :return: The change_type of this DiffResponseEntry.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """
        Sets the change_type of this DiffResponseEntry.
        Type of change made to file.


        :param change_type: The change_type of this DiffResponseEntry.
        :type: str
        """
        self._change_type = change_type

    @property
    def object_type(self):
        """
        Gets the object_type of this DiffResponseEntry.
        The type of the changed object.


        :return: The object_type of this DiffResponseEntry.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this DiffResponseEntry.
        The type of the changed object.


        :param object_type: The object_type of this DiffResponseEntry.
        :type: str
        """
        self._object_type = object_type

    @property
    def commit_id(self):
        """
        Gets the commit_id of this DiffResponseEntry.
        The ID of the commit where the change is coming from.


        :return: The commit_id of this DiffResponseEntry.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this DiffResponseEntry.
        The ID of the commit where the change is coming from.


        :param commit_id: The commit_id of this DiffResponseEntry.
        :type: str
        """
        self._commit_id = commit_id

    @property
    def old_path(self):
        """
        Gets the old_path of this DiffResponseEntry.
        The path on the target to the changed object.


        :return: The old_path of this DiffResponseEntry.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        """
        Sets the old_path of this DiffResponseEntry.
        The path on the target to the changed object.


        :param old_path: The old_path of this DiffResponseEntry.
        :type: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        """
        Gets the new_path of this DiffResponseEntry.
        The path on the source to the changed object.


        :return: The new_path of this DiffResponseEntry.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        """
        Sets the new_path of this DiffResponseEntry.
        The path on the source to the changed object.


        :param new_path: The new_path of this DiffResponseEntry.
        :type: str
        """
        self._new_path = new_path

    @property
    def old_id(self):
        """
        Gets the old_id of this DiffResponseEntry.
        The ID of the changed object on the target.


        :return: The old_id of this DiffResponseEntry.
        :rtype: str
        """
        return self._old_id

    @old_id.setter
    def old_id(self, old_id):
        """
        Sets the old_id of this DiffResponseEntry.
        The ID of the changed object on the target.


        :param old_id: The old_id of this DiffResponseEntry.
        :type: str
        """
        self._old_id = old_id

    @property
    def new_id(self):
        """
        Gets the new_id of this DiffResponseEntry.
        The ID of the changed object on the source.


        :return: The new_id of this DiffResponseEntry.
        :rtype: str
        """
        return self._new_id

    @new_id.setter
    def new_id(self, new_id):
        """
        Sets the new_id of this DiffResponseEntry.
        The ID of the changed object on the source.


        :param new_id: The new_id of this DiffResponseEntry.
        :type: str
        """
        self._new_id = new_id

    @property
    def url(self):
        """
        Gets the url of this DiffResponseEntry.
        The URL of the changed object.


        :return: The url of this DiffResponseEntry.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DiffResponseEntry.
        The URL of the changed object.


        :param url: The url of this DiffResponseEntry.
        :type: str
        """
        self._url = url

    @property
    def added_lines_count(self):
        """
        Gets the added_lines_count of this DiffResponseEntry.
        The number of lines added in whole difference.


        :return: The added_lines_count of this DiffResponseEntry.
        :rtype: int
        """
        return self._added_lines_count

    @added_lines_count.setter
    def added_lines_count(self, added_lines_count):
        """
        Sets the added_lines_count of this DiffResponseEntry.
        The number of lines added in whole difference.


        :param added_lines_count: The added_lines_count of this DiffResponseEntry.
        :type: int
        """
        self._added_lines_count = added_lines_count

    @property
    def deleted_lines_count(self):
        """
        Gets the deleted_lines_count of this DiffResponseEntry.
        The number of lines deleted in whole difference.


        :return: The deleted_lines_count of this DiffResponseEntry.
        :rtype: int
        """
        return self._deleted_lines_count

    @deleted_lines_count.setter
    def deleted_lines_count(self, deleted_lines_count):
        """
        Sets the deleted_lines_count of this DiffResponseEntry.
        The number of lines deleted in whole difference.


        :param deleted_lines_count: The deleted_lines_count of this DiffResponseEntry.
        :type: int
        """
        self._deleted_lines_count = deleted_lines_count

    @property
    def are_conflicts_in_file(self):
        """
        Gets the are_conflicts_in_file of this DiffResponseEntry.
        Indicates whether the changed file contains conflicts.


        :return: The are_conflicts_in_file of this DiffResponseEntry.
        :rtype: bool
        """
        return self._are_conflicts_in_file

    @are_conflicts_in_file.setter
    def are_conflicts_in_file(self, are_conflicts_in_file):
        """
        Sets the are_conflicts_in_file of this DiffResponseEntry.
        Indicates whether the changed file contains conflicts.


        :param are_conflicts_in_file: The are_conflicts_in_file of this DiffResponseEntry.
        :type: bool
        """
        self._are_conflicts_in_file = are_conflicts_in_file

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
