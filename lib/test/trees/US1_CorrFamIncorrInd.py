from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('1', name = ' Dean /Adams/', sex = 'M', birthday = datetime(day = 20, month = 9, year = 2019)),
    Individual('2', name = 'Alex /Russo/', sex = 'F', birthday = datetime(day = 30, month = 1, year = 2020)),
    Individual('3', name = 'Ethan /Evans/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 2030 )),
    Individual('4', name = 'Lizzie /MacGuire', sex = 'F', birthday = datetime(day = 15, month = 3, year = 2020), death = datetime(day = 7, month = 10, year = 2003))
] 

_families = [
    Family('F1', married = datetime.datetime(2015, 1, 18, 0, 0)),
    Family('F2', married = datetime.datetime(1989, 10, 21, 0, 0), divorced = datetime.datetime(2007, 12, 8, 0, 0))
]

correct_incorrect = Tree()

[correct_incorrect.add_individual(i) for i in _individuals]
[correct_incorrect.add_family(f) for f in _families]