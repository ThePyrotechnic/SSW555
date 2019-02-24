from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('1', name = 'Mickey /Mouse/', sex = 'M', birthday = datetime(day = 20, month = 2, year = 1947)),
    Individual('2', name = 'Minnie /Mouse/', sex = 'F', birthday = datetime(day = 7, month = 10, year = 1947)),
    Individual('3', name = 'Pluto /Dog/', sex = 'M', birthday = datetime(day = 5, month = 6, year = 1965)),
    Individual('4', name = 'Donald /Duck/', sex = 'M', birthday = datetime(day = 30, month = 7, year = 1950)),
    Individual('5', name = "Daisy /Duck/", sex = 'F', birthday = datetime(day = 18, month = 11, year = 1952)),
    Individual('6', name = 'Huey / Duck/', sex = 'M', birthday = datetime(day = 29, month = 3, year = 1970)),
    Individual('7', name = 'Dewey /Duck/', sex = 'M', birthday = datetime(day = 14, month = 9, year = 1972)),
    Individual('8', name = 'Atilla /Duck/', sex = 'F', birthday = datetime(day = 10, month = 8, year = 1975)),
    Individual('9', name = 'Snow /White', sex = 'F', birthday = datetime(day = 6, month = 1, year = 1996)),
    Individual('10', name = 'Prince /Charming', sex = 'M', birthday = datetime(day = 13, month = 4, year = 1993))
]

_families = [
    Family('F1', husband = '1', wife = '2', children = ['3'], married = datetime(day = 1, month = 1 , year = 1963)),
    Family('F2', husband = '4', wife = '5', children = ['6', '7', '8'], married = datetime(day = 3, month = 5, year = 1967)),
    Family('F3', husband = '10', wife = '9', married = datetime(day = 24, month = 12, year = 2018))
]

of_age = Tree()

[of_age.add_individual(i) for i in _individuals]
[of_age.add_family(f) for f in _families]