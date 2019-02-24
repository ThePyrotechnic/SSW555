from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('1a1a', name='Evan /Doe/', sex='M', birthday=datetime(day=12, month=4, year=1998)),
    Individual('2b2b', name='Elena /Doe/', sex='F', birthday=datetime(day=15, month=9, year=2000)),
    Individual('3c3c', name='John /Doe/', sex='F', birthday=datetime(day=2, month=3, year=1962)),
    Individual('4d4d', name='Jane /Doe/', sex='F', birthday=datetime(day=2, month=3, year=1962)),
    Individual('5e5e', name='Ava /White/', sex='M', birthday=datetime(day=1, month=4, year=1985)),
    Individual('6f6f', name='Maria /White/', sex='F', birthday=datetime(day=9, month=10, year=1988)),
    Individual('7g7g', name='Ken /White/', sex='M', birthday=datetime(day=30, month=1, year=1946)),
    Individual('8h8h', name='Ana /White/', sex='F', birthday=datetime(day=3, month=5, year=1940))   
]

_families = [
    Family('F1', husband_id='3c3c', wife_id='4d4d', children=['1', '2']),
    Family('F2', husband_id='7g7g', wife_id='8h8h', children=['5', '6'])
]

husband_incorrect = Tree()

[husband_incorrect .add_individual(i) for i in _individuals]
[husband_incorrect .add_family(f) for f in _families]
