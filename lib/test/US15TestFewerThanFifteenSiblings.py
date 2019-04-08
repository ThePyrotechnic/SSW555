import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import us15_more_than_fifteen_siblings
from lib.test.trees import us15_exactly_fifteen_siblings
from lib.test.trees import us15_many_more_than_fifteen_siblings


class TestFewerThanFifteenSiblings(unittest.TestCase):

    def test_under_fifteen(self):
        self.assertTrue(kristen_tree.fewer_than_fifteen_siblings())

    def test_under_fifteen_2(self):
        self.assertTrue(michael_tree.fewer_than_fifteen_siblings())

    def test_more_than_fifteen(self):
        self.assertFalse(us15_more_than_fifteen_siblings.fewer_than_fifteen_siblings())

    def test_exactly_fifteen(self):
        self.assertFalse(us15_exactly_fifteen_siblings.fewer_than_fifteen_siblings())

    def test_many_more_than_fifteen(self):
        self.assertFalse(us15_many_more_than_fifteen_siblings.fewer_than_fifteen_siblings())