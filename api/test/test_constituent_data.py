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

from openapi_client.models.constituent_data import ConstituentData

class TestConstituentData(unittest.TestCase):
    """ConstituentData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConstituentData:
        """Test ConstituentData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConstituentData`
        """
        model = ConstituentData()
        if include_optional:
            return ConstituentData(
                id = '',
                change_per = 1.337,
                weightage = 1.337,
                contribution_point = 1.337
            )
        else:
            return ConstituentData(
        )
        """

    def testConstituentData(self):
        """Test ConstituentData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
