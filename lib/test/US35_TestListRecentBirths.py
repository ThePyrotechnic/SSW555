import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import sprint_one_tree
from lib.test.trees import sprint_two_tree
from lib.GedObjects import Tree, Family, Individual
from datetime import datetime, timedelta
import lib.GedConstants as gc

birth1 = datetime.today()
birth2 = datetime.today() - timedelta(days=1)
birth3 = datetime.today() - timedelta(days=29)
birth4 = datetime.today() - timedelta(days=15)

_recently_born_individuals = [
    Individual('1', name='Randy /Pay/', birthday=birth1),
    Individual('2', name='Rondy /Pay/', birthday=birth2),
    Individual('3', name='Rendy /Day/', birthday=birth3),
    Individual('4', name='Rindy /Day/', birthday=birth4)
]

all_recent_births_tree = Tree()

[all_recent_births_tree.add_individual(i) for i in _recently_born_individuals]

birth5 = datetime.today()
birth6 = datetime.today() - timedelta(days=40)
birth7 = datetime.today() - timedelta(days=27)
birth8 = datetime.today() - timedelta(days=1000)

some_recently_born_individuals = [
    Individual('5', name='Mickey /Mouse/', birthday=birth5),
    Individual('6', name='Minnie /Mouse/', birthday=birth6),
    Individual('7', name='John /Mouse/', birthday=birth7),
    Individual('8', name='Jane /Mouse/', birthday=birth8)
]

some_recent_births_tree = Tree()

[some_recent_births_tree.add_individual(i) for i in some_recently_born_individuals]


class TestListRecentBirths(unittest.TestCase):
    def test_michael_tree(self):
        self.assertEqual(michael_tree.list_recent_births(), [])

    def test_kristen_tree(self):
        self.assertEqual(kristen_tree.list_recent_births(), [])

    def test_sprint_one_tree(self):
        self.assertEqual(sprint_one_tree.list_recent_births(), [])

    # def test_sprint_two_tree(self):
    #     self.assertEqual(sprint_two_tree.list_recent_births(), [
    #         ['us36_parent1', 'Homer /Simpson/', 'M', '1965-11-30', 53, False, '2019-03-20', 'NA', 'us36_fam'],
    #         ['us36_parent2', 'Marge /Simpson/', 'F', '1967-08-13', 51, False, '2019-03-21', 'NA', 'us36_fam']
    #     ])

    def test_all_recent_births_tree(self):
        self.assertEqual(all_recent_births_tree.list_recent_births(), [
            ['1', 'Randy /Pay/', 'NA', birth1.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
            ['2', 'Rondy /Pay/', 'NA', birth2.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
            ['3', 'Rendy /Day/', 'NA', birth3.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
            ['4', 'Rindy /Day/', 'NA', birth4.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
        ])

    def test_some_recent_births_tree(self):
        self.assertEqual(some_recent_births_tree.list_recent_births(), [
            ['5', 'Mickey /Mouse/', 'NA', birth5.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
            ['7', 'John /Mouse/', 'NA', birth7.strftime(gc.DATE_FORMAT), 0, True, 'NA', 'NA', 'NA'],
        ])
