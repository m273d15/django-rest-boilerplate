from eid_server.eid_types.type_check import *
from eid_server.eid_types.place import *
from eid_server.eid_types.generaldate import *
from eid_server.eid_types.restricted_id import *
from datetime import date


class DocumentType:

    DOCUMENTTYPE_DEFINITION = "^[A-Z,\s]{2}$" 
  
    def __init__(self, documentCode):
        self.documentCode = documentCode

    @property
    def documentCode(self):
        return self._documentCode

    @documentCode.setter
    def documentCode(self, value):
        check_is_string_matching("DocumentType consists only of uppercase double-digit characters A-Z", 
            "DocumentType", value, self.DOCUMENTTYPE_DEFINITION)
        self._documentCode = value


class PersonalData:

    def __init__(self, *args, **kwargs):
        self.documentType = kwargs.get('documentType', None)
        self.issuingState = kwargs.get('issuingState', None)
        self.dateOfExpiry = kwargs.get('dateOfExpiry', None)
        self.givenNames = kwargs.get('givenNames', None)
        self.familyNames = kwargs.get('familyNames', None)
        self.artisticName = kwargs.get('artisticName', None)
        self.academicTitle = kwargs.get('academicTitle', None)
        self.dateOfBirth = kwargs.get('dateOfBirth', None)
        self.placeOfBirth = kwargs.get('placeOfBirth', None)
        self.nationality = kwargs.get('nationality', None)
        self.birthName = kwargs.get('birthName', None)
        self.placeOfResidence = kwargs.get('placeOfResidence', None)
        self.residencePermitI = kwargs.get('residencePermitI', None)
        self.restrictedID = kwargs.get('restrictedID', None)

    @property
    def documentType(self):
        return self._documentType

    @documentType.setter
    def documentType(self, value):
        if not value is None:
            check("documentType has to be a valid DocumentType", value, DocumentType)
        self._documentType = value

    @property
    def issuingState(self):
        return self._issuingState

    @issuingState.setter
    def issuingState(self, value):
        if not value is None:
            ICAOCountry.check_icao_country("issuingState", value)
        self._issuingState = value

    @property
    def dateOfExpiry(self):
        return self._dateOfExpiry

    @dateOfExpiry.setter
    def dateOfExpiry(self, value):
        if not value is None:
            check("dateOfExpiry has to be a valid Date", value, date)
        self._dateOfExpiry = value

    @property
    def givenNames(self):
        return self._givenNames

    @givenNames.setter
    def givenNames(self, value):
        if not value is None:
            check_str("givenNames", value)
        self._givenNames = value

    @property
    def familyNames(self):
        return self._familyNames

    @familyNames.setter
    def familyNames(self, value):
        if not value is None:
            check_str("familyNames", value)
        self._familyNames = value

    @property
    def artisticName(self):
        return self._artisticName

    @artisticName.setter
    def artisticName(self, value):
        if not value is None:
            check_str("artisticName", value)
        self._artisticName = value

    @property
    def academicTitle(self):
        return self._academicTitle

    @academicTitle.setter
    def academicTitle(self, value):
        if not value is None:
            check_str("academicTitle", value)
        self._academicTitle = value

    @property
    def dateOfBirth(self):
        return self._dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, value):
        if not value is None:
            GeneralDate.check_generalDate("dateOfBirth has to be a valid GeneralDate", value)
        self._dateOfBirth = value

    @property
    def placeOfBirth(self):
        return self._placeOfBirth

    @placeOfBirth.setter
    def placeOfBirth(self, value):
        if not value is None:
            GeneralPlace.check_general_place("placeOfBirth", value)
        self._placeOfBirth = value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        if not value is None:
            ICAOCountry.check_icao_country("nationality", value)
        self._nationality = value

    @property
    def birthName(self):
        return self._birthName

    @birthName.setter
    def birthName(self, value):
        if not value is None:
            check_str("birthName", value)
        self._birthName = value

    @property
    def placeOfResidence(self):
        return self._placeOfResidence

    @placeOfResidence.setter
    def placeOfResidence(self, value):
        if not value is None:
            GeneralPlace.check_general_place("selection", value)
        self._placeOfResidence = value

    @property
    def residencePermitI(self):
        return self._residencePermitI

    @residencePermitI.setter
    def residencePermitI(self, value):
        if not value is None:
            check_str("residencePermitI", value)
        self._residencePermitI = value

    @property
    def restrictedID(self):
        return self._restrictedID

    @restrictedID.setter
    def restrictedID(self, value):
        if not value is None:
            RestrictedId.check_restrictedId("restrictedID has to be a valid", value)
        self._restrictedID = value

