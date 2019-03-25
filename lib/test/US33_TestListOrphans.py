import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import sprint_one_tree
from lib.test.trees import sprint_two_tree


class TestListOrphans(unittest.TestCase):
    def test_michael_tree(self):
        self.assertListEqual(michael_tree.list_orphans(), [])

    def test_kristen_tree(self):
        self.assertListEqual(kristen_tree.list_orphans(), [])

    def test_sprint_one_tree(self):
        self.assertListEqual(sprint_one_tree.list_orphans(), [])

    def test_sprint_two_tree(self):
        self.assertListEqual(sprint_two_tree.list_orphans(), [['us33_orphan', 'orphan /US33/', 'M', '2018-01-01', 1, True, 'NA', 'us33_fam', 'NA']])
