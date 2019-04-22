import unittest

from lib.test.trees import michael_tree
from lib.test.trees import kristen_tree
from lib.test.trees import us05_marriage_before_death, us05_death_before_marriage


class TestMarriageBeforeDeath(unittest.TestCase):
    def test_marriage_before_death(self):
        self.assertTrue(us05_marriage_before_death.marriage_before_death())

    def test_death_before_marriage(self):
        self.assertFalse(us05_death_before_marriage.marriage_before_death())

    def test_michael_tree(self):
        self.assertTrue(michael_tree.marriage_before_death())

    def test_kristen_tree(self):
        self.assertTrue(kristen_tree.marriage_before_death())
