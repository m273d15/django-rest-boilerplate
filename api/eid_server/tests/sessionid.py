from django.test import TestCase
from eid_server.eid_types.sessionid import SessionID
from eid_server.eid_types.hexbinary import HexBinary16


class SessionIdTests(TestCase):

    VALID_ID_STRING = "3fc1a83fc1a8b4563fc1a83fc1a8b456"
    VALID_ID_HEXBINARY16 = HexBinary16(VALID_ID_STRING)

    def test_valid_sessionid(self):
        p = SessionID(self.VALID_ID_HEXBINARY16)
        
        self.assertEqual(p.id, self.VALID_ID_HEXBINARY16)
        
