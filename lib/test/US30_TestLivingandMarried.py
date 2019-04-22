import unittest
from datetime import datetime
from lib.test.trees import us30_us34_tree
from lib.GedObjects import Tree, Family, Individual

_individuals1 = [
#all should work (complete)
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1963, 5, 10, 0, 0), death=None, spouse= 'F1'),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse= 'F1'),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse= 'F3'),
    Individual('6', name = 'John /Name/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse= 'F3')
]

_individuals2 = [
# only some have spouses 
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1963, 5, 10, 0, 0), death=None, spouse= None),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse= None),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1965, 7, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1966, 8, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse= None),
    Individual('6', name = 'John /Name/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse= 'F3')
]

_individuals3 = [
#some are dead
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(2011, 1, 14, 0, 0), spouse= 'F1'),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1964, 6, 10, 0, 0), death = None, spouse= 'F1'),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1965, 7, 10, 0, 0), death = datetime(2001, 9, 11, 0, 0), spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1966, 8, 10, 0, 0), death = None, spouse= 'F2'),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 1, 10, 0, 0), death = datetime(2016, 6, 9, 0, 0), spouse= 'F3'),
    Individual('6', name = 'John /Name/', birthday = datetime(1967, 1, 10, 0, 0), death = None, spouse= 'F3')
]

_individuals4 = [
#all should fail
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1963, 5, 10, 0, 0), death = datetime(2000, 10, 5, 0, 0), spouse = 'F1'),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1964, 6, 10, 0, 0), death=None, spouse= None),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1965, 7, 10, 0, 0), death = datetime(2010, 8, 15, 0, 0), spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1966, 8, 10, 0, 0), death= datetime(1999, 8, 26, 0, 0), spouse= None),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 1, 10, 0, 0), death=None, spouse= None),
    Individual('6', name = 'John /Name/', birthday = datetime(1967, 1, 10, 0, 0), death = datetime(2007, 4, 19, 0, 0), spouse= 'F3')
]

all_correct_tree = Tree()
some_spouse_tree = Tree()
some_dead_tree = Tree()
all_fail_tree = Tree()

[all_correct_tree.add_individual(i) for i in _individuals1]
[some_spouse_tree.add_individual(i) for i in _individuals2]
[some_dead_tree.add_individual(i) for i in _individuals3]
[all_fail_tree.add_individual(i) for i in _individuals4]

class TestLivingandSingle(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual([res[0] for res in all_correct_tree.list_living_married()], ['Linda /Burger/', 'Bob /Burger/', 'Shawn /Sheep/', 'Sherry /Sheep/', 'Jane /Name/', 'John /Name/'])

    def test_some_spouse(self):
        self.assertEqual([res[0] for res in some_spouse_tree.list_living_married()], ['Shawn /Sheep/', 'Sherry /Sheep/', 'John /Name/'])

    def test_some_dead(self):
        self.assertEqual([res[0] for res in some_dead_tree.list_living_married()], ['Bob /Burger/', 'Sherry /Sheep/', 'John /Name/'])
    
    def test_all_fail(self):
        self.assertEqual([res[0] for res in all_fail_tree.list_living_married()], [])
    
    def test_tree(self):
        self.assertEqual([res[0] for res in us30_us34_tree.list_living_married()],['Slither /Python/', 'Pie /Python/', 'Regina /Ruby/'])