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

from openapi_client.models.limits_v1_data import LimitsV1Data

class TestLimitsV1Data(unittest.TestCase):
    """LimitsV1Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LimitsV1Data:
        """Test LimitsV1Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LimitsV1Data`
        """
        model = LimitsV1Data()
        if include_optional:
            return LimitsV1Data(
                total_credits = 1.337,
                avail_margin = 1.337,
                margin_used = 1.337,
                detailed_view = [
                    openapi_client.models.detailed_view.DetailedView(
                        title = '', 
                        val = 1.337, 
                        details = [
                            openapi_client.models.values.Values(
                                key = '', 
                                value = 1.337, )
                            ], )
                    ]
            )
        else:
            return LimitsV1Data(
        )
        """

    def testLimitsV1Data(self):
        """Test LimitsV1Data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
