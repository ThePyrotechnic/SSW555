import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import us23_two_individuals_with_same_name_and_birth_date
from lib.test.trees import us23_four_individuals_with_same_name_and_birth_date


class TestFewerThaFifteenSiblings(unittest.TestCase):

    def test_no_dups(self):
        self.assertTrue(kristen_tree.unique_stuff())

    def test_no_dups_2(self):
        self.assertTrue(michael_tree.unique_stuff())

    def test_two_individuals_with_same_name_and_birth_date(self):
        self.assertFalse(us23_two_individuals_with_same_name_and_birth_date.unique_stuff())

    def test_four_individuals_with_same_name_and_birth_date(self):
        self.assertFalse(us23_four_individuals_with_same_name_and_birth_date.unique_stuff())
