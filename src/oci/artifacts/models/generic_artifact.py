# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenericArtifact(object):
    """
    The metadata of the artifact.
    """

    #: A constant which can be used with the lifecycle_state property of a GenericArtifact.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a GenericArtifact.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a GenericArtifact.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new GenericArtifact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GenericArtifact.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this GenericArtifact.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GenericArtifact.
        :type compartment_id: str

        :param repository_id:
            The value to assign to the repository_id property of this GenericArtifact.
        :type repository_id: str

        :param artifact_path:
            The value to assign to the artifact_path property of this GenericArtifact.
        :type artifact_path: str

        :param version:
            The value to assign to the version property of this GenericArtifact.
        :type version: str

        :param sha256:
            The value to assign to the sha256 property of this GenericArtifact.
        :type sha256: str

        :param size_in_bytes:
            The value to assign to the size_in_bytes property of this GenericArtifact.
        :type size_in_bytes: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GenericArtifact.
            Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GenericArtifact.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GenericArtifact.
        :type defined_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this GenericArtifact.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'repository_id': 'str',
            'artifact_path': 'str',
            'version': 'str',
            'sha256': 'str',
            'size_in_bytes': 'int',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'repository_id': 'repositoryId',
            'artifact_path': 'artifactPath',
            'version': 'version',
            'sha256': 'sha256',
            'size_in_bytes': 'sizeInBytes',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._repository_id = None
        self._artifact_path = None
        self._version = None
        self._sha256 = None
        self._size_in_bytes = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this GenericArtifact.
        The `OCID`__ of the artifact.

        Example: `ocid1.genericartifact.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this GenericArtifact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GenericArtifact.
        The `OCID`__ of the artifact.

        Example: `ocid1.genericartifact.oc1..exampleuniqueID`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this GenericArtifact.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this GenericArtifact.
        The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.

        Example: `project01/my-web-app/artifact-abc:1.0.0`


        :return: The display_name of this GenericArtifact.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GenericArtifact.
        The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.

        Example: `project01/my-web-app/artifact-abc:1.0.0`


        :param display_name: The display_name of this GenericArtifact.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this GenericArtifact.
        The `OCID`__ of the repository's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this GenericArtifact.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this GenericArtifact.
        The `OCID`__ of the repository's compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this GenericArtifact.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this GenericArtifact.
        The `OCID`__ of the repository.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The repository_id of this GenericArtifact.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this GenericArtifact.
        The `OCID`__ of the repository.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param repository_id: The repository_id of this GenericArtifact.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def artifact_path(self):
        """
        **[Required]** Gets the artifact_path of this GenericArtifact.
        A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.

        Example: `project01/my-web-app/artifact-abc`


        :return: The artifact_path of this GenericArtifact.
        :rtype: str
        """
        return self._artifact_path

    @artifact_path.setter
    def artifact_path(self, artifact_path):
        """
        Sets the artifact_path of this GenericArtifact.
        A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize the repository. An artifact path does not include an artifact version.

        Example: `project01/my-web-app/artifact-abc`


        :param artifact_path: The artifact_path of this GenericArtifact.
        :type: str
        """
        self._artifact_path = artifact_path

    @property
    def version(self):
        """
        **[Required]** Gets the version of this GenericArtifact.
        A user-defined string to describe the artifact version.

        Example: `1.1.0` or `1.2-beta-2`


        :return: The version of this GenericArtifact.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this GenericArtifact.
        A user-defined string to describe the artifact version.

        Example: `1.1.0` or `1.2-beta-2`


        :param version: The version of this GenericArtifact.
        :type: str
        """
        self._version = version

    @property
    def sha256(self):
        """
        **[Required]** Gets the sha256 of this GenericArtifact.
        The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.


        :return: The sha256 of this GenericArtifact.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """
        Sets the sha256 of this GenericArtifact.
        The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact properties.


        :param sha256: The sha256 of this GenericArtifact.
        :type: str
        """
        self._sha256 = sha256

    @property
    def size_in_bytes(self):
        """
        **[Required]** Gets the size_in_bytes of this GenericArtifact.
        The size of the artifact in bytes.


        :return: The size_in_bytes of this GenericArtifact.
        :rtype: int
        """
        return self._size_in_bytes

    @size_in_bytes.setter
    def size_in_bytes(self, size_in_bytes):
        """
        Sets the size_in_bytes of this GenericArtifact.
        The size of the artifact in bytes.


        :param size_in_bytes: The size_in_bytes of this GenericArtifact.
        :type: int
        """
        self._size_in_bytes = size_in_bytes

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this GenericArtifact.
        The current state of the artifact.

        Allowed values for this property are: "AVAILABLE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this GenericArtifact.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this GenericArtifact.
        The current state of the artifact.


        :param lifecycle_state: The lifecycle_state of this GenericArtifact.
        :type: str
        """
        allowed_values = ["AVAILABLE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this GenericArtifact.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this GenericArtifact.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this GenericArtifact.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this GenericArtifact.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this GenericArtifact.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this GenericArtifact.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this GenericArtifact.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this GenericArtifact.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this GenericArtifact.
        An RFC 3339 timestamp indicating when the repository was created.


        :return: The time_created of this GenericArtifact.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this GenericArtifact.
        An RFC 3339 timestamp indicating when the repository was created.


        :param time_created: The time_created of this GenericArtifact.
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
