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

from openapi_client.models.price_shocker import PriceShocker

class TestPriceShocker(unittest.TestCase):
    """PriceShocker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceShocker:
        """Test PriceShocker
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceShocker`
        """
        model = PriceShocker()
        if include_optional:
            return PriceShocker(
                id = '',
                change_per = '',
                avg_price = ''
            )
        else:
            return PriceShocker(
        )
        """

    def testPriceShocker(self):
        """Test PriceShocker"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
