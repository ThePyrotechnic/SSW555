import unittest
from datetime import datetime
from lib.test.trees import us30_us34_tree
from lib.GedObjects import Tree, Family, Individual

_families = [
    Family('F1', husband_id = '2', wife_id = '1', married = datetime(day = 1, month = 12 , year = 1980)),
    Family('F2', husband_id = '3', wife_id = '4', married = datetime(day = 15, month = 9 , year = 1993)),
    Family('F3', husband_id = '6', wife_id = '5', married = datetime(day = 28, month = 4 , year = 2014))
]
_individuals1 = [
#all should work (complete)
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1960, 5, 10, 0, 0), death=None, spouse= 'F1'),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1935, 6, 15, 0, 0), death=None, spouse= 'F1'),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1960, 7, 12, 0, 0), death=None, spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1978, 8, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 3, 25, 0, 0), death=None, spouse= 'F3'),
    Individual('6', name = 'John /Name/', birthday = datetime(1993, 1, 30, 0, 0), death=None, spouse= 'F3')
]

_individuals2 = [
# only some individuals have a large age gap 
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1963, 5, 16, 0, 0), death=None, spouse= None),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1964, 6, 15, 0, 0), death=None, spouse= None),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1960, 4, 10, 0, 0), death=None, spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1978, 8, 20, 0, 0), death=None, spouse= 'F2'),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1967, 11, 11, 0, 0), death=None, spouse= None),
    Individual('6', name = 'John /Name/', birthday = datetime(1993, 9, 30, 0, 0), death=None, spouse= 'F3')
]

_individuals4 = [
#all should fail
    Individual('1', name = 'Linda /Burger/', birthday = datetime(1960, 1, 13, 0, 0), death = datetime(2000, 10, 5, 0, 0), spouse = 'F1'),
    Individual('2', name = 'Bob /Burger/', birthday = datetime(1958, 2, 4, 0, 0), death=None, spouse= None),
    Individual('3', name = 'Shawn /Sheep/', birthday = datetime(1969, 3, 29, 0, 0), death = datetime(2010, 8, 15, 0, 0), spouse= 'F2'),
    Individual('4', name = 'Sherry /Sheep/', birthday = datetime(1972, 10, 17, 0, 0), death= datetime(1999, 8, 26, 0, 0), spouse= None),
    Individual('5', name = 'Jane /Name/', birthday = datetime(1987, 11, 8, 0, 0), death=None, spouse= None),
    Individual('6', name = 'John /Name/', birthday = datetime(1986, 12, 31, 0, 0), death = datetime(2007, 4, 19, 0, 0), spouse= 'F3')
]

all_correct_tree = Tree()
some_correct_tree = Tree()
all_fail_tree = Tree()

[all_correct_tree.add_individual(i) for i in _individuals1]
[all_correct_tree.add_family(f) for f in _families]
[some_correct_tree.add_individual(i) for i in _individuals2]
[some_correct_tree.add_family(f) for f in _families]
[all_fail_tree.add_individual(i) for i in _individuals4]
[all_fail_tree.add_family(f) for f in _families]

class TestLivingandSingle(unittest.TestCase):

    def test_all_correct(self):
        self.assertEqual([res[:-1] for res in all_correct_tree.list_large_age_difference()], [['Bob /Burger/', '15-06-1935', '01-12-1980'], ['Linda /Burger/', '10-05-1960', '01-12-1980'],
        ['Shawn /Sheep/','12-07-1960', '15-09-1993'], ['Sherry /Sheep/','10-08-1978', '15-09-1993'], 
        ['John /Name/','30-01-1993', '28-04-2014'], ['Jane /Name/','25-03-1967', '28-04-2014']])

    def test_some_normal(self):
        self.assertEqual([res[:-1] for res in some_correct_tree.list_large_age_difference()], [ ['Shawn /Sheep/','10-04-1960', '15-09-1993'], ['Sherry /Sheep/','20-08-1978', '15-09-1993'],
        ['John /Name/','30-09-1993', '28-04-2014'], ['Jane /Name/','11-11-1967', '28-04-2014']])

    def test_all_fail(self):
        self.assertEqual([res[:-1] for res in all_fail_tree.list_large_age_difference()], [])
    
    def test_import_tree(self):
        self.assertEqual([res[:-1] for res in us30_us34_tree.list_large_age_difference()],[['Slither /Python/', '21-03-1950', '28-02-1985'], ['Pie /Python/', '13-07-1968', '28-02-1985'],
        ['Jake /Java/', '21-08-1962', '23-02-1979'], ['Julie /Java/', '14-02-1940', '23-02-1979']])