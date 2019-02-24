from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family
from lib.GedObjects import Individual

_individuals = [
    Individual('aa', name='Evan /Doe/', sex='M', birthday=datetime(day=12, month=4, year=1998)),
    Individual('bb', name='Elena /Doe/', sex='F', birthday=datetime(day=15, month=9, year=2000)),
    Individual('cc', name='John /Doe/', sex='F', birthday=datetime(day=2, month=3, year=1962)), # cc is wrong
    Individual('dd', name='Jane /Doe/', sex='M', birthday=datetime(day=2, month=3, year=1962)), # dd is wrong
    Individual('ee', name='Ava /White/', sex='F', birthday=datetime(day=1, month=4, year=1985)),
    Individual('ff', name='Maria /White/', sex='F', birthday=datetime(day=9, month=10, year=1988)),
    Individual('gg', name='Ken /White/', sex='M', birthday=datetime(day=30, month=1, year=1946)),
    Individual('hh', name='Ana /White/', sex='F', birthday=datetime(day=3, month=5, year=1940))   
]

_families = [
    Family('F1', husband_id='cc', wife_id='dd', children=['1', '2']),
    Family('F2', husband_id='gg', wife_id='hh', children=['5', '6'])
]

husb_and_wife_incorrect = Tree()

[husb_and_wife_incorrect .add_individual(i) for i in _individuals]
[husb_and_wife_incorrect .add_family(f) for f in _families]
