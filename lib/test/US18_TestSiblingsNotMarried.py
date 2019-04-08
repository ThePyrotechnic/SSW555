import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import us18_siblings_married, us18_siblings_not_married


class TestSiblingsNotMarried(unittest.TestCase):
    def test_michael_tree(self):
        self.assertTrue(michael_tree.siblings_not_married())

    def test_kristen_tree(self):
        self.assertTrue(kristen_tree.siblings_not_married())

    def test_siblings_married(self):
        self.assertFalse(us18_siblings_married.siblings_not_married())

    def test_siblings_not_married(self):
        self.assertTrue(us18_siblings_not_married.siblings_not_married())
