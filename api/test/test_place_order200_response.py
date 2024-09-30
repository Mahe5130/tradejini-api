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

from openapi_client.models.place_order200_response import PlaceOrder200Response

class TestPlaceOrder200Response(unittest.TestCase):
    """PlaceOrder200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaceOrder200Response:
        """Test PlaceOrder200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaceOrder200Response`
        """
        model = PlaceOrder200Response()
        if include_optional:
            return PlaceOrder200Response(
                s = 'ok',
                d = openapi_client.models.place_order_data.PlaceOrderData(
                    msg = '', 
                    order_id = '', ),
                msg = ''
            )
        else:
            return PlaceOrder200Response(
        )
        """

    def testPlaceOrder200Response(self):
        """Test PlaceOrder200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
