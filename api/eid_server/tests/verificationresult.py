from django.test import TestCase
from eid_server.eid_types.verificationresult import VerificationResult


class VerificationResultTests(TestCase):

    VALID_VERIFICATIONRESULT_BOOL_TRUE = True
    VALID_VERIFICATIONRESULT_BOOL_FALSE = False

    def test_valid_verificationResult_true(self):
        verificationresult = VerificationResult(self.VALID_VERIFICATIONRESULT_BOOL_TRUE)
        v = verificationresult.fulfills_request

        self.assertEqual(v, self.VALID_VERIFICATIONRESULT_BOOL_TRUE)

    def test_valid_verificationResult_false(self):
        verificationresult = VerificationResult(self.VALID_VERIFICATIONRESULT_BOOL_FALSE)
        v = verificationresult.fulfills_request

        self.assertEqual(v, self.VALID_VERIFICATIONRESULT_BOOL_FALSE)

    def test_verificationResult_raise_if_none_fulfills_request(self):
        with self.assertRaises(TypeError):
            VerificationResult(None)

    def test_verificationResult_raise_if_int(self):
        with self.assertRaises(TypeError):
            VerificationResult(4)
 
