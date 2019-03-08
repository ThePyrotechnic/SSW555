import unittest

from lib.test.trees import kristen_tree
from lib.test.trees import michael_tree
from lib.test.trees import sprint_one_tree
from lib.test.trees import sprint_two_tree
from lib.test.trees import us36_some_recent_deaths
from lib.test.trees import us36_all_recent_deaths
from lib.GedObjects import Tree, Family, Individual
from datetime import datetime, timedelta

death1 = datetime.today()
death2 = datetime.today() - timedelta(days=1)
death3 = datetime.today() - timedelta(days=29)
death4 = datetime.today() - timedelta(days=15)

_recently_dead_individuals = [
    Individual('1', name='Randy /Pay/', birthday=datetime(day=29, month=9, year=1998), death=death1),  # 80 years old
    Individual('2', name='Rondy /Pay/', birthday=datetime(day=29, month=9, year=1998), death=death2),
    Individual('3', name='Rendy /Day/', birthday=datetime(day=29, month=9, year=1998), death=death3),
    Individual('4', name='Rindy /Day/', birthday=datetime(day=29, month=9, year=1998), death=death4)
]

all_recent_deaths_tree = Tree()

[all_recent_deaths_tree.add_individual(i) for i in _recently_dead_individuals]


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

    def test_some_recent_deaths(self):
        self.assertEqual(us36_some_recent_deaths.list_recent_deaths(), [
            ['@I1@', 'Michael /Manis/', 'M', '1998-03-23', 20, False, '2019-03-01', '@F1@', 'NA'],
            ['@I5@', 'Daniel /Doe/', 'M', '1944-12-12', 74, False, '2019-02-28', 'NA', '@F2@'],
            ['@I7@', 'Joseph /Dane/', 'M', '1945-06-18', 73, False, '2019-02-16', 'NA', '@F3@']
        ])

    def test_all_recent_deaths(self):
        self.assertEqual(us36_all_recent_deaths.list_recent_deaths(), [
            ['@I1@', 'Michael /Manis/', 'M', '1998-03-23', 20, False, '2019-03-01', '@F1@', 'NA'],
            ['@I2@', 'Robert /Manis/', 'M', '1963-03-02', 55, False, '2019-02-26', 'NA', '@F1@'],
            ['@I3@', 'Susan /Farinelli/', 'F', '1963-02-02', 56, False, '2019-02-26', '@F2@', '@F1@'],
            ['@I4@', 'Robert /Manis/', 'M', '1998-03-23', 20, False, '2019-02-25', '@F1@', 'NA'],
            ['@I5@', 'Daniel /Doe/', 'M', '1944-12-12', 74, False, '2019-02-28', 'NA', '@F2@'],
            ['@I6@', 'Jane /Don/', 'F', '1944-01-28', 75, False, '2019-02-27', 'NA', '@F3@'],
            ['@I7@', 'Joseph /Dane/', 'M', '1945-06-18', 73, False, '2019-02-16', 'NA', '@F3@'],
            # ['@I8@', 'Jack /Dane/', 'M', '1961-08-02', 57, False, '2019-02-03', '@F3@', 'NA'],
        ])

    def test_all_recent_deaths_tree(self):
        self.assertEqual(all_recent_deaths_tree.list_recent_deaths(), [
            ['1', 'Randy /Pay/', 'NA', '1998-09-29', 20, False, death1.strftime(Tree._DATE_FORMAT), 'NA', 'NA'],
            ['2', 'Rondy /Pay/', 'NA', '1998-09-29', 20, False, death2.strftime(Tree._DATE_FORMAT), 'NA', 'NA'],
            ['3', 'Rendy /Day/', 'NA', '1998-09-29', 20, False, death3.strftime(Tree._DATE_FORMAT), 'NA', 'NA'],
            ['4', 'Rindy /Day/', 'NA', '1998-09-29', 20, False, death4.strftime(Tree._DATE_FORMAT), 'NA', 'NA'],
        ])
