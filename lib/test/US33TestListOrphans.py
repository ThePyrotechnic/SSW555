import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import us09_birt_after_deaths


class TestListOrphans(unittest.TestCase):

    def test_no_orphans(self):
        self.assertEqual(kristen_tree.list_orphans(), [])

    def test_some_orphans(self):
        self.assertFalse(us09_birt_after_deaths.birth_bef_death())

