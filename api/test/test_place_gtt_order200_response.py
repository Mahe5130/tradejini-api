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

from openapi_client.models.place_gtt_order200_response import PlaceGTTOrder200Response

class TestPlaceGTTOrder200Response(unittest.TestCase):
    """PlaceGTTOrder200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaceGTTOrder200Response:
        """Test PlaceGTTOrder200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaceGTTOrder200Response`
        """
        model = PlaceGTTOrder200Response()
        if include_optional:
            return PlaceGTTOrder200Response(
                s = '',
                d = openapi_client.models.place_gtt_order_data.PlaceGTTOrderData(
                    msg = '', 
                    order_id = '', ),
                msg = ''
            )
        else:
            return PlaceGTTOrder200Response(
        )
        """

    def testPlaceGTTOrder200Response(self):
        """Test PlaceGTTOrder200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
