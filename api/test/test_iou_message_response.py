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

from openapi_client.models.iou_message_response import IouMessageResponse

class TestIouMessageResponse(unittest.TestCase):
    """IouMessageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IouMessageResponse:
        """Test IouMessageResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IouMessageResponse`
        """
        model = IouMessageResponse()
        if include_optional:
            return IouMessageResponse(
                msg = '',
                s = ''
            )
        else:
            return IouMessageResponse(
        )
        """

    def testIouMessageResponse(self):
        """Test IouMessageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
