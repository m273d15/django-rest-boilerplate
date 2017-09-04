from django.test import TestCase
from boilerplate.eid_types.attributeselection import AttributeSelection


class AttributeSelectionTests(TestCase):

    VALID_SELECTION_STRING_ALLOWED = "ALLOWED"
    VALID_SELECTION_STRING_PROHIBITED = "PROHIBITED"

    def test_valid_attributeselection_allowed(self):
        selection = AttributeSelection(self.VALID_SELECTION_STRING_ALLOWED)
        s = selection.selection

        self.assertEqual(s, self.VALID_SELECTION_STRING_ALLOWED)

    def test_valid_attributeselection_prohibited(self):
        selection = AttributeSelection(self.VALID_SELECTION_STRING_PROHIBITED)
        s = selection.selection

        self.assertEqual(s, self.VALID_SELECTION_STRING_PROHIBITED)

    def test_attributeselection_raise_if_empty_selection(self):
        with self.assertRaises(TypeError):
            AttributeSelection("")

    def test_attributeselection_raise_if_none_selection(self):
        with self.assertRaises(TypeError):
            AttributeSelection(None)

    def test_attributeselection_raise_if_invalid_selection(self):
        with self.assertRaises(TypeError):
            AttributeSelection("TEST")

    def test_attributeselection_raise_if_int(self):
        with self.assertRaises(TypeError):
            AttributeSelection(2)
 
