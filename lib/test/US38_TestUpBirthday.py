import unittest
from datetime import datetime, timedelta

from lib.GedObjects import Tree, Family, Individual

today = datetime.now()
_individuals1 = [
    # all should be upcoming
    Individual('1', name='Randy /Pay/', birthday=today + timedelta(days=1), death=None),
    Individual('2', name='Rondy /Pay/', birthday=today + timedelta(days=2), death=None),
    Individual('3', name='Rendy /Day/', birthday=today + timedelta(days=3), death=None),
    Individual('4', name='Rindy /Day/', birthday=today + timedelta(days=4), death=None)
]

_individuals2 = [
    # some be upcoming
    Individual('1', name='Randy /Pay/', birthday=today + timedelta(days=46), death=None),
    Individual('2', name='Rondy /Pay/', birthday=today + timedelta(days=2), death=None),
    Individual('3', name='Rendy /Day/', birthday=today + timedelta(days=41), death=None),
    Individual('4', name='Rindy /Day/', birthday=today + timedelta(days=3), death=None)
]

_individuals3 = [
    # none of these ppl were born lol
    Individual('1', name='Randy /Pay/', death=None),
    Individual('2', name='Rondy /Pay/', death=None),
    Individual('3', name='Rendy /Day/', death=None),
    Individual('4', name='Rindy /Day/', death=None)
]

_individuals4 = [
    # some are dead
    Individual('1', name='Randy /Pay/', birthday=today + timedelta(days=45), death=datetime(1964, 6, 10, 0, 0)),
    Individual('2', name='Rondy /Pay/', birthday=today + timedelta(days=2), death=None),
    Individual('3', name='Rendy /Day/', birthday=today + timedelta(days=4), death=None),
    Individual('4', name='Rindy /Day/', birthday=today + timedelta(days=40), death=datetime(1967, 1, 10, 0, 0))
]

_individuals5 = [
    # all should fail
    Individual('1', name='Randy /Pay/', birthday=today + timedelta(days=40), death=datetime(1964, 6, 10, 0, 0)),
    Individual('2', name='Rondy /Pay/', birthday=today + timedelta(days=42), death=None),
    Individual('3', name='Rendy /Day/', birthday=today + timedelta(days=43), death=None),
    Individual('4', name='Rindy /Day/', birthday=today + timedelta(days=44), death=datetime(1967, 1, 10, 0, 0))
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
                         [['Randy /Pay/', (today + timedelta(days=1)).strftime(Tree._DATE_FORMAT)],
                          ['Rondy /Pay/', (today + timedelta(days=2)).strftime(Tree._DATE_FORMAT)],
                          ['Rendy /Day/', (today + timedelta(days=3)).strftime(Tree._DATE_FORMAT)],
                          ['Rindy /Day/', (today + timedelta(days=4)).strftime(Tree._DATE_FORMAT)]])

    def test_some_spouse(self):
        self.assertEqual(some_upcoming_tree.upcoming_birthday(),
                         [['Rondy /Pay/', (today + timedelta(days=2)).strftime(Tree._DATE_FORMAT)],
                          ['Rindy /Day/', (today + timedelta(days=3)).strftime(Tree._DATE_FORMAT)]])

    def test_some_under(self):
        self.assertEqual(no_birth_tree.upcoming_birthday(), [])

    def test_some_dead(self):
        self.assertEqual(some_dead_tree.upcoming_birthday(),
                         [['Rondy /Pay/', (today + timedelta(days=2)).strftime(Tree._DATE_FORMAT)],
                          ['Rendy /Day/', (today + timedelta(days=4)).strftime(Tree._DATE_FORMAT)]])

    def test_all_fail(self):
        self.assertEqual(no_upcoming_tree.upcoming_birthday(), [])
