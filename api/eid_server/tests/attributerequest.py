from django.test import TestCase
from eid_server.eid_types.attributerequest import AttributeRequest


class AttributeRequestTests(TestCase):

    VALID_REQUEST_STRING_ALLOWED = "ALLOWED"
    VALID_REQUEST_STRING_PROHIBITED = "PROHIBITED"
    VALID_REQUEST_STRING_REQUIRED = "REQUIRED"

    def test_valid_attributerequest_allowed(self):
        request = AttributeRequest(self.VALID_REQUEST_STRING_ALLOWED)
        r = request.request

        self.assertEqual(r, self.VALID_REQUEST_STRING_ALLOWED)

    def test_valid_attributerequest_prohibited(self):
        request = AttributeRequest(self.VALID_REQUEST_STRING_PROHIBITED)
        r = request.request

        self.assertEqual(r, self.VALID_REQUEST_STRING_PROHIBITED)

    def test_valid_attributerequest_required(self):
        request = AttributeRequest(self.VALID_REQUEST_STRING_REQUIRED)
        r = request.request

        self.assertEqual(r, self.VALID_REQUEST_STRING_REQUIRED)

    def test_attributerequest_raise_if_empty_request(self):
        with self.assertRaises(TypeError):
            AttributeRequest("")

    def test_attributerequest_raise_if_none_request(self):
        with self.assertRaises(TypeError):
            AttributeRequest(None)

    def test_attributerequest_raise_if_invalid_request(self):
        with self.assertRaises(TypeError):
            AttributeRequest("TEST")

    def test_attributerequest_raise_if_int(self):
        with self.assertRaises(TypeError):
            AttributeRequest(2)

