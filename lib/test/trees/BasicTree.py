from datetime import datetime

from lib.GedObjects import Individual, Family, Tree

_individuals = [
    Individual('1', name='Michael /Manis/', sex='M', birthday=datetime(day=23, month=3, year=1998)),
    Individual('2', name='Robby /Manis', sex='M', birthday=datetime(day=23, month=3, year=1998)),
    Individual('3', name='Bob /Manis/', sex='M', birthday=datetime(day=2, month=3, year=1962)),
    Individual('4', name='Susan /Manis/', sex='F', birthday=datetime(day=2, month=3, year=1962))
]

_families = [
    Family('F1', husband_id='3', wife_id='4', children=['1', '2'])
]

basic_tree = Tree()

[basic_tree.add_individual(i) for i in _individuals]
[basic_tree.add_family(f) for f in _families]
