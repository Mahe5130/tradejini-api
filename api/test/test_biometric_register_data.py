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

from openapi_client.models.biometric_register_data import BiometricRegisterData

class TestBiometricRegisterData(unittest.TestCase):
    """BiometricRegisterData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BiometricRegisterData:
        """Test BiometricRegisterData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BiometricRegisterData`
        """
        model = BiometricRegisterData()
        if include_optional:
            return BiometricRegisterData(
                msg = '',
                biometric_id = ''
            )
        else:
            return BiometricRegisterData(
        )
        """

    def testBiometricRegisterData(self):
        """Test BiometricRegisterData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
