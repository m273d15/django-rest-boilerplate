from django.test import TestCase
from eid_server.eid_types.placeverificationrequest import *


class PlaceVerificationRequestTests(TestCase):

    VALID_COMMUNITY_ID_1 = ""
    VALID_COMMUNITY_ID_2 = "0276"
    VALID_COMMUNITY_ID_3 = "027612"
    VALID_COMMUNITY_ID_4 = "02761209"
    VALID_COMMUNITY_ID_5 = "0276120937"
    VALID_COMMUNITY_ID_6 = "02761209370123"

    def test_valid_communityid_1(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_1)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_1)

    def test_valid_communityid_2(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_2)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_2)

    def test_valid_communityid_3(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_3)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_3)

    def test_valid_communityid_4(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_4)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_4)

    def test_valid_communityid_5(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_5)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_5)

    def test_valid_communityid_6(self):
        request = PlaceVerificationRequest(self.VALID_COMMUNITY_ID_6)
        communityid = request.communityid

        self.assertEqual(communityid, self.VALID_COMMUNITY_ID_6)

    def test_placeverificationrequest_raise_if_invalid_communityid(self):
        with self.assertRaises(TypeError):
            PlaceVerificationRequest("1234")

    def test_placeverificationrequest_raise_if_none_communityid(self):
        with self.assertRaises(TypeError):
            PlaceVerificationRequest(None)

    def test_placeverificationrequest_raise_if_invalid_datatype_communityid(self):
        with self.assertRaises(TypeError):
            PlaceVerificationRequest(1234)

