from boilerplate.eid_types.type_check import *


class OperationsRequestor:

    DESCRIPTION_STRING = " has to be a non empty string containing either 'ALLOWED' or 'PROHIBITED' or 'REQUIRED'"

    def __init__(self, *args, **kwargs):
        self.documentType = kwargs.get('documentType', 'PROHIBITED')
        self.issuingState = kwargs.get('issuingState', 'PROHIBITED')
        self.dateOfExpiry = kwargs.get('dateOfExpiry', 'PROHIBITED')
        self.givenNames = kwargs.get('givenNames', 'PROHIBITED')
        self.familyNames = kwargs.get('familyNames', 'PROHIBITED')
        self.artisticName = kwargs.get('artisticName', 'PROHIBITED')
        self.academicTitle = kwargs.get('academicTitle', 'PROHIBITED')
        self.dateOfBirth = kwargs.get('dateOfBirth', 'PROHIBITED')
        self.placeOfBirth = kwargs.get('placeOfBirth', 'PROHIBITED')
        self.nationality = kwargs.get('nationality', 'PROHIBITED')
        self.birthName = kwargs.get('birthName', 'PROHIBITED')
        self.placeOfResidence = kwargs.get('placeOfResidence', 'PROHIBITED')
        self.residencePermitI = kwargs.get('residencePermitI', 'PROHIBITED')
        self.restrictedID = kwargs.get('restrictedID', 'PROHIBITED')
        self.ageVerification = kwargs.get('ageVerification', 'PROHIBITED')
        self.placeVerification = kwargs.get('placeVerification', 'PROHIBITED')

    @property
    def documentType(self):
        return self._documentType

    @documentType.setter
    def documentType(self, value):
        check_attributeRequest("documentType" + self.DESCRIPTION_STRING, value)
        self._documentType = value

    @property
    def issuingState(self):
        return self._issuingState

    @issuingState.setter
    def issuingState(self, value):
        check_attributeRequest("issuingState" + self.DESCRIPTION_STRING, value)
        self._issuingState = value

    @property
    def dateOfExpiry(self):
        return self._dateOfExpiry

    @dateOfExpiry.setter
    def dateOfExpiry(self, value):
        check_attributeRequest("dateOfExpiry" + self.DESCRIPTION_STRING, value)
        self._dateOfExpiry = value

    @property
    def givenNames(self):
        return self._givenNames

    @givenNames.setter
    def givenNames(self, value):
        check_attributeRequest("givenNames" + self.DESCRIPTION_STRING, value)
        self._givenNames = value

    @property
    def familyNames(self):
        return self._familyNames

    @familyNames.setter
    def familyNames(self, value):
        check_attributeRequest("familyNames" + self.DESCRIPTION_STRING, value)
        self._familyNames = value

    @property
    def artisticName(self):
        return self._artisticName

    @artisticName.setter
    def artisticName(self, value):
        check_attributeRequest("artisticName" + self.DESCRIPTION_STRING, value)
        self._artisticName = value

    @property
    def academicTitle(self):
        return self._academicTitle

    @academicTitle.setter
    def academicTitle(self, value):
        check_attributeRequest("academicTitle" + self.DESCRIPTION_STRING, value)
        self._academicTitle = value

    @property
    def dateOfBirth(self):
        return self._dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, value):
        check_attributeRequest("dateOfBirth" + self.DESCRIPTION_STRING, value)
        self._dateOfBirth = value

    @property
    def placeOfBirth(self):
        return self._placeOfBirth

    @placeOfBirth.setter
    def placeOfBirth(self, value):
        check_attributeRequest("placeOfBirth" + self.DESCRIPTION_STRING, value)
        self._placeOfBirth = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        check_attributeRequest("nationality" + self.DESCRIPTION_STRING, value)
        self._nationality = value

    @property
    def birthName(self):
        return self._birthName

    @birthName.setter
    def birthName(self, value):
        check_attributeRequest("birthName" + self.DESCRIPTION_STRING, value)
        self._birthName = value

    @property
    def placeOfResidence(self):
        return self._placeOfResidence

    @placeOfResidence.setter
    def placeOfResidence(self, value):
        check_attributeRequest("selection" + self.DESCRIPTION_STRING, value)
        self._placeOfResidence = value

    @property
    def residencePermitI(self):
        return self._residencePermitI

    @residencePermitI.setter
    def residencePermitI(self, value):
        check_attributeRequest("residencePermitI" + self.DESCRIPTION_STRING, value)
        self._residencePermitI = value

    @property
    def restrictedID(self):
        return self._restrictedID

    @restrictedID.setter
    def restrictedID(self, value):
        check_attributeRequest("restrictedID" + self.DESCRIPTION_STRING, value)
        self._restrictedID = value

    @property
    def ageVerification(self):
        return self._ageVerification

    @ageVerification.setter
    def ageVerification(self, value):
        check_attributeRequest("ageVerification" + self.DESCRIPTION_STRING, value)
        self._ageVerification = value

    @property
    def placeVerification(self):
        return self._placeVerification

    @placeVerification.setter
    def placeVerification(self, value):
        check_attributeRequest("placeVerification" + self.DESCRIPTION_STRING, value)
        self._placeVerification = value
        
