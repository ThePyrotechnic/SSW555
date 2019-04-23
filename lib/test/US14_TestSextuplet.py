import unittest

from datetime import datetime

from lib.GedObjects import Tree, Family, Individual

_individuals = [
    Individual('1', name = 'Monty /Python//', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('2', name = 'Ronty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('3', name = 'Tonty /Python/', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('4', name = 'Fonty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('5', name = 'Lonty /Python/', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('6', name = 'Zonty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1999)),
]

_families = [
    Family('F1', children = ['1','2','3','4','5','6'])
]

sextuplet_check = Tree()

[sextuplet_check.add_individual(i) for i in _individuals]
[sextuplet_check.add_family(f) for f in _families]


_individuals2 = [
    Individual('1', name = 'Monty /Python//', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1999)),
    Individual('2', name = 'Ronty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1998)),
    Individual('3', name = 'Tonty /Python/', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1997)),
    Individual('4', name = 'Fonty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1996)),
    Individual('5', name = 'Lonty /Python/', sex = 'M', birthday = datetime(day = 23, month = 3, year = 1995)),
    Individual('6', name = 'Zonty /Python/', sex = 'F', birthday = datetime(day = 23, month = 3, year = 1994)),
]

_families2 = [
    Family('F1', children = ['1','2','3','4','5','6'])
]

no_sextuplet = Tree()

[no_sextuplet.add_individual(i) for i in _individuals2]
[no_sextuplet.add_family(f) for f in _families2]

class TestParentsNotOld(unittest.TestCase):
    def test_not_sextuplet(self):
        self.assertTrue(no_sextuplet.no_sextuplets())

    def test_sextuplet_exists(self):
        self.assertFalse(sextuplet_check.no_sextuplets())