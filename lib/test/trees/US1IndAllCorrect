from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('1', name = 'Super /Man/', sex = 'M', birthday = datetime(day = 28, month = 1, year = 1954), death = datetime(day = 5, month = 11, year = 2017)),
    Individual('2', name = 'Angela /Brown/', sex = 'F', birthday = datetime(day = 16, month = 2, year = 1987)),
    Individual('3', name = 'Jimmy /Gold/', sex = 'M', birthday = datetime(day = 1, month = 8, year = 1942), death = datetime(day = 23, month = 5, year = 2018 )),
    Individual('4', name = 'Carmen /Sandiego', sex = 'F', birthday = datetime(day = 11, month = 4, year = 2000))
] 


correct_inds = Tree()
[correct_inds.add_individual(i) for i in _individuals]