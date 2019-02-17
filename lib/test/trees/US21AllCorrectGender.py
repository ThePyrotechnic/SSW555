from datetime import datetime

from GedcomParser.SSW555.lib.GedObjects import Tree
from GedcomParser.SSW555.lib.GedObjects import Family
from GedcomParser.SSW555.lib.GedObjects import Individual

_individuals = [
    Individual('1', name='Evan /Doe/', sex='M', birthday=datetime(day=12, month=4, year=1998)),
    Individual('2', name='Elena /Doe/', sex='F', birthday=datetime(day=15, month=9, year=2000)),
    Individual('3', name='John /Doe/', sex='M', birthday=datetime(day=2, month=3, year=1962)),
    Individual('4', name='Jane /Doe/', sex='F', birthday=datetime(day=2, month=3, year=1962))
]

_families = [
    Family('F1', husband_id='3', wife_id='4', children=['1', '2'])
]

all_correct_gender = Tree()

[all_correct_gender .add_individual(i) for i in _individuals]
[all_correct_gender .add_family(f) for f in _families]
