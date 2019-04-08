import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import michael_dup_names


class TestUniqueChildren(unittest.TestCase):

    def test_michael_tree(self):
        self.assertTrue(michael_tree.unique_children())

    def test_kristen_tree(self):
        self.assertTrue(kristen_tree.unique_children())

    def test_michael_dup_names(self):
        self.assertFalse(michael_dup_names.unique_children())
