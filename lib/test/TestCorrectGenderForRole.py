import unittest

from GedcomParser.SSW555.lib.test.trees.US21AllCorrectGender import all_correct_gender
from GedcomParser.SSW555.lib.test.trees.US21HusbandIncorrect import husband_incorrect
from GedcomParser.SSW555.lib.test.trees.US21WifeIncorrect import wife_incorrect
from GedcomParser.SSW555.lib.test.trees.US21HusbAndWifeIncorrect import husb_and_wife_incorrect
from GedcomParser.SSW555.lib.test.trees.US21TwoHusbAndWifeIncorrect import two_husb_and_wife_incorrect


class TestCorrectGenderForRole(unittest.TestCase):
        
    def test_all_correct_gender(self):
        self.assertTrue(all_correct_gender.correct_gender_for_role())
        
    def test_husband_incorrect(self):
        self.assertFalse(husband_incorrect.correct_gender_for_role())
         
    def test_wife_inccorect(self):
        self.assertFalse(wife_incorrect.correct_gender_for_role())
         
    def test_husb_and_wife_incorrect(self):
        self.assertFalse(husb_and_wife_incorrect.correct_gender_for_role())
         
    def test_two_husb_and_wife_incorrect(self):
        self.assertFalse(two_husb_and_wife_incorrect.correct_gender_for_role())
