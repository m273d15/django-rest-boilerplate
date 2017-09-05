from django.test import TestCase
from eid_server.eid_types.operationsresponder import OperationsResponder


class OperationsResponderTests(TestCase):

    VALID_SELECTION_STRING_ALLOWED = "ALLOWED"
    VALID_SELECTION_STRING_PROHIBITED = "PROHIBITED"
    VALID_SELECTION_STRING_NOTONCHIP = "NOTONCHIP"

    def test_valid_operationsresponder_allowed(self):
        operationsResponder = OperationsResponder(
            documentType=self.VALID_SELECTION_STRING_ALLOWED, 
            issuingState=self.VALID_SELECTION_STRING_ALLOWED, 
            dateOfExpiry=self.VALID_SELECTION_STRING_ALLOWED, 
            givenNames=self.VALID_SELECTION_STRING_ALLOWED, 
            familyNames=self.VALID_SELECTION_STRING_ALLOWED, 
            artisticName=self.VALID_SELECTION_STRING_ALLOWED, 
            academicTitle=self.VALID_SELECTION_STRING_ALLOWED, 
            dateOfBirth=self.VALID_SELECTION_STRING_ALLOWED, 
            placeOfBirth=self.VALID_SELECTION_STRING_ALLOWED, 
            nationality=self.VALID_SELECTION_STRING_ALLOWED, 
            birthName=self.VALID_SELECTION_STRING_ALLOWED, 
            placeOfResidence=self.VALID_SELECTION_STRING_ALLOWED, 
            residencePermitI=self.VALID_SELECTION_STRING_ALLOWED, 
            restrictedID=self.VALID_SELECTION_STRING_ALLOWED, 
            ageVerification=self.VALID_SELECTION_STRING_ALLOWED, 
            placeVerification=self.VALID_SELECTION_STRING_ALLOWED)
        
        documentType = operationsResponder.documentType
        issuingState = operationsResponder.issuingState
        dateOfExpiry = operationsResponder.dateOfExpiry
        givenNames = operationsResponder.givenNames
        familyNames = operationsResponder.familyNames
        artisticName = operationsResponder.artisticName
        academicTitle = operationsResponder.academicTitle
        dateOfBirth = operationsResponder.dateOfBirth
        placeOfBirth = operationsResponder.placeOfBirth
        nationality = operationsResponder.nationality
        birthName = operationsResponder.birthName
        placeOfResidence = operationsResponder.placeOfResidence
        residencePermitI = operationsResponder.residencePermitI
        restrictedID = operationsResponder.restrictedID
        ageVerification = operationsResponder.ageVerification
        placeVerification = operationsResponder.placeVerification

        self.assertEqual(documentType, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(issuingState, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(dateOfExpiry, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(givenNames, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(familyNames, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(artisticName, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(academicTitle, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(dateOfBirth, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(placeOfBirth, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(nationality, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(birthName, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(placeOfResidence, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(residencePermitI, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(restrictedID, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(ageVerification, self.VALID_SELECTION_STRING_ALLOWED)
        self.assertEqual(placeVerification, self.VALID_SELECTION_STRING_ALLOWED)

    def test_valid_operationsResponder_prohibited(self):
        operationsResponder = OperationsResponder(
            documentType=self.VALID_SELECTION_STRING_PROHIBITED, 
            issuingState=self.VALID_SELECTION_STRING_PROHIBITED, 
            dateOfExpiry=self.VALID_SELECTION_STRING_PROHIBITED, 
            givenNames=self.VALID_SELECTION_STRING_PROHIBITED, 
            familyNames=self.VALID_SELECTION_STRING_PROHIBITED, 
            artisticName=self.VALID_SELECTION_STRING_PROHIBITED, 
            academicTitle=self.VALID_SELECTION_STRING_PROHIBITED, 
            dateOfBirth=self.VALID_SELECTION_STRING_PROHIBITED, 
            placeOfBirth=self.VALID_SELECTION_STRING_PROHIBITED, 
            nationality=self.VALID_SELECTION_STRING_PROHIBITED, 
            birthName=self.VALID_SELECTION_STRING_PROHIBITED, 
            placeOfResidence=self.VALID_SELECTION_STRING_PROHIBITED, 
            residencePermitI=self.VALID_SELECTION_STRING_PROHIBITED, 
            restrictedID=self.VALID_SELECTION_STRING_PROHIBITED, 
            ageVerification=self.VALID_SELECTION_STRING_PROHIBITED, 
            placeVerification=self.VALID_SELECTION_STRING_PROHIBITED)
        
        documentType = operationsResponder.documentType
        issuingState = operationsResponder.issuingState
        dateOfExpiry = operationsResponder.dateOfExpiry
        givenNames = operationsResponder.givenNames
        familyNames = operationsResponder.familyNames
        artisticName = operationsResponder.artisticName
        academicTitle = operationsResponder.academicTitle
        dateOfBirth = operationsResponder.dateOfBirth
        placeOfBirth = operationsResponder.placeOfBirth
        nationality = operationsResponder.nationality
        birthName = operationsResponder.birthName
        placeOfResidence = operationsResponder.placeOfResidence
        residencePermitI = operationsResponder.residencePermitI
        restrictedID = operationsResponder.restrictedID
        ageVerification = operationsResponder.ageVerification
        placeVerification = operationsResponder.placeVerification

        self.assertEqual(documentType, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(issuingState, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(dateOfExpiry, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(givenNames, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(familyNames, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(artisticName, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(academicTitle, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(dateOfBirth, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(placeOfBirth, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(nationality, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(birthName, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(placeOfResidence, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(residencePermitI, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(restrictedID, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(ageVerification, self.VALID_SELECTION_STRING_PROHIBITED)
        self.assertEqual(placeVerification, self.VALID_SELECTION_STRING_PROHIBITED)

    def test_valid_operationsresponder_required(self):
        operationsResponder = OperationsResponder(
            documentType=self.VALID_SELECTION_STRING_NOTONCHIP, 
            issuingState=self.VALID_SELECTION_STRING_NOTONCHIP, 
            dateOfExpiry=self.VALID_SELECTION_STRING_NOTONCHIP, 
            givenNames=self.VALID_SELECTION_STRING_NOTONCHIP, 
            familyNames=self.VALID_SELECTION_STRING_NOTONCHIP, 
            artisticName=self.VALID_SELECTION_STRING_NOTONCHIP, 
            academicTitle=self.VALID_SELECTION_STRING_NOTONCHIP, 
            dateOfBirth=self.VALID_SELECTION_STRING_NOTONCHIP, 
            placeOfBirth=self.VALID_SELECTION_STRING_NOTONCHIP, 
            nationality=self.VALID_SELECTION_STRING_NOTONCHIP, 
            birthName=self.VALID_SELECTION_STRING_NOTONCHIP, 
            placeOfResidence=self.VALID_SELECTION_STRING_NOTONCHIP, 
            residencePermitI=self.VALID_SELECTION_STRING_NOTONCHIP, 
            restrictedID=self.VALID_SELECTION_STRING_NOTONCHIP, 
            ageVerification=self.VALID_SELECTION_STRING_NOTONCHIP, 
            placeVerification=self.VALID_SELECTION_STRING_NOTONCHIP)
        
        documentType = operationsResponder.documentType
        issuingState = operationsResponder.issuingState
        dateOfExpiry = operationsResponder.dateOfExpiry
        givenNames = operationsResponder.givenNames
        familyNames = operationsResponder.familyNames
        artisticName = operationsResponder.artisticName
        academicTitle = operationsResponder.academicTitle
        dateOfBirth = operationsResponder.dateOfBirth
        placeOfBirth = operationsResponder.placeOfBirth
        nationality = operationsResponder.nationality
        birthName = operationsResponder.birthName
        placeOfResidence = operationsResponder.placeOfResidence
        residencePermitI = operationsResponder.residencePermitI
        restrictedID = operationsResponder.restrictedID
        ageVerification = operationsResponder.ageVerification
        placeVerification = operationsResponder.placeVerification

        self.assertEqual(documentType, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(issuingState, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(dateOfExpiry, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(givenNames, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(familyNames, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(artisticName, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(academicTitle, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(dateOfBirth, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(placeOfBirth, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(nationality, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(birthName, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(placeOfResidence, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(residencePermitI, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(restrictedID, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(ageVerification, self.VALID_SELECTION_STRING_NOTONCHIP)
        self.assertEqual(placeVerification, self.VALID_SELECTION_STRING_NOTONCHIP)

