from django.test import TestCase
from boilerplate.eid_types.attributeresponse import *


class AttributeResponseTests(TestCase):

    VALID_RESPONSE_ALLOWED = "ALLOWED"
    VALID_RESPONSE_PROHIBITED = "PROHIBITED"
    VALID_RESPONSE_NOTONCHIP = "NOTONCHIP"

    def test_valid_attributeresponse_allowed(self):
        response = AttributeResponse(self.VALID_RESPONSE_ALLOWED)
        r = response.response

        self.assertEqual(r, self.VALID_RESPONSE_ALLOWED)

    def test_valid_attributeresponse_prohibited(self):
        response = AttributeResponse(self.VALID_RESPONSE_PROHIBITED)
        r = response.response

        self.assertEqual(r, self.VALID_RESPONSE_PROHIBITED)

    def test_valid_attributeresponse_notonchip(self):
        response = AttributeResponse(self.VALID_RESPONSE_NOTONCHIP)
        r = response.response

        self.assertEqual(r, self.VALID_RESPONSE_NOTONCHIP)

    def test_attributeresponse_raise_if_empty_response(self):
        with self.assertRaises(TypeError):
            AttributeResponse("")

    def test_attributeresponse_raise_if_none_response(self):
        with self.assertRaises(TypeError):
            AttributeResponse(None)

    def test_attributeresponse_raise_if_invalid_selection(self):
        with self.assertRaises(TypeError):
            AttributeResponse("foo")
        
    def test_attributeresponse_raise_if_invalid_datatype(self):
        with self.assertRaises(TypeError):
            AttributeResponse(1)

