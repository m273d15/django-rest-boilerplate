from eid_server.eid_types.type_check import *


class AttributeRequest:
    def __init__(self, request):
        self.request = request

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, value):
        check_attributeRequest("request has to be a non empty string containing either" 
            + "'ALLOWED' or 'PROHIBITED' or 'REQUIRED'", value)
        self._request = value
        
