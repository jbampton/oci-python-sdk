# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChatResult(object):
    """
    The response of a chat request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChatResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this ChatResult.
        :type message: oci.generative_ai_agent_runtime.models.Message

        :param traces:
            The value to assign to the traces property of this ChatResult.
        :type traces: list[oci.generative_ai_agent_runtime.models.Trace]

        :param tool_results:
            The value to assign to the tool_results property of this ChatResult.
        :type tool_results: dict(str, str)

        :param required_actions:
            The value to assign to the required_actions property of this ChatResult.
        :type required_actions: list[oci.generative_ai_agent_runtime.models.RequiredAction]

        :param guardrail_result:
            The value to assign to the guardrail_result property of this ChatResult.
        :type guardrail_result: str

        """
        self.swagger_types = {
            'message': 'Message',
            'traces': 'list[Trace]',
            'tool_results': 'dict(str, str)',
            'required_actions': 'list[RequiredAction]',
            'guardrail_result': 'str'
        }
        self.attribute_map = {
            'message': 'message',
            'traces': 'traces',
            'tool_results': 'toolResults',
            'required_actions': 'requiredActions',
            'guardrail_result': 'guardrailResult'
        }
        self._message = None
        self._traces = None
        self._tool_results = None
        self._required_actions = None
        self._guardrail_result = None

    @property
    def message(self):
        """
        Gets the message of this ChatResult.

        :return: The message of this ChatResult.
        :rtype: oci.generative_ai_agent_runtime.models.Message
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ChatResult.

        :param message: The message of this ChatResult.
        :type: oci.generative_ai_agent_runtime.models.Message
        """
        self._message = message

    @property
    def traces(self):
        """
        Gets the traces of this ChatResult.
        The trace that displays the internal progression, such as reasoning and actions during an execution.


        :return: The traces of this ChatResult.
        :rtype: list[oci.generative_ai_agent_runtime.models.Trace]
        """
        return self._traces

    @traces.setter
    def traces(self, traces):
        """
        Sets the traces of this ChatResult.
        The trace that displays the internal progression, such as reasoning and actions during an execution.


        :param traces: The traces of this ChatResult.
        :type: list[oci.generative_ai_agent_runtime.models.Trace]
        """
        self._traces = traces

    @property
    def tool_results(self):
        """
        Gets the tool_results of this ChatResult.
        A map where each key is a toolId and the value contains tool type and additional dynamic results.


        :return: The tool_results of this ChatResult.
        :rtype: dict(str, str)
        """
        return self._tool_results

    @tool_results.setter
    def tool_results(self, tool_results):
        """
        Sets the tool_results of this ChatResult.
        A map where each key is a toolId and the value contains tool type and additional dynamic results.


        :param tool_results: The tool_results of this ChatResult.
        :type: dict(str, str)
        """
        self._tool_results = tool_results

    @property
    def required_actions(self):
        """
        Gets the required_actions of this ChatResult.
        A list of actions the agent requires the user or agent client to perform.


        :return: The required_actions of this ChatResult.
        :rtype: list[oci.generative_ai_agent_runtime.models.RequiredAction]
        """
        return self._required_actions

    @required_actions.setter
    def required_actions(self, required_actions):
        """
        Sets the required_actions of this ChatResult.
        A list of actions the agent requires the user or agent client to perform.


        :param required_actions: The required_actions of this ChatResult.
        :type: list[oci.generative_ai_agent_runtime.models.RequiredAction]
        """
        self._required_actions = required_actions

    @property
    def guardrail_result(self):
        """
        Gets the guardrail_result of this ChatResult.
        Captures the result of guardrail evaluations as JSON string performed on either the input to the agent or the output generated by the agent.


        :return: The guardrail_result of this ChatResult.
        :rtype: str
        """
        return self._guardrail_result

    @guardrail_result.setter
    def guardrail_result(self, guardrail_result):
        """
        Sets the guardrail_result of this ChatResult.
        Captures the result of guardrail evaluations as JSON string performed on either the input to the agent or the output generated by the agent.


        :param guardrail_result: The guardrail_result of this ChatResult.
        :type: str
        """
        self._guardrail_result = guardrail_result

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
