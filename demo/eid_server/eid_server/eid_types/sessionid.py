from eid_server.eid_types.type_check import *
from eid_server.eid_types.hexbinary import *


class SessionID:

    def __init__(self, id):
        self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        check("id", value, HexBinary16)
        self._id = value

