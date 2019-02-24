import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree


def _generic_test(tree):
    """
    Individual information must conform to a predefined order
    Refer to Individual.indi_to_list for the order
    """
    individuals_by_id = tree.individuals()
    prev_individual = individuals_by_id[0]
    for individual in individuals_by_id[1:]:
        assert individual[0] >= prev_individual[0]
        prev_individual = individual


class TestIndividualsById(unittest.TestCase):
    def test_michael_tree(self):
        _generic_test(michael_tree)

    def test_kristen_tree(self):
        _generic_test(kristen_tree)
