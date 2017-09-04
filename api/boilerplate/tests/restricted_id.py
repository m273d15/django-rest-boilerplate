from django.test import TestCase
from boilerplate.eid_types.restricted_id import HexBinary, RestrictedId


class RestrictedIdTests(TestCase):

    VALID_HEX_STRING = "3fc1a8"
    VALID_HEX_STRING2 = "fc1a83"
    VALID_HEX_BINARY = HexBinary(VALID_HEX_STRING)
    VALID_HEX_BINARY2 = HexBinary(VALID_HEX_STRING2)

    def test_valid_restricted_id_without_id2(self):
        r_id = RestrictedId(self.VALID_HEX_BINARY)
        self.assertEqual(r_id.id.hex_string, self.VALID_HEX_STRING)
        
    def test_valid_restricted_id_with_id2(self):
        r_id = RestrictedId(self.VALID_HEX_BINARY, self.VALID_HEX_BINARY2)
        self.assertEqual(r_id.id.hex_string, self.VALID_HEX_STRING)
        self.assertEqual(r_id.id2.hex_string, self.VALID_HEX_STRING2)
 
