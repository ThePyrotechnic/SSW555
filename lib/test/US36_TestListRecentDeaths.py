import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import sprint_one_tree
from lib.test.trees import sprint_two_tree
from lib.GedObjects import Tree, Family, Individual
from datetime import datetime, timedelta
import lib.GedConstants as gc

death1 = datetime.today()
death2 = datetime.today() - timedelta(days=1)
death3 = datetime.today() - timedelta(days=29)
death4 = datetime.today() - timedelta(days=15)

_recently_dead_individuals = [
    Individual('1', name='Randy /Pay/', birthday=datetime(day=29, month=9, year=1998), death=death1),
    Individual('2', name='Rondy /Pay/', birthday=datetime(day=29, month=9, year=1998), death=death2),
    Individual('3', name='Rendy /Day/', birthday=datetime(day=29, month=9, year=1998), death=death3),
    Individual('4', name='Rindy /Day/', birthday=datetime(day=29, month=9, year=1998), death=death4)
]

all_recent_deaths_tree = Tree()

[all_recent_deaths_tree.add_individual(i) for i in _recently_dead_individuals]

death5 = datetime.today()
death6 = datetime.today() - timedelta(days=40)
death7 = datetime.today() - timedelta(days=27)
death8 = datetime.today() - timedelta(days=1000)

some_recently_dead_individuals = [
    Individual('5', name='Mickey /Mouse/', birthday=datetime(day=29, month=9, year=1998), death=death5),
    Individual('6', name='Minnie /Mouse/', birthday=datetime(day=29, month=9, year=1998), death=death6),
    Individual('7', name='John /Mouse/', birthday=datetime(day=29, month=9, year=1998), death=death7),
    Individual('8', name='Jane /Mouse/', birthday=datetime(day=29, month=9, year=1998), death=death8)
]

some_recent_deaths_tree = Tree()

[some_recent_deaths_tree.add_individual(i) for i in some_recently_dead_individuals]

class TestListRecentDeaths(unittest.TestCase):
    def test_michael_tree(self):
        self.assertEqual(michael_tree.list_recent_deaths(), [])

    def test_kristen_tree(self):
        self.assertEqual(kristen_tree.list_recent_deaths(), [])

    def test_sprint_one_tree(self):
        self.assertEqual(sprint_one_tree.list_recent_deaths(), [])

    def test_sprint_two_tree(self):
        self.assertEqual(sprint_two_tree.list_recent_deaths(), [
            ['us36_parent1', 'Homer /Simpson/', 'M', '1965-11-30', 53, False, '2019-02-24', 'NA', 'us36_fam'],
            ['us36_parent2', 'Marge /Simpson/', 'F', '1967-08-13', 51, False, '2019-02-27', 'NA', 'us36_fam']
        ])

    def test_all_recent_deaths_tree(self):
        self.assertEqual(all_recent_deaths_tree.list_recent_deaths(), [
            ['1', 'Randy /Pay/', 'NA', '1998-09-29', 20, False, death1.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
            ['2', 'Rondy /Pay/', 'NA', '1998-09-29', 20, False, death2.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
            ['3', 'Rendy /Day/', 'NA', '1998-09-29', 20, False, death3.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
            ['4', 'Rindy /Day/', 'NA', '1998-09-29', 20, False, death4.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
        ])

    def test_some_recent_deaths_tree(self):
        self.assertEqual(some_recent_deaths_tree.list_recent_deaths(), [
            ['5', 'Mickey /Mouse/', 'NA', '1998-09-29', 20, False, death5.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
            ['7', 'John /Mouse/', 'NA', '1998-09-29', 20, False, death7.strftime(gc.DATE_FORMAT), 'NA', 'NA'],
        ])
