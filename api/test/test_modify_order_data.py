# coding: utf-8

"""
    CubePlus Rest API Specifications

    Gateway API's

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.modify_order_data import ModifyOrderData

class TestModifyOrderData(unittest.TestCase):
    """ModifyOrderData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifyOrderData:
        """Test ModifyOrderData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifyOrderData`
        """
        model = ModifyOrderData()
        if include_optional:
            return ModifyOrderData(
                msg = '',
                order_id = ''
            )
        else:
            return ModifyOrderData(
        )
        """

    def testModifyOrderData(self):
        """Test ModifyOrderData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
