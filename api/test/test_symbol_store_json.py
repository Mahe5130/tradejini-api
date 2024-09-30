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

from openapi_client.models.symbol_store_json import SymbolStoreJson

class TestSymbolStoreJson(unittest.TestCase):
    """SymbolStoreJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SymbolStoreJson:
        """Test SymbolStoreJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SymbolStoreJson`
        """
        model = SymbolStoreJson()
        if include_optional:
            return SymbolStoreJson(
                id = '',
                isin = '',
                disp_name = '',
                desc = '',
                exc_token = '',
                lot = '',
                tick = '',
                expiry = '',
                strike = '',
                opt_type = '',
                weekly = '',
                asset = '',
                instrument = '',
                symbol = '',
                series = '',
                exchange = '',
                freeze_qty = '',
                und_id = '',
                trd_unit = '',
                lot_multi = ''
            )
        else:
            return SymbolStoreJson(
        )
        """

    def testSymbolStoreJson(self):
        """Test SymbolStoreJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
