import unittest
from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals1 = [
#all should work (complete)
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death=None, spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse=None),
    Individual('6', name = 'Tandy /Lay/', birthday = datetime(1968, 2, 10, 0, 0), death=None, spouse=None),
    Individual('7', name = 'Tindy /May/', birthday = datetime(1969, 3, 10, 0, 0), death=None, spouse=None),
    Individual('8', name = 'Tendy /May/', birthday = datetime(1970, 4, 10, 0, 0), death=None, spouse=None)
]

_individuals2 = [
#some have spouses (complete)
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death=None, spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse='@F4@'),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse='@F5@'),
    Individual('6', name = 'Tandy /Lay/', birthday = datetime(1968, 2, 10, 0, 0), death=None, spouse='@F7@'),
    Individual('7', name = 'Tindy /May/', birthday = datetime(1969, 3, 10, 0, 0), death=None, spouse=None),
    Individual('8', name = 'Tendy /May/', birthday = datetime(1970, 4, 10, 0, 0), death=None, spouse='@F9@')
]

_individuals3 = [
#some are under 30 (complete)
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1993, 5, 10, 0, 0), death=None, spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1995, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1997, 1, 10, 0, 0), death=None, spouse=None),
    Individual('6', name = 'Tandy /Lay/', birthday = datetime(1968, 2, 10, 0, 0), death=None, spouse=None),
    Individual('7', name = 'Tindy /May/', birthday = datetime(1999, 3, 10, 0, 0), death=None, spouse=None),
    Individual('8', name = 'Tendy /May/', birthday = datetime(2005, 4, 10, 0, 0), death=None, spouse=None)
]

_individuals4 = [
#some are dead
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(1964, 6, 10, 0, 0), spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death = datetime(1967, 1, 10, 0, 0), spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse=None),
    Individual('6', name = 'Tandy /Lay/', birthday = datetime(1968, 2, 10, 0, 0), death = datetime(1969, 3, 10, 0, 0), spouse=None),
    Individual('7', name = 'Tindy /May/', birthday = datetime(1969, 3, 10, 0, 0), death = datetime(1970, 4, 10, 0, 0), spouse=None),
    Individual('8', name = 'Tendy /May/', birthday = datetime(1970, 4, 10, 0, 0), death=None, spouse=None)
]

_individuals5 = [
#all should fail
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(1964, 6, 10, 0, 0), spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse='@F5@'),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1997, 1, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death = datetime(1967, 1, 10, 0, 0), spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse='@F7@'),
    Individual('6', name = 'Tandy /Lay/', birthday = datetime(1968, 2, 10, 0, 0), death = datetime(1969, 3, 10, 0, 0), spouse=None),
    Individual('7', name = 'Tindy /May/', birthday = datetime(1969, 3, 10, 0, 0), death = datetime(1970, 4, 10, 0, 0), spouse=None),
    Individual('8', name = 'Tendy /May/', birthday = datetime(2005, 4, 10, 0, 0), death=None, spouse=None)
]

all_correct_tree = Tree()
some_spouse_tree = Tree()
some_under_tree = Tree()
some_dead_tree = Tree()
all_fail_tree = Tree()

[all_correct_tree.add_individual(i) for i in _individuals1]
[some_spouse_tree.add_individual(i) for i in _individuals2]
[some_under_tree.add_individual(i) for i in _individuals3]
[some_dead_tree.add_individual(i) for i in _individuals4]
[all_fail_tree.add_individual(i) for i in _individuals5]

class TestLivingandSingle(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual(all_correct_tree.living_single(), ['Randy /Pay/', 'Rondy /Pay/', 'Rendy /Day/', 'Rindy /Day/', 'Rundy /Lay/', 'Tandy /Lay/', 'Tindy /May/', 'Tendy /May/'])

    def test_some_spouse(self):
        self.assertEqual(some_spouse_tree.living_single(), ['Randy /Pay/', 'Rendy /Day/', 'Rindy /Day/', 'Tindy /May/'])

    def test_some_under(self):
        self.assertEqual(some_under_tree.living_single(), ['Rondy /Pay/', 'Rindy /Day/', 'Tandy /Lay/'])
    
    def test_some_dead(self):
        self.assertEqual(some_dead_tree.living_single(), ['Rondy /Pay/', 'Rendy /Day/', 'Rundy /Lay/', 'Tendy /May/'])
    
    def test_all_fail(self):
        self.assertEqual(all_fail_tree.living_single(), [])