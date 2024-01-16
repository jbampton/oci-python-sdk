# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180401

from .alarm_suppression_target import AlarmSuppressionTarget
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlarmSuppressionAlarmTarget(AlarmSuppressionTarget):
    """
    The alarm target of the alarm suppression.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlarmSuppressionAlarmTarget object with values from keyword arguments. The default value of the :py:attr:`~oci.monitoring.models.AlarmSuppressionAlarmTarget.target_type` attribute
        of this class is ``ALARM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_type:
            The value to assign to the target_type property of this AlarmSuppressionAlarmTarget.
            Allowed values for this property are: "ALARM"
        :type target_type: str

        :param alarm_id:
            The value to assign to the alarm_id property of this AlarmSuppressionAlarmTarget.
        :type alarm_id: str

        """
        self.swagger_types = {
            'target_type': 'str',
            'alarm_id': 'str'
        }

        self.attribute_map = {
            'target_type': 'targetType',
            'alarm_id': 'alarmId'
        }

        self._target_type = None
        self._alarm_id = None
        self._target_type = 'ALARM'

    @property
    def alarm_id(self):
        """
        **[Required]** Gets the alarm_id of this AlarmSuppressionAlarmTarget.
        The `OCID`__ of the alarm that is the target of the alarm suppression.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The alarm_id of this AlarmSuppressionAlarmTarget.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """
        Sets the alarm_id of this AlarmSuppressionAlarmTarget.
        The `OCID`__ of the alarm that is the target of the alarm suppression.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param alarm_id: The alarm_id of this AlarmSuppressionAlarmTarget.
        :type: str
        """
        self._alarm_id = alarm_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
