from boilerplate.eid_types.type_check import *


class PlaceVerificationRequest:
    def __init__(self, communityid):
        self.communityid = communityid

    @property
    def communityid(self):
        return self._communityid

    @communityid.setter
    def communityid(self, value):
        check_placeVerificationRequest("CommunityID should be a string matching the pattern" 
        + "'([0][0-9]{3}([0-9]{2}([0][0-9]([0-9]{2}([0][0-9]{3})?)?)?)?)?$'", 'communityid', 
        value)
        self._communityid = value
        
