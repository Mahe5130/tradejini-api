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

from openapi_client.models.cancel_gtt_order200_response import CancelGTTOrder200Response

class TestCancelGTTOrder200Response(unittest.TestCase):
    """CancelGTTOrder200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CancelGTTOrder200Response:
        """Test CancelGTTOrder200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CancelGTTOrder200Response`
        """
        model = CancelGTTOrder200Response()
        if include_optional:
            return CancelGTTOrder200Response(
                s = '',
                d = openapi_client.models.cancel_gtt_order_data.CancelGTTOrderData(
                    msg = '', 
                    order_id = '', ),
                msg = ''
            )
        else:
            return CancelGTTOrder200Response(
        )
        """

    def testCancelGTTOrder200Response(self):
        """Test CancelGTTOrder200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
