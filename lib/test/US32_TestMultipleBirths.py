import unittest
from datetime import datetime
from lib.test.trees import sprint_two_tree
from lib.GedObjects import Tree, Family, Individual

class TestLivingandSingle(unittest.TestCase):

    def test_all_kids_same_birth(self):
        self.assertEqual(sprint_two_tree.multiple_births(), [['Michael /Phillips/', '23-03-1998'],
        ['Robert /Manis/', '23-03-1998'], ['Thomas /Dane/', '08-05-1945'], ['Thomas /Dane/', '08-05-1945'], ['Albert /Tang/', '18-04-1997'],
        ['Lucille /Tang/', '18-04-1997']])
