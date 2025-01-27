# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.auditregistration_v1alpha1_api import AuditregistrationV1alpha1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestAuditregistrationV1alpha1Api(unittest.TestCase):
    """AuditregistrationV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.auditregistration_v1alpha1_api.AuditregistrationV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_audit_sink(self):
        """Test case for create_audit_sink

        """
        pass

    def test_delete_audit_sink(self):
        """Test case for delete_audit_sink

        """
        pass

    def test_delete_collection_audit_sink(self):
        """Test case for delete_collection_audit_sink

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_audit_sink(self):
        """Test case for list_audit_sink

        """
        pass

    def test_patch_audit_sink(self):
        """Test case for patch_audit_sink

        """
        pass

    def test_read_audit_sink(self):
        """Test case for read_audit_sink

        """
        pass

    def test_replace_audit_sink(self):
        """Test case for replace_audit_sink

        """
        pass


if __name__ == '__main__':
    unittest.main()
