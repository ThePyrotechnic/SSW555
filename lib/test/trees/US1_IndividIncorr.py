from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Individual

_individuals = [
    Individual('1', name = 'Dill /Pickles/', sex = 'M', birthday = datetime(day = 20, month = 6, year = 2020)),
    Individual('2', name = 'Sean /John/', sex = 'F', birthday = datetime(day = 30, month = 12, year = 2091)),
    Individual('3', name = 'Paul /Matthews/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 3019 ))
] 

incorrect_indivs = Tree()
[incorrect_indivs.add_individual(i) for i in _individuals]