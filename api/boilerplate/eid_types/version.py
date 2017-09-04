from boilerplate.eid_types.type_check import *


class Version:
    def __init__(self, version, major, minor, bugfix=None):
        self.version = version
        self.major = major
        self.minor = minor
        self.bugfix = bugfix

    @property
    def bugfix(self):
        return self._bugfix

    @bugfix.setter
    def bugfix(self, value):
        if (not value is None):
            check_int("bugfix", value)
        self._bugfix = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        check_int("major", value)
        self._major = value

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, value):
        check_int("minor", value)
        self._minor = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        check_str("version", value)
        self._version = value
        
