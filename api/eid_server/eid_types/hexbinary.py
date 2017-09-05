from eid_server.eid_types.type_check import *


class HexBinary:

    def __init__(self, hex_string):
        self.hex_string = hex_string

    @property
    def hex_string(self):
        return self._hex_string

    @hex_string.setter
    def hex_string(self, value):

        pattern = "^([A-F,a-f,0-9]{2})*$"
        check_is_string_matching("Hex string should match the regex " + pattern, "hex_string",
            value, pattern)    
        self._hex_string = value
        
        
class HexBinary16:

    def __init__(self, hex_string16):
        self.hex_string16 = hex_string16
        
    @property
    def hex_string16(self):
        return self._hex_string16
        
    @hex_string16.setter
    def hex_string16(self, value):
        pattern = "^([A-F,a-f,0-9]{2}){8,}$"
        check_is_string_matching("Hex string should match the regex " + pattern 
            + " and be longer than 16", "hex_string16", value, pattern)
        self._hex_string16 = value
        
