from boilerplate.eid_types.type_check import *


class VerificationResult:
    def __init__(self, fulfills_request):
        self.fulfills_request = fulfills_request

    @property
    def fulfills_request(self):
        return self._fulfills_request

    @fulfills_request.setter
    def fulfills_request(self, value):
        check_bool("major has to be a boolean", value)
        self._fulfills_request = value
        
