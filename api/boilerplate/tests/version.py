from django.test import TestCase
from boilerplate.eid_types.version import Version


class VersionTests(TestCase):

    VALID_VERSION_STRING = "1.2-SNAPSHOT"
    VALID_MAJOR = 1
    VALID_MINOR = 2
    VALID_BUGFIX = 3

    def test_valid_version(self):
        version = Version(self.VALID_VERSION_STRING, self.VALID_MAJOR, self.VALID_MINOR, 
        self.VALID_BUGFIX)
        v = version.version
        ma = version.major
        mi = version.minor
        bu = version.bugfix

        self.assertEqual(v, self.VALID_VERSION_STRING)
        self.assertEqual(ma, self.VALID_MAJOR)
        self.assertEqual(mi, self.VALID_MINOR)
        self.assertEqual(bu, self.VALID_BUGFIX)

    def test_version_raise_if_invalid_bugfix(self):
        with self.assertRaises(TypeError):
            Version(self.VALID_VERSION_STRING, self.VALID_MAJOR, "Test")     

    def test_version_raise_if_empty_version(self):
        with self.assertRaises(TypeError):
            Version("", self.VALID_MAJOR, self.VALID_MINOR)
            
    def test_version_raise_if_none_version(self):
        with self.assertRaises(TypeError):
            Version(None, self.VALID_MAJOR, self.VALID_MINOR)

    def test_major_raise_if_none(self):
        with self.assertRaises(TypeError):
            Version(self.VALID_VERSION_STRING, None, self.VALID_MINOR)
    
    def test_minor_raise_if_none(self):
        with self.assertRaises(TypeError):
            Version(self.VALID_VERSION_STRING, self.VALID_MAJOR, None)

