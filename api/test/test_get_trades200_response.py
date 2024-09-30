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

from openapi_client.models.get_trades200_response import GetTrades200Response

class TestGetTrades200Response(unittest.TestCase):
    """GetTrades200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTrades200Response:
        """Test GetTrades200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTrades200Response`
        """
        model = GetTrades200Response()
        if include_optional:
            return GetTrades200Response(
                s = '',
                d = [
                    openapi_client.models.trade_record.TradeRecord(
                        sym_id = '', 
                        side = 'buy', 
                        type = 'limit', 
                        validity = 'day', 
                        product = 'delivery', 
                        order_id = '', 
                        fill_id = '', 
                        fill_qty = 1.337, 
                        fill_price = 1.337, 
                        fill_value = 1.337, 
                        time = '', 
                        exch_order_id = '', 
                        avg_price = 1.337, 
                        sym = {
                            'key' : None
                            }, 
                        remarks = '', 
                        leg_type = '', 
                        main_leg_order_id = '', )
                    ],
                msg = ''
            )
        else:
            return GetTrades200Response(
        )
        """

    def testGetTrades200Response(self):
        """Test GetTrades200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
