import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree


def _generic_test(tree):
    """
    Family information must conform to a predefined order
    Refer to Family.fam_to_list for the order
    """
    families_by_id = tree.individuals()
    prev_family = families_by_id[0]
    for family in families_by_id[1:]:
        assert family[0] >= prev_family[0]
        prev_family = family


class TestFamiliesById(unittest.TestCase):
    def test_michael_tree(self):
        _generic_test(michael_tree)

    def test_kristen_tree(self):
        _generic_test(kristen_tree)
