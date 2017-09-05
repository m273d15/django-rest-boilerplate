from django.test import TestCase
from eid_server.eid_types.hexbinary import *


class HexBinaryTests(TestCase):

    VALID_HEX_STRING = "3fc1a8"

    def test_valid_hex_bin(self):
        hex_bin = HexBinary(self.VALID_HEX_STRING)
        self.assertEqual(hex_bin.hex_string, self.VALID_HEX_STRING)            

    def test_invalid_hex_bin_odd_size_string(self):
        with self.assertRaises(TypeError):
            HexBinary("33a")

    def test_invalid_hex_bin_invalid_alphabet(self):
        with self.assertRaises(TypeError):
            HexBinary("33g")


class HexBinary16Tests(TestCase):

    VALID_HEX_STRING16 = "3fc1a83fc1a8b456"

    def test_valid_hex_bin16(self):
        hex_bin16 = HexBinary16(self.VALID_HEX_STRING16)
        self.assertEqual(hex_bin16.hex_string16, self.VALID_HEX_STRING16)
        
    def test_invalid_hex_bin16_too_short(self):
        with self.assertRaises(TypeError):
            HexBinary16("33a1")

    def test_invalid_hex_bin16_odd_size_string(self):
        with self.assertRaises(TypeError):
            HexBinary16("33afc1a8b")

    def test_invalid_hex_bin16_invalid_alphabet(self):
        with self.assertRaises(TypeError):
            HexBinary16("gzc1a83fc1a8")

