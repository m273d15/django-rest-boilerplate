from django.test import TestCase
from boilerplate.eid_types.ageverificationrequest import *


class AgeVerificationRequestTests(TestCase):

    VALID_AGE_VERIFICATION_REQUEST = 30
    
    def test_valid_ageverificationrequest(self):
        request = AgeVerificationRequest(self.VALID_AGE_VERIFICATION_REQUEST)
        age = request.age

        self.assertEqual(age, self.VALID_AGE_VERIFICATION_REQUEST)

    def test_ageverificationrequest_raise_if_none_age(self):
        with self.assertRaises(TypeError):
            AgeVerificationRequest(None)

    def test_ageverificationrequest_raise_if_negative_age(self):
        with self.assertRaises(TypeError):
            AgeVerificationRequest(-12)

    def test_ageverificationrequest_raise_if_invalid_datatype_age(self):
        with self.assertRaises(TypeError):
            AgeVerificationRequest(2.0)

