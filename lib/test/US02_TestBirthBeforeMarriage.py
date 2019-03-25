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
    Family('F1', husband_id = '1', wife_id = '2', married = datetime(day = 1, month = 1 , year = 1948)),
    Family('F2', husband_id = '3', wife_id = '4', married = datetime(day = 1, month = 1 , year = 1963)),
    Family('F3', husband_id = '5', wife_id = '6', married = datetime(day = 1, month = 1 , year = 1951)),
]

born_wed = Tree()

[born_wed.add_individual(i) for i in _individuals]
[born_wed.add_family(f) for f in _families]


_individuals2 = [
    Individual('a', name = 'Toddy /Frod/', sex = 'M', birthday = datetime(day = 20, month = 1, year = 1947)),
    Individual('b', name = 'Loddy /Frod/', sex = 'F', birthday = datetime(day = 20, month = 2, year = 1948)),
    Individual('c', name = 'Moosy /Goose/', sex = 'M', birthday = datetime(day = 10, month = 3, year = 1949)),
    Individual('d', name = 'Toosy /Goose/', sex = 'F', birthday = datetime(day = 25, month = 4, year = 1950)),
    Individual('e', name = 'Becky /Tech/', sex = 'M', birthday = datetime(day = 25, month = 5, year = 1951)),
    Individual('f', name = 'Lecky /Tech/', sex = 'F', birthday = datetime(day = 10, month = 6, year = 1950)),

]

_families2 = [
    Family('F1', husband_id = 'a', wife_id = 'b', married = datetime(day = 1, month = 1 , year = 1970)),
    Family('F2', husband_id = 'c', wife_id = 'd', married = datetime(day = 1, month = 1 , year = 1963)),
    Family('F3', husband_id = 'e', wife_id = 'f', married = datetime(day = 1, month = 1 , year = 1981)),
]

valid_dates = Tree()

[valid_dates.add_individual(i) for i in _individuals2]
[valid_dates.add_family(f) for f in _families2]

class Test_Birth_Before_Marriage(unittest.TestCase):
    def test_invalid_dates(self):
        self.assertFalse(born_wed.birth_pre_marriage())

    def test_valid_dates(self):
        self.assertTrue(valid_dates.birth_pre_marriage())