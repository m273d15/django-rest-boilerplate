from eid_server.eid_types.type_check import * 


class AttributeResponse:
    def __init__(self, response):
        self.response = response

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        check_attributeResponse("response has to be a non empty string containing either" 
            + "'ALLOWED', 'PROHIBITED' or 'NOTONCHIP'", 'response', value)
        self._response = value
        
