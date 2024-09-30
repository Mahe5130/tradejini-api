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

from openapi_client.models.chart_resp import ChartResp

class TestChartResp(unittest.TestCase):
    """ChartResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChartResp:
        """Test ChartResp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChartResp`
        """
        model = ChartResp()
        if include_optional:
            return ChartResp(
                s = 'ok',
                d = openapi_client.models.chart_data_points_chart_points.ChartDataPointsChartPoints(
                    bars = [
                        [
                            openapi_client.models.chart_points.ChartPoints(
                                time = 56, 
                                open = 1.337, 
                                high = 1.337, 
                                low = 1.337, 
                                close = 1.337, 
                                volume = 56, 
                                minute_oi = 56, )
                            ]
                        ], 
                    sum_up_volume = 56, )
            )
        else:
            return ChartResp(
        )
        """

    def testChartResp(self):
        """Test ChartResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
