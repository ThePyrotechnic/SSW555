import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree


def _generic_test(tree):
    """
    Individual information must conform to a predefined order
    Refer to Individual.indi_to_list for the order
    """
    siblings_by_age = tree.siblings_by_age()
    prev_sibling = siblings_by_age[0]
    for sibling in siblings_by_age[1:]:
        assert sibling[4] >= prev_sibling[4]
        prev_sibling = sibling


class TestSiblingsByAge(unittest.TestCase):

    def test_michael_tree(self):
        _generic_test(michael_tree)

    def test_kristen_tree(self):
        _generic_test(kristen_tree)
