from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Family

_families = [
    Family('F1', married = datetime.datetime(2021, 4, 11, 0, 0)),
    Family('F2', married = datetime.datetime(2075, 10, 31, 0, 0), divorced = datetime.datetime(2007, 12, 25, 0, 0)),
    Family('F3', married = datetime.datetime(3004, 12, 5, 0, 0)),
    Family('F4', married = datetime.datetime(2011, 6, 29, 0, 0), divorced = datetime.datetime(2100, 2, 12, 0, 0))
]

incorrect_fam = Tree()
[incorrect_fam.add_family(f) for f in _families]