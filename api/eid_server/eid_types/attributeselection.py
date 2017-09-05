from eid_server.eid_types.type_check import *


class AttributeSelection:
    def __init__(self, selection):
        self.selection = selection

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        check_attributeSelection("selection has to be a non empty string containing either" 
            + " 'ALLOWED' or 'PROHIBITED'", value)
        self._selection = value
        
