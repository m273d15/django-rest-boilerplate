from django.test import TestCase
from datetime import date as datetime
from boilerplate.eid_types.generaldate import *


class GeneralDateTests(TestCase):

    VALID_DATE_STRING_1 = "19900124"
    VALID_DATE_STRING_2 = "24 01 1990"
    #VALID_DATE_STRING_2 = "  12 617" TODO: Reconsider if this is really valid

    def test_valid_date_string_1(self):
        date = GeneralDate(self.VALID_DATE_STRING_1)
        d = date.dateString

        self.assertEqual(d, self.VALID_DATE_STRING_1)
        
    def test_valid_generaldate_1(self):
        today = datetime.today()
        date = GeneralDate(self.VALID_DATE_STRING_1, today)
        s = date.dateString
        v = date.dateValue
        
        self.assertEqual(s, self.VALID_DATE_STRING_1)
        self.assertEqual(v, today)
        
    def test_valid_generaldate_2(self):
        today = datetime.today()
        date = GeneralDate(self.VALID_DATE_STRING_2, today)
        s = date.dateString
        v = date.dateValue
        
        self.assertEqual(s, self.VALID_DATE_STRING_2)
        self.assertEqual(v, today)
        
    #def test_valid_date_string_2(self):
    #    date = GeneralDate(self.VALID_DATE_STRING_2)
    #    d = date.dateString

    #    assert d == self.VALID_DATE_STRING_2

    def test_generaldate_raise_if_none_datestring(self):
        with self.assertRaises(TypeError):
            GeneralDate(None)

    #def test_generaldate_raise_if_invalid_datestring(self):
    #    try:
    #        GeneralDate(" 102725134")
    #        self.fail("dateString should only accept strings which match the pattern 'yyyymmdd'")
    #    except TypeError:
    #        pass

    def test_generaldate_raise_if_empty_datestring(self):
        with self.assertRaises(TypeError):
            GeneralDate("")

