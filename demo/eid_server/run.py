from procbridge import procbridge
from eid_server.eid_types.personaldata import *
from eid_server.eid_types.restricted_id import *
from eid_server.eid_types.hexbinary import *
from datetime import date as datetime
import time
import json

if __name__ == '__main__':

    host = '0.0.0.0'
    port = 8877
    
    VALID_DOCUMENT_TYPE = DocumentType("DE")
    VALID_ISSUING_STATE = ICAOCountry("D")
    VALID_DATE_OF_EXPIRY = datetime.today()
    VALID_GIVEN_NAMES = "Max"
    VALID_FAMILY_NAMES = "Mustermann"
    VALID_ARTISTIC_NAME = "Mozart"
    VALID_ACADEMIC_TITLE = "Dr"
    VALID_DATE_OF_BIRTH = GeneralDate("19900124")
    VALID_PLACE_OF_BIRTH = GeneralPlace(Place("Berlin", ICAOCountry("D")), 
        "Berlin, DE", "no place info")
    VALID_NATIONALITY = ICAOCountry("D")
    VALID_BIRTH_NAME = "Musterfrau"
    VALID_PLACE_OF_RESIDENCE = GeneralPlace(Place("Berlin", ICAOCountry("D")), 
        "Berlin, DE", "no place info")
    VALID_RESIDENCE_PERMIT_I = "Residence Permit I"
    VALID_RESTRICTED_ID = RestrictedId(HexBinary("3fc1a8"), HexBinary("fc1a83"))

    personal_data = PersonalData(
            documentType=VALID_DOCUMENT_TYPE, 
            issuingState=VALID_ISSUING_STATE, 
            dateOfExpiry=VALID_DATE_OF_EXPIRY, 
            givenNames=VALID_GIVEN_NAMES, 
            familyNames=VALID_FAMILY_NAMES, 
            artisticName=VALID_ARTISTIC_NAME, 
            academicTitle=VALID_ACADEMIC_TITLE, 
            dateOfBirth=VALID_DATE_OF_BIRTH, 
            placeOfBirth=VALID_PLACE_OF_BIRTH, 
            nationality=VALID_NATIONALITY, 
            birthName=VALID_BIRTH_NAME, 
            placeOfResidence=VALID_PLACE_OF_RESIDENCE, 
            residencePermitI=VALID_RESIDENCE_PERMIT_I, 
            restrictedID=VALID_RESTRICTED_ID)

    # define request handler
    def request_handler(api: str, arg: dict) -> dict:

        if api == 'storeNPAData':
            print("Received arg:", arg, flush=True)
            print("Received restricted id:", arg['restrictedID'], flush=True)
            personal_data.restrictedID = RestrictedId(HexBinary(arg['restrictedID']))
            print("Updated restricted id:", personal_data.restrictedID.id.hex_string, flush=True)
            
            return arg
        else:
            raise Exception('unknown api')

    # start socket server
    server = procbridge.ProcBridgeServer(host, port, request_handler)
    server.start()
    print('listening...')

    while True:
        time.sleep(1)

    server.stop()
    print('bye!')