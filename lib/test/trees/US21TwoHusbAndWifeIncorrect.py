from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('a', name='Evan /Doe/', sex='M', birthday=datetime(day=12, month=4, year=1998)),
    Individual('b', name='Elena /Doe/', sex='F', birthday=datetime(day=15, month=9, year=2000)),
    Individual('c', name='John /Doe/', sex='F', birthday=datetime(day=2, month=3, year=1962)),
    Individual('d', name='Jane /Doe/', sex='M', birthday=datetime(day=2, month=3, year=1962)),
    Individual('e', name='Ava /White/', sex='M', birthday=datetime(day=1, month=4, year=1985)),
    Individual('f', name='Maria /White/', sex='F', birthday=datetime(day=9, month=10, year=1988)),
    Individual('g', name='Ken /White/', sex='F', birthday=datetime(day=30, month=1, year=1946)),
    Individual('h', name='Ana /White/', sex='M', birthday=datetime(day=3, month=5, year=1940))   
]

_families = [
    Family('F1', husband_id='c', wife_id='d', children=['1', '2']),
    Family('F2', husband_id='g', wife_id='h', children=['5', '6'])
]

two_husb_and_wife_incorrect = Tree()

[two_husb_and_wife_incorrect .add_individual(i) for i in _individuals]
[two_husb_and_wife_incorrect .add_family(f) for f in _families]
