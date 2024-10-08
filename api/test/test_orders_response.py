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

from openapi_client.models.orders_response import OrdersResponse

class TestOrdersResponse(unittest.TestCase):
    """OrdersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrdersResponse:
        """Test OrdersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrdersResponse`
        """
        model = OrdersResponse()
        if include_optional:
            return OrdersResponse(
                s = 'ok',
                d = [
                    openapi_client.models.order_record.OrderRecord(
                        sym_id = '', 
                        status = 'open', 
                        qty = 1.337, 
                        side = 'buy', 
                        type = 'limit', 
                        validity = 'day', 
                        source = '', 
                        limit_price = 1.337, 
                        exch_order_id = '', 
                        disc_qty = 1.337, 
                        product = 'delivery', 
                        exch_time = '', 
                        order_id = '', 
                        order_time = '', 
                        avg_price = 1.337, 
                        amo = True, 
                        fill_qty = 1.337, 
                        trig_price = 1.337, 
                        reason = '', 
                        pending_qty = 1.337, 
                        sym = {
                            'key' : None
                            }, 
                        mkt_prot = 1.337, 
                        stop_trig_price = 1.337, 
                        target_price = 1.337, 
                        trailing_stop_price = 1.337, 
                        remarks = '', 
                        leg_type = 'main', 
                        main_leg_order_id = '', 
                        order_value = 1.337, 
                        trade_value = 1.337, 
                        alg_type = 'trailing', 
                        modifiable = True, 
                        cancellable = True, 
                        exitable = True, )
                    ]
            )
        else:
            return OrdersResponse(
        )
        """

    def testOrdersResponse(self):
        """Test OrdersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
