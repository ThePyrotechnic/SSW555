import unittest
from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals1 = [
#all should be upcoming
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 2, 28, 0, 0), death=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 3, 10, 0, 0), death=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 3, 13, 0, 0), death=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 3, 14, 0, 0), death=None)
]

_individuals2 = [
#some be upcoming
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 3, 10, 0, 0), death=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 3, 14, 0, 0), death=None)
]

_individuals3 = [
#none of these ppl were born lol
    Individual('1', name = 'Randy /Pay/', death=None),
    Individual('2', name = 'Rondy /Pay/', death=None),
    Individual('3', name = 'Rendy /Day/', death=None),
    Individual('4', name = 'Rindy /Day/', death=None)
]

_individuals4 = [
#some are dead
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(1964, 6, 10, 0, 0)),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 3, 10, 0, 0), death=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 3, 13, 0, 0), death=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death = datetime(1967, 1, 10, 0, 0))
]

_individuals5 = [
#all should fail
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(1964, 6, 10, 0, 0)),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1997, 1, 10, 0, 0), death=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death = datetime(1967, 1, 10, 0, 0))
]

all_upcoming_tree = Tree()
some_upcoming_tree = Tree()
no_birth_tree = Tree()
some_dead_tree = Tree()
no_upcoming_tree = Tree()

[all_upcoming_tree.add_individual(i) for i in _individuals1]
[some_upcoming_tree.add_individual(i) for i in _individuals2]
[no_birth_tree.add_individual(i) for i in _individuals3]
[some_dead_tree.add_individual(i) for i in _individuals4]
[no_upcoming_tree.add_individual(i) for i in _individuals5]

class TestUpBirth(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual(all_upcoming_tree.upcoming_birthday(),
                         [['Randy /Pay/', '28-02-1963'], ['Rondy /Pay/', '10-03-1964'], ['Rendy /Day/', '13-03-1965'],['Rindy /Day/', '14-03-1966']])

    def test_some_spouse(self):
        self.assertEqual(some_upcoming_tree.upcoming_birthday(), [['Rondy /Pay/', '10-03-1964'], ['Rindy /Day/', '14-03-1966']])

    def test_some_under(self):
        self.assertEqual(no_birth_tree.upcoming_birthday(), [])
    
    def test_some_dead(self):
        self.assertEqual(some_dead_tree.upcoming_birthday(), [['Rondy /Pay/', '10-03-1964'], ['Rendy /Day/', '13-03-1965']])
    
    def test_all_fail(self):
        self.assertEqual(no_upcoming_tree.upcoming_birthday(), [])