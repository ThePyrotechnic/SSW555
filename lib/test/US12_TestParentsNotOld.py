import unittest

from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals = [
    Individual('1', name = 'Michelle /Obama/', sex = 'M', birthday = datetime(day = 20, month = 1, year = 1947)),
    Individual('2', name = 'Barack /Obama/', sex = 'F', birthday = datetime(day = 20, month = 2, year = 1948)),
    Individual('3', name = 'Bill /Clinton/', sex = 'M', birthday = datetime(day = 10, month = 3, year = 1988)),
    Individual('4', name = 'Hillary /Clinton/', sex = 'F', birthday = datetime(day = 25, month = 4, year = 1999)),
    Individual('5', name = 'Lorry /Tot/', sex = 'M', birthday = datetime(day = 25, month = 5, year = 1951)),
    Individual('6', name = 'Borry /Tot/', sex = 'F', birthday = datetime(day = 10, month = 6, year = 1950)),
]

_families = [
    Family('F1', husband_id = '1', wife_id = '2', children = '3', married = datetime(day = 1, month = 1 , year = 1948)),
    Family('F2', husband_id = '5', wife_id = '6', children = '4', married = datetime(day = 1, month = 1 , year = 1963)),
]

parents_age_okay = Tree()

[parents_age_okay.add_individual(i) for i in _individuals]
[parents_age_okay.add_family(f) for f in _families]


_individuals2 = [
    Individual('1', name = 'Michelle /Obama/', sex = 'M', birthday = datetime(day = 20, month = 1, year = 1947)),
    Individual('2', name = 'Barack /Obama/', sex = 'F', birthday = datetime(day = 20, month = 2, year = 1948)),
    Individual('3', name = 'Bill /Clinton/', sex = 'M', birthday = datetime(day = 10, month = 3, year = 2009)),
    Individual('4', name = 'Hillary /Clinton/', sex = 'F', birthday = datetime(day = 25, month = 4, year = 2012)),
    Individual('5', name = 'Lorry /Tot/', sex = 'M', birthday = datetime(day = 25, month = 5, year = 1951)),
    Individual('6', name = 'Borry /Tot/', sex = 'F', birthday = datetime(day = 10, month = 6, year = 1950)),
]

_families2 = [
    Family('F1', husband_id = '1', wife_id = '2', children = '3', married = datetime(day = 1, month = 1 , year = 1948)),
    Family('F2', husband_id = '5', wife_id = '6', children = '4', married = datetime(day = 1, month = 1 , year = 1963)),
]

parents_old = Tree()

[parents_old.add_individual(i) for i in _individuals2]
[parents_old.add_family(f) for f in _families2]

class TestParentsNotOld(unittest.TestCase):
    def test_parents_are_too_old(self):
        self.assertTrue(parents_age_okay.par_not_old())

    def test_parents_not_too_old(self):
        self.assertFalse(parents_old.par_not_old())

