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

from openapi_client.models.trailing_order_record import TrailingOrderRecord

class TestTrailingOrderRecord(unittest.TestCase):
    """TrailingOrderRecord unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrailingOrderRecord:
        """Test TrailingOrderRecord
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrailingOrderRecord`
        """
        model = TrailingOrderRecord()
        if include_optional:
            return TrailingOrderRecord(
                sym_id = '',
                order_id = '',
                side = 'buy',
                type = 'limit',
                product = 'delivery',
                validity = 'day',
                qty = 1.337,
                limit_price = 1.337,
                target_price = 1.337,
                trailing_stop_price = 1.337,
                reason = '',
                price_factor = 1.337,
                multiplier = 1.337,
                trig_price = 1.337,
                status = ''
            )
        else:
            return TrailingOrderRecord(
        )
        """

    def testTrailingOrderRecord(self):
        """Test TrailingOrderRecord"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
