import unittest

from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals = [
    Individual('1', name = 'Toddy /Frod/', sex = 'M', birthday = datetime(day = 20, month = 1, year = 1947)),
    Individual('2', name = 'Loddy /Frod/', sex = 'F', birthday = datetime(day = 20, month = 2, year = 1948)),
    Individual('3', name = 'Moosy /Goose/', sex = 'M', birthday = datetime(day = 10, month = 3, year = 1949)),
    Individual('4', name = 'Toosy /Goose/', sex = 'F', birthday = datetime(day = 25, month = 4, year = 1950)),
    Individual('5', name = 'Becky /Tech/', sex = 'M', birthday = datetime(day = 25, month = 5, year = 1951)),
    Individual('6', name = 'Lecky /Tech/', sex = 'F', birthday = datetime(day = 10, month = 6, year = 1950)),

]

_families = [
    Family('F1', husband_id = '1', wife_id = '2', children = '2', married = datetime(day = 1, month = 1 , year = 1948)),
    Family('F2', husband_id = '3', wife_id = '4', married = datetime(day = 1, month = 1 , year = 1963)),
    Family('F3', husband_id = '5', wife_id = '6', children = '5', married = datetime(day = 1, month = 1 , year = 1951)),
]

in_wed = Tree()

[in_wed.add_individual(i) for i in _individuals]
[in_wed.add_family(f) for f in _families]


_individuals2 = [
    Individual('a', name = 'Toddy /Frod/', sex = 'M', birthday = datetime(day = 20, month = 1, year = 1947)),
    Individual('b', name = 'Loddy /Frod/', sex = 'F', birthday = datetime(day = 20, month = 2, year = 1948)),
    Individual('c', name = 'Moosy /Goose/', sex = 'M', birthday = datetime(day = 10, month = 3, year = 1949)),
    Individual('d', name = 'Toosy /Goose/', sex = 'F', birthday = datetime(day = 25, month = 4, year = 1950)),
    Individual('e', name = 'Becky /Tech/', sex = 'M', birthday = datetime(day = 25, month = 5, year = 1951)),
    Individual('f', name = 'Lecky /Tech/', sex = 'F', birthday = datetime(day = 10, month = 6, year = 1950)),

]

_families2 = [
    Family('F1', husband_id = 'a', wife_id = 'b', children = 'c', married = datetime(day = 1, month = 1 , year = 1948)),
    Family('F2', husband_id = 'c', wife_id = 'd', married = datetime(day = 1, month = 1 , year = 1963)),
    Family('F3', husband_id = 'e', wife_id = 'f', children = 'a', married = datetime(day = 1, month = 1 , year = 1951)),
]

no_marrs_to_children = Tree()

[no_marrs_to_children.add_individual(i) for i in _individuals2]
[no_marrs_to_children.add_family(f) for f in _families2]

class TestParentNotSpouse(unittest.TestCase):
    def test_some_marriages_to_children(self):
        self.assertFalse(in_wed.parent_not_spouse())

    def test_no_marriages_to_children(self):
        self.assertTrue(no_marrs_to_children.parent_not_spouse())

