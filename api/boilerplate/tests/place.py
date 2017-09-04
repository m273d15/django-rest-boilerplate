from django.test import TestCase
from boilerplate.eid_types.place import ICAOCountry, Place, GeneralPlace


class ICAOCountryTests(TestCase):

    VALID_ICAO_3L_CODE="AFG"
    VALID_ICAO_1L_CODE="A"

    def test_valid_country_with_3_letters(self):
        country = ICAOCountry(self.VALID_ICAO_3L_CODE)
        self.assertEqual(country.country, self.VALID_ICAO_3L_CODE)

    def test_icao_country_raise_country_is_empty(self):
        with self.assertRaises(TypeError):
            ICAOCountry("")     

    def test_icao_country_raise_country_has_length_2(self):
        with self.assertRaises(TypeError):
            ICAOCountry("AB")     

    def test_icao_country_raise_country_has_length_4(self):
        with self.assertRaises(TypeError):
            ICAOCountry("ABCD")     

    def test_icao_country_raise_country_contains_lowercase(self):
        with self.assertRaises(TypeError):
            ICAOCountry("AbC")

    def test_icao_country_with_whitespaces(self):
        country_str = "A C"
        country = ICAOCountry(country_str)
        self.assertEqual(country.country, country_str)


class GeneralPlaceTests(TestCase):

    VALID_PLACE = Place("Chicago", ICAOCountry("USA"))
    VALID_TEXT = "text"
    VALID_INFO = "info"

    def test_valid_generalplace(self):
        gplace = GeneralPlace(self.VALID_PLACE, self.VALID_TEXT, self.VALID_INFO)

        self.assertEqual(gplace.freetext_place, self.VALID_TEXT)
        self.assertEqual(gplace.no_place_info, self.VALID_INFO)

    def test_generalplace_with_None_structured_place(self):
        with self.assertRaises(TypeError):
            GeneralPlace(None, "text", "text")


class PlaceTests(TestCase):

    VALID_CITY = "Chicago"
    VALID_COUNTRY = ICAOCountry("USA")

    VALID_STATE = "Illinois"
    VALID_STREET = "State Street"
    VALID_ZIP_CODE = "60606"

    def test_valid_place_with_all_optional(self):
        place = Place(self.VALID_CITY, self.VALID_COUNTRY, state = self.VALID_STATE, street = self.VALID_STREET, zip_code = self.VALID_ZIP_CODE)

        self.assertEqual(place.city, self.VALID_CITY)
        self.assertEqual(place.country.country, self.VALID_COUNTRY.country)
        self.assertEqual(place.state, self.VALID_STATE)
        self.assertEqual(place.street, self.VALID_STREET)
        self.assertEqual(place.zip_code, self.VALID_ZIP_CODE)

    def test_place_with_None_country(self):
        with self.assertRaises(TypeError):
            Place(self.VALID_CITY, None)

    def test_place_with_without_optional(self):
        place = Place(self.VALID_CITY, self.VALID_COUNTRY)

        self.assertEqual(place.city, self.VALID_CITY)
        self.assertEqual(place.country.country, self.VALID_COUNTRY.country)

