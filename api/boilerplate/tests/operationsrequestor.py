from django.test import TestCase
from boilerplate.eid_types.operationsrequestor import OperationsRequestor


class OperationsRequestorTests(TestCase):

    VALID_SELECTION_STRING_ALLOWED = "ALLOWED"
    VALID_SELECTION_STRING_PROHIBITED = "PROHIBITED"
    VALID_SELECTION_STRING_REQUIRED = "REQUIRED"

    def test_valid_operationsrequestor_allowed(self):
        operationsRequestor = OperationsRequestor(documentType=self.VALID_SELECTION_STRING_ALLOWED, 
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
        
        documentType = operationsRequestor.documentType
        issuingState = operationsRequestor.issuingState
        dateOfExpiry = operationsRequestor.dateOfExpiry
        givenNames = operationsRequestor.givenNames
        familyNames = operationsRequestor.familyNames
        artisticName = operationsRequestor.artisticName
        academicTitle = operationsRequestor.academicTitle
        dateOfBirth = operationsRequestor.dateOfBirth
        placeOfBirth = operationsRequestor.placeOfBirth
        nationality = operationsRequestor.nationality
        birthName = operationsRequestor.birthName
        placeOfResidence = operationsRequestor.placeOfResidence
        residencePermitI = operationsRequestor.residencePermitI
        restrictedID = operationsRequestor.restrictedID
        ageVerification = operationsRequestor.ageVerification
        placeVerification = operationsRequestor.placeVerification

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

    def test_valid_operationsRequestor_prohibited(self):
        operationsRequestor = OperationsRequestor(documentType=self.VALID_SELECTION_STRING_PROHIBITED, 
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
        
        documentType = operationsRequestor.documentType
        issuingState = operationsRequestor.issuingState
        dateOfExpiry = operationsRequestor.dateOfExpiry
        givenNames = operationsRequestor.givenNames
        familyNames = operationsRequestor.familyNames
        artisticName = operationsRequestor.artisticName
        academicTitle = operationsRequestor.academicTitle
        dateOfBirth = operationsRequestor.dateOfBirth
        placeOfBirth = operationsRequestor.placeOfBirth
        nationality = operationsRequestor.nationality
        birthName = operationsRequestor.birthName
        placeOfResidence = operationsRequestor.placeOfResidence
        residencePermitI = operationsRequestor.residencePermitI
        restrictedID = operationsRequestor.restrictedID
        ageVerification = operationsRequestor.ageVerification
        placeVerification = operationsRequestor.placeVerification

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

    def test_valid_operationsrequestor_required(self):
        operationsRequestor = OperationsRequestor(documentType=self.VALID_SELECTION_STRING_REQUIRED, 
        issuingState=self.VALID_SELECTION_STRING_REQUIRED, 
        dateOfExpiry=self.VALID_SELECTION_STRING_REQUIRED, 
        givenNames=self.VALID_SELECTION_STRING_REQUIRED, 
        familyNames=self.VALID_SELECTION_STRING_REQUIRED, 
        artisticName=self.VALID_SELECTION_STRING_REQUIRED, 
        academicTitle=self.VALID_SELECTION_STRING_REQUIRED, 
        dateOfBirth=self.VALID_SELECTION_STRING_REQUIRED, 
        placeOfBirth=self.VALID_SELECTION_STRING_REQUIRED, 
        nationality=self.VALID_SELECTION_STRING_REQUIRED, 
        birthName=self.VALID_SELECTION_STRING_REQUIRED, 
        placeOfResidence=self.VALID_SELECTION_STRING_REQUIRED, 
        residencePermitI=self.VALID_SELECTION_STRING_REQUIRED, 
        restrictedID=self.VALID_SELECTION_STRING_REQUIRED, 
        ageVerification=self.VALID_SELECTION_STRING_REQUIRED, 
        placeVerification=self.VALID_SELECTION_STRING_REQUIRED)
        
        documentType = operationsRequestor.documentType
        issuingState = operationsRequestor.issuingState
        dateOfExpiry = operationsRequestor.dateOfExpiry
        givenNames = operationsRequestor.givenNames
        familyNames = operationsRequestor.familyNames
        artisticName = operationsRequestor.artisticName
        academicTitle = operationsRequestor.academicTitle
        dateOfBirth = operationsRequestor.dateOfBirth
        placeOfBirth = operationsRequestor.placeOfBirth
        nationality = operationsRequestor.nationality
        birthName = operationsRequestor.birthName
        placeOfResidence = operationsRequestor.placeOfResidence
        residencePermitI = operationsRequestor.residencePermitI
        restrictedID = operationsRequestor.restrictedID
        ageVerification = operationsRequestor.ageVerification
        placeVerification = operationsRequestor.placeVerification

        self.assertEqual(documentType, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(issuingState, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(dateOfExpiry, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(givenNames, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(familyNames, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(artisticName, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(academicTitle, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(dateOfBirth, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(placeOfBirth, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(nationality, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(birthName, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(placeOfResidence, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(residencePermitI, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(restrictedID, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(ageVerification, self.VALID_SELECTION_STRING_REQUIRED)
        self.assertEqual(placeVerification, self.VALID_SELECTION_STRING_REQUIRED)

