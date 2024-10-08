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

from openapi_client.models.modify_oco_order200_response import ModifyOCOOrder200Response

class TestModifyOCOOrder200Response(unittest.TestCase):
    """ModifyOCOOrder200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifyOCOOrder200Response:
        """Test ModifyOCOOrder200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifyOCOOrder200Response`
        """
        model = ModifyOCOOrder200Response()
        if include_optional:
            return ModifyOCOOrder200Response(
                s = '',
                d = openapi_client.models.modify_oco_order_data.ModifyOCOOrderData(
                    msg = '', 
                    order_id = '', ),
                msg = ''
            )
        else:
            return ModifyOCOOrder200Response(
        )
        """

    def testModifyOCOOrder200Response(self):
        """Test ModifyOCOOrder200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
