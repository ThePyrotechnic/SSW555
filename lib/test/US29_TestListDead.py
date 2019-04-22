import unittest
from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals1 = [
#all should work (complete)
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death=None, spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse=None)
]

_individuals2 = [
#some are dead
    Individual('1', name = 'Randy /Pay/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(1964, 6, 10, 0, 0), spouse=None),
    Individual('2', name = 'Rondy /Pay/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse=None),
    Individual('3', name = 'Rendy /Day/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse=None),
    Individual('4', name = 'Rindy /Day/', birthday = datetime(1966, 8, 10, 0, 0), death = datetime(1967, 1, 10, 0, 0), spouse=None),
    Individual('5', name = 'Rundy /Lay/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse=None),
]

all_alive_tree = Tree()
some_dead_tree = Tree()

[all_alive_tree.add_individual(i) for i in _individuals1]
[some_dead_tree.add_individual(i) for i in _individuals2]

class TestLivingandSinglListDead(unittest.TestCase):

    def test_all_alive(self):
        self.assertEqual([res[0] for res in all_alive_tree.list_deceased()], [])

    def test_some_dead(self):
        self.assertEqual([res[0] for res in some_dead_tree.list_deceased()], ['Randy /Pay/', 'Rindy /Day/'])