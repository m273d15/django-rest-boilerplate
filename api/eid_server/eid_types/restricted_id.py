from eid_server.eid_types.type_check import *
from eid_server.eid_types.hexbinary import *


class RestrictedId:
    def __init__(self, id, id2=None):
        self.id = id
        self.id2 = id2

    def check_restrictedId(description, variable):
        check(description, variable, RestrictedId)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check("id", value, HexBinary)
        self._id = value

    @property
    def id2(self):
        return self._id2

    @id2.setter
    def id2(self, value):
        if(not value is None):
            check("id2", value, HexBinary)
        self._id2 = value
        
