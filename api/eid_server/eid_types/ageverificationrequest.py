from eid_server.eid_types.type_check import *


class AgeVerificationRequest:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        check_positive_int('age', value)
        self._age = value
        
