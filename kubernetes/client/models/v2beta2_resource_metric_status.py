# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V2beta2ResourceMetricStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'current': 'V2beta2MetricValueStatus',
        'name': 'str'
    }

    attribute_map = {
        'current': 'current',
        'name': 'name'
    }

    def __init__(self, current=None, name=None):  # noqa: E501
        """V2beta2ResourceMetricStatus - a model defined in OpenAPI"""  # noqa: E501

        self._current = None
        self._name = None
        self.discriminator = None

        self.current = current
        self.name = name

    @property
    def current(self):
        """Gets the current of this V2beta2ResourceMetricStatus.  # noqa: E501


        :return: The current of this V2beta2ResourceMetricStatus.  # noqa: E501
        :rtype: V2beta2MetricValueStatus
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this V2beta2ResourceMetricStatus.


        :param current: The current of this V2beta2ResourceMetricStatus.  # noqa: E501
        :type: V2beta2MetricValueStatus
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")  # noqa: E501

        self._current = current

    @property
    def name(self):
        """Gets the name of this V2beta2ResourceMetricStatus.  # noqa: E501

        Name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta2ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2beta2ResourceMetricStatus.

        Name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta2ResourceMetricStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta2ResourceMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
