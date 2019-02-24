import unittest

from lib.test.trees.US16AllSameNames import all_same_names
from lib.test.trees.US16FatherDiff import father_diff
from lib.test.trees.US16SonDiff import son_diff
from lib.test.trees.US16ThreeSonsOneDiff import three_sons_one_diff
from lib.test.trees.US16TwoAbbFams import two_fams_abb

class TestSameMaleLastNames(unittest.TestCase):

    def test_all_correct_gender(self):
        self.assertTrue(all_same_names.male_last_names())

    def test_husband_incorrect(self):
        self.assertFalse(father_diff.male_last_names())

    def test_wife_inccorect(self):
        self.assertFalse(son_diff.male_last_names())

    def test_husb_and_wife_incorrect(self):
        self.assertFalse(three_sons_one_diff.male_last_names())

    def test_two_husb_and_wife_incorrect(self):
        self.assertFalse(two_fams_abb.male_last_names())