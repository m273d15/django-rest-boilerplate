from boilerplate.eid_types.type_check import *
from boilerplate.eid_types.hexbinary import *


class PreSharedKey:
    def __init__(self, id, key):
        self.id = id
        self.key = key

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check_str("id", value, False)
        self._id = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        check("key", value, HexBinary16)
        self._key = value
        
