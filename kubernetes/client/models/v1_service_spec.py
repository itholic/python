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


class V1ServiceSpec(object):
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
        'cluster_ip': 'str',
        'external_i_ps': 'list[str]',
        'external_name': 'str',
        'external_traffic_policy': 'str',
        'health_check_node_port': 'int',
        'load_balancer_ip': 'str',
        'load_balancer_source_ranges': 'list[str]',
        'ports': 'list[V1ServicePort]',
        'publish_not_ready_addresses': 'bool',
        'selector': 'dict(str, str)',
        'session_affinity': 'str',
        'session_affinity_config': 'V1SessionAffinityConfig',
        'type': 'str'
    }

    attribute_map = {
        'cluster_ip': 'clusterIP',
        'external_i_ps': 'externalIPs',
        'external_name': 'externalName',
        'external_traffic_policy': 'externalTrafficPolicy',
        'health_check_node_port': 'healthCheckNodePort',
        'load_balancer_ip': 'loadBalancerIP',
        'load_balancer_source_ranges': 'loadBalancerSourceRanges',
        'ports': 'ports',
        'publish_not_ready_addresses': 'publishNotReadyAddresses',
        'selector': 'selector',
        'session_affinity': 'sessionAffinity',
        'session_affinity_config': 'sessionAffinityConfig',
        'type': 'type'
    }

    def __init__(self, cluster_ip=None, external_i_ps=None, external_name=None, external_traffic_policy=None, health_check_node_port=None, load_balancer_ip=None, load_balancer_source_ranges=None, ports=None, publish_not_ready_addresses=None, selector=None, session_affinity=None, session_affinity_config=None, type=None):  # noqa: E501
        """V1ServiceSpec - a model defined in OpenAPI"""  # noqa: E501

        self._cluster_ip = None
        self._external_i_ps = None
        self._external_name = None
        self._external_traffic_policy = None
        self._health_check_node_port = None
        self._load_balancer_ip = None
        self._load_balancer_source_ranges = None
        self._ports = None
        self._publish_not_ready_addresses = None
        self._selector = None
        self._session_affinity = None
        self._session_affinity_config = None
        self._type = None
        self.discriminator = None

        if cluster_ip is not None:
            self.cluster_ip = cluster_ip
        if external_i_ps is not None:
            self.external_i_ps = external_i_ps
        if external_name is not None:
            self.external_name = external_name
        if external_traffic_policy is not None:
            self.external_traffic_policy = external_traffic_policy
        if health_check_node_port is not None:
            self.health_check_node_port = health_check_node_port
        if load_balancer_ip is not None:
            self.load_balancer_ip = load_balancer_ip
        if load_balancer_source_ranges is not None:
            self.load_balancer_source_ranges = load_balancer_source_ranges
        if ports is not None:
            self.ports = ports
        if publish_not_ready_addresses is not None:
            self.publish_not_ready_addresses = publish_not_ready_addresses
        if selector is not None:
            self.selector = selector
        if session_affinity is not None:
            self.session_affinity = session_affinity
        if session_affinity_config is not None:
            self.session_affinity_config = session_affinity_config
        if type is not None:
            self.type = type

    @property
    def cluster_ip(self):
        """Gets the cluster_ip of this V1ServiceSpec.  # noqa: E501

        clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are \"None\", empty string (\"\"), or a valid IP address. \"None\" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :return: The cluster_ip of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """Sets the cluster_ip of this V1ServiceSpec.

        clusterIP is the IP address of the service and is usually assigned randomly by the master. If an address is specified manually and is not in use by others, it will be allocated to the service; otherwise, creation of the service will fail. This field can not be changed through updates. Valid values are \"None\", empty string (\"\"), or a valid IP address. \"None\" can be specified for headless services when proxying is not required. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :param cluster_ip: The cluster_ip of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._cluster_ip = cluster_ip

    @property
    def external_i_ps(self):
        """Gets the external_i_ps of this V1ServiceSpec.  # noqa: E501

        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  # noqa: E501

        :return: The external_i_ps of this V1ServiceSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_i_ps

    @external_i_ps.setter
    def external_i_ps(self, external_i_ps):
        """Sets the external_i_ps of this V1ServiceSpec.

        externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.  # noqa: E501

        :param external_i_ps: The external_i_ps of this V1ServiceSpec.  # noqa: E501
        :type: list[str]
        """

        self._external_i_ps = external_i_ps

    @property
    def external_name(self):
        """Gets the external_name of this V1ServiceSpec.  # noqa: E501

        externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires Type to be ExternalName.  # noqa: E501

        :return: The external_name of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this V1ServiceSpec.

        externalName is the external reference that kubedns or equivalent will return as a CNAME record for this service. No proxying will be involved. Must be a valid RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires Type to be ExternalName.  # noqa: E501

        :param external_name: The external_name of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._external_name = external_name

    @property
    def external_traffic_policy(self):
        """Gets the external_traffic_policy of this V1ServiceSpec.  # noqa: E501

        externalTrafficPolicy denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. \"Local\" preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. \"Cluster\" obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading.  # noqa: E501

        :return: The external_traffic_policy of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._external_traffic_policy

    @external_traffic_policy.setter
    def external_traffic_policy(self, external_traffic_policy):
        """Sets the external_traffic_policy of this V1ServiceSpec.

        externalTrafficPolicy denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. \"Local\" preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. \"Cluster\" obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading.  # noqa: E501

        :param external_traffic_policy: The external_traffic_policy of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._external_traffic_policy = external_traffic_policy

    @property
    def health_check_node_port(self):
        """Gets the health_check_node_port of this V1ServiceSpec.  # noqa: E501

        healthCheckNodePort specifies the healthcheck nodePort for the service. If not specified, HealthCheckNodePort is created by the service api backend with the allocated nodePort. Will use user-specified nodePort value if specified by the client. Only effects when Type is set to LoadBalancer and ExternalTrafficPolicy is set to Local.  # noqa: E501

        :return: The health_check_node_port of this V1ServiceSpec.  # noqa: E501
        :rtype: int
        """
        return self._health_check_node_port

    @health_check_node_port.setter
    def health_check_node_port(self, health_check_node_port):
        """Sets the health_check_node_port of this V1ServiceSpec.

        healthCheckNodePort specifies the healthcheck nodePort for the service. If not specified, HealthCheckNodePort is created by the service api backend with the allocated nodePort. Will use user-specified nodePort value if specified by the client. Only effects when Type is set to LoadBalancer and ExternalTrafficPolicy is set to Local.  # noqa: E501

        :param health_check_node_port: The health_check_node_port of this V1ServiceSpec.  # noqa: E501
        :type: int
        """

        self._health_check_node_port = health_check_node_port

    @property
    def load_balancer_ip(self):
        """Gets the load_balancer_ip of this V1ServiceSpec.  # noqa: E501

        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.  # noqa: E501

        :return: The load_balancer_ip of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_ip

    @load_balancer_ip.setter
    def load_balancer_ip(self, load_balancer_ip):
        """Sets the load_balancer_ip of this V1ServiceSpec.

        Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.  # noqa: E501

        :param load_balancer_ip: The load_balancer_ip of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._load_balancer_ip = load_balancer_ip

    @property
    def load_balancer_source_ranges(self):
        """Gets the load_balancer_source_ranges of this V1ServiceSpec.  # noqa: E501

        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/  # noqa: E501

        :return: The load_balancer_source_ranges of this V1ServiceSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_source_ranges

    @load_balancer_source_ranges.setter
    def load_balancer_source_ranges(self, load_balancer_source_ranges):
        """Sets the load_balancer_source_ranges of this V1ServiceSpec.

        If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature.\" More info: https://kubernetes.io/docs/tasks/access-application-cluster/configure-cloud-provider-firewall/  # noqa: E501

        :param load_balancer_source_ranges: The load_balancer_source_ranges of this V1ServiceSpec.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_source_ranges = load_balancer_source_ranges

    @property
    def ports(self):
        """Gets the ports of this V1ServiceSpec.  # noqa: E501

        The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :return: The ports of this V1ServiceSpec.  # noqa: E501
        :rtype: list[V1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this V1ServiceSpec.

        The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :param ports: The ports of this V1ServiceSpec.  # noqa: E501
        :type: list[V1ServicePort]
        """

        self._ports = ports

    @property
    def publish_not_ready_addresses(self):
        """Gets the publish_not_ready_addresses of this V1ServiceSpec.  # noqa: E501

        publishNotReadyAddresses, when set to true, indicates that DNS implementations must publish the notReadyAddresses of subsets for the Endpoints associated with the Service. The default value is false. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate SRV records for its Pods without respect to their readiness for purpose of peer discovery.  # noqa: E501

        :return: The publish_not_ready_addresses of this V1ServiceSpec.  # noqa: E501
        :rtype: bool
        """
        return self._publish_not_ready_addresses

    @publish_not_ready_addresses.setter
    def publish_not_ready_addresses(self, publish_not_ready_addresses):
        """Sets the publish_not_ready_addresses of this V1ServiceSpec.

        publishNotReadyAddresses, when set to true, indicates that DNS implementations must publish the notReadyAddresses of subsets for the Endpoints associated with the Service. The default value is false. The primary use case for setting this field is to use a StatefulSet's Headless Service to propagate SRV records for its Pods without respect to their readiness for purpose of peer discovery.  # noqa: E501

        :param publish_not_ready_addresses: The publish_not_ready_addresses of this V1ServiceSpec.  # noqa: E501
        :type: bool
        """

        self._publish_not_ready_addresses = publish_not_ready_addresses

    @property
    def selector(self):
        """Gets the selector of this V1ServiceSpec.  # noqa: E501

        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/  # noqa: E501

        :return: The selector of this V1ServiceSpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1ServiceSpec.

        Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/  # noqa: E501

        :param selector: The selector of this V1ServiceSpec.  # noqa: E501
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def session_affinity(self):
        """Gets the session_affinity of this V1ServiceSpec.  # noqa: E501

        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :return: The session_affinity of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        """Sets the session_affinity of this V1ServiceSpec.

        Supports \"ClientIP\" and \"None\". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies  # noqa: E501

        :param session_affinity: The session_affinity of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._session_affinity = session_affinity

    @property
    def session_affinity_config(self):
        """Gets the session_affinity_config of this V1ServiceSpec.  # noqa: E501


        :return: The session_affinity_config of this V1ServiceSpec.  # noqa: E501
        :rtype: V1SessionAffinityConfig
        """
        return self._session_affinity_config

    @session_affinity_config.setter
    def session_affinity_config(self, session_affinity_config):
        """Sets the session_affinity_config of this V1ServiceSpec.


        :param session_affinity_config: The session_affinity_config of this V1ServiceSpec.  # noqa: E501
        :type: V1SessionAffinityConfig
        """

        self._session_affinity_config = session_affinity_config

    @property
    def type(self):
        """Gets the type of this V1ServiceSpec.  # noqa: E501

        type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. \"ExternalName\" maps to the specified externalName. \"ClusterIP\" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is \"None\", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. \"NodePort\" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. \"LoadBalancer\" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types  # noqa: E501

        :return: The type of this V1ServiceSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1ServiceSpec.

        type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. \"ExternalName\" maps to the specified externalName. \"ClusterIP\" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object. If clusterIP is \"None\", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a stable IP. \"NodePort\" builds on ClusterIP and allocates a port on every node which routes to the clusterIP. \"LoadBalancer\" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the clusterIP. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types  # noqa: E501

        :param type: The type of this V1ServiceSpec.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, V1ServiceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
