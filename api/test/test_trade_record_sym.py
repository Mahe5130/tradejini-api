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

from openapi_client.models.trade_record_sym import TradeRecordSym

class TestTradeRecordSym(unittest.TestCase):
    """TradeRecordSym unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TradeRecordSym:
        """Test TradeRecordSym
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TradeRecordSym`
        """
        model = TradeRecordSym()
        if include_optional:
            return TradeRecordSym(
                id = '',
                symbol = '',
                trad_symbol = '',
                exchange = '',
                lot = '',
                instrument = '',
                company_name = '',
                expiry = '',
                disp_symbol = '',
                asset = '',
                empty = True
            )
        else:
            return TradeRecordSym(
        )
        """

    def testTradeRecordSym(self):
        """Test TradeRecordSym"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
