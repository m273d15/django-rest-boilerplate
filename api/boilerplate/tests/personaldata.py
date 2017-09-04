from django.test import TestCase
from datetime import date as datetime
from boilerplate.eid_types.personaldata import *
from boilerplate.eid_types.restricted_id import *


class PersonalDataTests(TestCase):

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

    def test_valid_personaldata(self):
        personalData = PersonalData(documentType=self.VALID_DOCUMENT_TYPE, 
        issuingState=self.VALID_ISSUING_STATE, 
        dateOfExpiry=self.VALID_DATE_OF_EXPIRY, 
        givenNames=self.VALID_GIVEN_NAMES, 
        familyNames=self.VALID_FAMILY_NAMES, 
        artisticName=self.VALID_ARTISTIC_NAME, 
        academicTitle=self.VALID_ACADEMIC_TITLE, 
        dateOfBirth=self.VALID_DATE_OF_BIRTH, 
        placeOfBirth=self.VALID_PLACE_OF_BIRTH, 
        nationality=self.VALID_NATIONALITY, 
        birthName=self.VALID_BIRTH_NAME, 
        placeOfResidence=self.VALID_PLACE_OF_RESIDENCE, 
        residencePermitI=self.VALID_RESIDENCE_PERMIT_I, 
        restrictedID=self.VALID_RESTRICTED_ID)
        
        documentType = personalData.documentType
        issuingState = personalData.issuingState
        dateOfExpiry = personalData.dateOfExpiry
        givenNames = personalData.givenNames
        familyNames = personalData.familyNames
        artisticName = personalData.artisticName
        academicTitle = personalData.academicTitle
        dateOfBirth = personalData.dateOfBirth
        placeOfBirth = personalData.placeOfBirth
        nationality = personalData.nationality
        birthName = personalData.birthName
        placeOfResidence = personalData.placeOfResidence
        residencePermitI = personalData.residencePermitI
        restrictedID = personalData.restrictedID
        
        self.assertEqual(documentType, self.VALID_DOCUMENT_TYPE)
        self.assertEqual(issuingState, self.VALID_ISSUING_STATE)
        self.assertEqual(dateOfExpiry, self.VALID_DATE_OF_EXPIRY)
        self.assertEqual(givenNames, self.VALID_GIVEN_NAMES)
        self.assertEqual(familyNames, self.VALID_FAMILY_NAMES)
        self.assertEqual(artisticName, self.VALID_ARTISTIC_NAME)
        self.assertEqual(academicTitle, self.VALID_ACADEMIC_TITLE)
        self.assertEqual(dateOfBirth, self.VALID_DATE_OF_BIRTH)
        self.assertEqual(placeOfBirth, self.VALID_PLACE_OF_BIRTH)
        self.assertEqual(nationality, self.VALID_NATIONALITY)
        self.assertEqual(birthName, self.VALID_BIRTH_NAME)
        self.assertEqual(placeOfResidence, self.VALID_PLACE_OF_RESIDENCE)
        self.assertEqual(residencePermitI, self.VALID_RESIDENCE_PERMIT_I)
        self.assertEqual(restrictedID, self.VALID_RESTRICTED_ID)
        
