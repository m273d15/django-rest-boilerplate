from django.test import TestCase
from boilerplate.eid_types.presharedkey import *


class PreSharedKeyTests(TestCase):

    VALID_ID_STRING = "3a"
    VALID_KEY_STRING = "3fc1a83fc1a8b456"
    VALID_KEY_HEXBINARY16 = HexBinary16(VALID_KEY_STRING)

    def test_valid_presharedkey(self):
        p = PreSharedKey(self.VALID_ID_STRING, self.VALID_KEY_HEXBINARY16)
        
        self.assertEqual(p.id, self.VALID_ID_STRING)
        self.assertEqual(p.key, self.VALID_KEY_HEXBINARY16)
        
