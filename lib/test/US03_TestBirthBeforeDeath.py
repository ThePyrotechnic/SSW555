import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import us03_death_before_birth


class TestBirthBeforeDeath(unittest.TestCase):
    def test_michael_tree(self):
        self.assertTrue(michael_tree.birth_before_death())

    def test_kristen_tree(self):
        self.assertTrue(kristen_tree.birth_before_death())

    def test_birth_before_death(self):
        self.assertFalse(us03_death_before_birth.birth_before_death())
