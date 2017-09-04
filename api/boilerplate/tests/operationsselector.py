from django.test import TestCase
from boilerplate.eid_types.operationsselector import OperationsSelector


class OperationsSelectorTests(TestCase):

    VALID_SELECTION_STRING_ALLOWED = "ALLOWED"
    VALID_SELECTION_STRING_PROHIBITED = "PROHIBITED"

    def test_valid_operationselector_allowed(self):
        operationsSelector = OperationsSelector(documentType=self.VALID_SELECTION_STRING_ALLOWED, 
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
        
        documentType = operationsSelector.documentType
        issuingState = operationsSelector.issuingState
        dateOfExpiry = operationsSelector.dateOfExpiry
        givenNames = operationsSelector.givenNames
        familyNames = operationsSelector.familyNames
        artisticName = operationsSelector.artisticName
        academicTitle = operationsSelector.academicTitle
        dateOfBirth = operationsSelector.dateOfBirth
        placeOfBirth = operationsSelector.placeOfBirth
        nationality = operationsSelector.nationality
        birthName = operationsSelector.birthName
        placeOfResidence = operationsSelector.placeOfResidence
        residencePermitI = operationsSelector.residencePermitI
        restrictedID = operationsSelector.restrictedID
        ageVerification = operationsSelector.ageVerification
        placeVerification = operationsSelector.placeVerification

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
        
    def test_valid_operationselector_prohibited(self):
        operationsSelector = OperationsSelector(documentType=self.VALID_SELECTION_STRING_PROHIBITED, 
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
        
        documentType = operationsSelector.documentType
        issuingState = operationsSelector.issuingState
        dateOfExpiry = operationsSelector.dateOfExpiry
        givenNames = operationsSelector.givenNames
        familyNames = operationsSelector.familyNames
        artisticName = operationsSelector.artisticName
        academicTitle = operationsSelector.academicTitle
        dateOfBirth = operationsSelector.dateOfBirth
        placeOfBirth = operationsSelector.placeOfBirth
        nationality = operationsSelector.nationality
        birthName = operationsSelector.birthName
        placeOfResidence = operationsSelector.placeOfResidence
        residencePermitI = operationsSelector.residencePermitI
        restrictedID = operationsSelector.restrictedID
        ageVerification = operationsSelector.ageVerification
        placeVerification = operationsSelector.placeVerification

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

