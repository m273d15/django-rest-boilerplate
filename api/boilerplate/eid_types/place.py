from boilerplate.eid_types.type_check import *


class ICAOCountry:
    COUNTRY_PATTERN = "^([A-Z,\ ]|[A-Z,\ ]{3})$"

    def __init__(self, country_code):
        self.country = country_code

    def check_icao_country(variable_name, variable):
        check(variable_name + " has to be a valid ICAOCountry", variable, ICAOCountry)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        description = ("Country string has to consist of one or three characters, where"
        + " each charachter is an ascii uppercase char or a whitespace.")
        check_is_string_matching(description, "country", value, self.COUNTRY_PATTERN) 
        self._country = value


class GeneralPlace:
    def __init__(self, structured_place, freetext_place, no_place_info):
        self.structured_place = structured_place
        self.freetext_place = freetext_place
        self.no_place_info = no_place_info

    def check_general_place(variable_name, variable):
        check(variable_name + " has to be a valid GeneralPlace", variable, GeneralPlace)

    @property
    def structured_place(self):
        return self._structured_place

    @structured_place.setter
    def structured_place(self, value):
        Place.check_place("structured_place", value)
        self._structured_place = value

    @property
    def freetext_place(self):
        return self._freetext_place

    @freetext_place.setter
    def freetext_place(self, value):
        check_str("freetext_place", value, True)
        self._freetext_place = value

    @property
    def no_place_info(self):
        return self._no_place_info

    @no_place_info.setter
    def no_place_info(self, value):
        check_str("no_place_info", value, True)
        self._no_place_info = value


class Place:
    def __init__(self, city, country, *args, **kwargs):
        self.city = city
        self.country = country

        self.street = kwargs.get('street', None)
        self.state = kwargs.get('state', None)
        self.zip_code = kwargs.get('zip_code', None)

    def check_place(variable_name, variable):
        check(variable_name + " has to be a valid Place", variable, Place)

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        ICAOCountry.check_icao_country("country", value)
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        check_str("city", value)
        self._city = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        if not value is None:
            check_str("street", value)
        self._street = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if not value is None:
            check_str("state", value)
        self._state = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        if not value is None:
            check_str("zip_code", value)
        self._zip_code = value

