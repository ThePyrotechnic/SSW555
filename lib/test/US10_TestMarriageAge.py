import unittest

from lib.test.trees.US10AllOfAge import of_age

class Test_Age_At_Marriage(unittest.TestCase):
    def test_all_of_age(self):
        self.assertTrue(of_age.marriage_age())