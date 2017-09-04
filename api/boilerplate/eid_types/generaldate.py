from boilerplate.eid_types.type_check import *


class GeneralDate:
    def __init__(self, dateString, dateValue=None):
        self.dateString = dateString
        self.dateValue = dateValue
        
    def check_generalDate(description, variable):
        check(description, variable, GeneralDate)

    @property
    def dateString(self):
        return self._dateString
    
    # TODO: the specifications for this type are highly confusing! 
    # Might need refactoring. See #51
    @dateString.setter
    def dateString(self, value):
        check_dateString("dateString has to be a non empty string of the form 'yyyymmdd'", 
        'dateString', value)
        self._dateString = value

    @property
    def dateValue(self):
        return self._dateValue

    @dateValue.setter
    def dateValue(self, value):
        if not value is None:
            check_dateValue("dateValue is optional but when present, it has to be a non empty" 
            + " string of the form '[-]yyyy-mm-dd[z|(+|-)hh:mm]'", 'dateValue', value)
        self._dateValue = value
        
