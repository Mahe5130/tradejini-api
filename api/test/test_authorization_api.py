# coding: utf-8

"""
    CubePlus Rest API Specifications

    Gateway API's

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.authorization_api import AuthorizationApi


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthorizationApi()

    def tearDown(self) -> None:
        pass

    def test_authorize(self) -> None:
        """Test case for authorize

        Authorize
        """
        pass

    def test_get_access_token(self) -> None:
        """Test case for get_access_token

        Access token
        """
        pass

    def test_order_authorize(self) -> None:
        """Test case for order_authorize

        Order Connect [Offsite Orders]
        """
        pass

    def test_updated_individual_token(self) -> None:
        """Test case for updated_individual_token

        Individual Token service
        """
        pass


if __name__ == '__main__':
    unittest.main()
