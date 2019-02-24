from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('1', name = 'John /Dean/', sex = 'M', birthday = datetime(day = 20, month = 6, year = 1939)),
    Individual('2', name = 'Hannah /Montana/', sex = 'F', birthday = datetime(day = 30, month = 12, year = 1996)),
    Individual('3', name = 'Ethan /Evans/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 2018 )),
    Individual('4', name = 'Leslie /Maple/', sex = 'F', birthday = datetime(day = 12, month = 9, year = 1950))
] 

_families = [
    Family('F1', husband = '1', wife = '4', married = datetime.datetime(1973, 4, 11, 0, 0)),
    Family('F2', husband = '3', wife = '2', married = datetime.datetime(2000, 10, 31, 0, 0), divorced = datetime.datetime(2007, 12, 25, 0, 0))
]

correct_dates = Tree()

[correct_dates.add_individual(i) for i in _individuals]
[correct_dates.add_family(f) for f in _families]