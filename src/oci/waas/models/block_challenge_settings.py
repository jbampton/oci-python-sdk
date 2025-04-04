# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181116


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BlockChallengeSettings(object):
    """
    The challenge settings if `action` is set to `BLOCK`.
    """

    #: A constant which can be used with the block_action property of a BlockChallengeSettings.
    #: This constant has a value of "SET_RESPONSE_CODE"
    BLOCK_ACTION_SET_RESPONSE_CODE = "SET_RESPONSE_CODE"

    #: A constant which can be used with the block_action property of a BlockChallengeSettings.
    #: This constant has a value of "SHOW_ERROR_PAGE"
    BLOCK_ACTION_SHOW_ERROR_PAGE = "SHOW_ERROR_PAGE"

    #: A constant which can be used with the block_action property of a BlockChallengeSettings.
    #: This constant has a value of "SHOW_CAPTCHA"
    BLOCK_ACTION_SHOW_CAPTCHA = "SHOW_CAPTCHA"

    def __init__(self, **kwargs):
        """
        Initializes a new BlockChallengeSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param block_action:
            The value to assign to the block_action property of this BlockChallengeSettings.
            Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", "SHOW_CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type block_action: str

        :param block_response_code:
            The value to assign to the block_response_code property of this BlockChallengeSettings.
        :type block_response_code: int

        :param block_error_page_message:
            The value to assign to the block_error_page_message property of this BlockChallengeSettings.
        :type block_error_page_message: str

        :param block_error_page_description:
            The value to assign to the block_error_page_description property of this BlockChallengeSettings.
        :type block_error_page_description: str

        :param block_error_page_code:
            The value to assign to the block_error_page_code property of this BlockChallengeSettings.
        :type block_error_page_code: str

        :param captcha_title:
            The value to assign to the captcha_title property of this BlockChallengeSettings.
        :type captcha_title: str

        :param captcha_header:
            The value to assign to the captcha_header property of this BlockChallengeSettings.
        :type captcha_header: str

        :param captcha_footer:
            The value to assign to the captcha_footer property of this BlockChallengeSettings.
        :type captcha_footer: str

        :param captcha_submit_label:
            The value to assign to the captcha_submit_label property of this BlockChallengeSettings.
        :type captcha_submit_label: str

        """
        self.swagger_types = {
            'block_action': 'str',
            'block_response_code': 'int',
            'block_error_page_message': 'str',
            'block_error_page_description': 'str',
            'block_error_page_code': 'str',
            'captcha_title': 'str',
            'captcha_header': 'str',
            'captcha_footer': 'str',
            'captcha_submit_label': 'str'
        }
        self.attribute_map = {
            'block_action': 'blockAction',
            'block_response_code': 'blockResponseCode',
            'block_error_page_message': 'blockErrorPageMessage',
            'block_error_page_description': 'blockErrorPageDescription',
            'block_error_page_code': 'blockErrorPageCode',
            'captcha_title': 'captchaTitle',
            'captcha_header': 'captchaHeader',
            'captcha_footer': 'captchaFooter',
            'captcha_submit_label': 'captchaSubmitLabel'
        }
        self._block_action = None
        self._block_response_code = None
        self._block_error_page_message = None
        self._block_error_page_description = None
        self._block_error_page_code = None
        self._captcha_title = None
        self._captcha_header = None
        self._captcha_footer = None
        self._captcha_submit_label = None

    @property
    def block_action(self):
        """
        Gets the block_action of this BlockChallengeSettings.
        The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.

        Allowed values for this property are: "SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", "SHOW_CAPTCHA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The block_action of this BlockChallengeSettings.
        :rtype: str
        """
        return self._block_action

    @block_action.setter
    def block_action(self, block_action):
        """
        Sets the block_action of this BlockChallengeSettings.
        The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to `SHOW_ERROR_PAGE`.


        :param block_action: The block_action of this BlockChallengeSettings.
        :type: str
        """
        allowed_values = ["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE", "SHOW_CAPTCHA"]
        if not value_allowed_none_or_none_sentinel(block_action, allowed_values):
            block_action = 'UNKNOWN_ENUM_VALUE'
        self._block_action = block_action

    @property
    def block_response_code(self):
        """
        Gets the block_response_code of this BlockChallengeSettings.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :return: The block_response_code of this BlockChallengeSettings.
        :rtype: int
        """
        return self._block_response_code

    @block_response_code.setter
    def block_response_code(self, block_response_code):
        """
        Sets the block_response_code of this BlockChallengeSettings.
        The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.


        :param block_response_code: The block_response_code of this BlockChallengeSettings.
        :type: int
        """
        self._block_response_code = block_response_code

    @property
    def block_error_page_message(self):
        """
        Gets the block_error_page_message of this BlockChallengeSettings.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.


        :return: The block_error_page_message of this BlockChallengeSettings.
        :rtype: str
        """
        return self._block_error_page_message

    @block_error_page_message.setter
    def block_error_page_message(self, block_error_page_message):
        """
        Sets the block_error_page_message of this BlockChallengeSettings.
        The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access to the website is blocked`.


        :param block_error_page_message: The block_error_page_message of this BlockChallengeSettings.
        :type: str
        """
        self._block_error_page_message = block_error_page_message

    @property
    def block_error_page_description(self):
        """
        Gets the block_error_page_description of this BlockChallengeSettings.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`


        :return: The block_error_page_description of this BlockChallengeSettings.
        :rtype: str
        """
        return self._block_error_page_description

    @block_error_page_description.setter
    def block_error_page_description(self, block_error_page_description):
        """
        Sets the block_error_page_description of this BlockChallengeSettings.
        The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`


        :param block_error_page_description: The block_error_page_description of this BlockChallengeSettings.
        :type: str
        """
        self._block_error_page_description = block_error_page_description

    @property
    def block_error_page_code(self):
        """
        Gets the block_error_page_code of this BlockChallengeSettings.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.


        :return: The block_error_page_code of this BlockChallengeSettings.
        :rtype: str
        """
        return self._block_error_page_code

    @block_error_page_code.setter
    def block_error_page_code(self, block_error_page_code):
        """
        Sets the block_error_page_code of this BlockChallengeSettings.
        The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and the request is blocked. If unspecified, defaults to `403`.


        :param block_error_page_code: The block_error_page_code of this BlockChallengeSettings.
        :type: str
        """
        self._block_error_page_code = block_error_page_code

    @property
    def captcha_title(self):
        """
        Gets the captcha_title of this BlockChallengeSettings.
        The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`


        :return: The captcha_title of this BlockChallengeSettings.
        :rtype: str
        """
        return self._captcha_title

    @captcha_title.setter
    def captcha_title(self, captcha_title):
        """
        Sets the captcha_title of this BlockChallengeSettings.
        The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`


        :param captcha_title: The captcha_title of this BlockChallengeSettings.
        :type: str
        """
        self._captcha_title = captcha_title

    @property
    def captcha_header(self):
        """
        Gets the captcha_header of this BlockChallengeSettings.
        The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`


        :return: The captcha_header of this BlockChallengeSettings.
        :rtype: str
        """
        return self._captcha_header

    @captcha_header.setter
    def captcha_header(self, captcha_header):
        """
        Sets the captcha_header of this BlockChallengeSettings.
        The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the text from captcha below.`


        :param captcha_header: The captcha_header of this BlockChallengeSettings.
        :type: str
        """
        self._captcha_header = captcha_header

    @property
    def captcha_footer(self):
        """
        Gets the captcha_footer of this BlockChallengeSettings.
        The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.


        :return: The captcha_footer of this BlockChallengeSettings.
        :rtype: str
        """
        return self._captcha_footer

    @captcha_footer.setter
    def captcha_footer(self, captcha_footer):
        """
        Sets the captcha_footer of this BlockChallengeSettings.
        The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in image above`.


        :param captcha_footer: The captcha_footer of this BlockChallengeSettings.
        :type: str
        """
        self._captcha_footer = captcha_footer

    @property
    def captcha_submit_label(self):
        """
        Gets the captcha_submit_label of this BlockChallengeSettings.
        The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.


        :return: The captcha_submit_label of this BlockChallengeSettings.
        :rtype: str
        """
        return self._captcha_submit_label

    @captcha_submit_label.setter
    def captcha_submit_label(self, captcha_submit_label):
        """
        Sets the captcha_submit_label of this BlockChallengeSettings.
        The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.


        :param captcha_submit_label: The captcha_submit_label of this BlockChallengeSettings.
        :type: str
        """
        self._captcha_submit_label = captcha_submit_label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
