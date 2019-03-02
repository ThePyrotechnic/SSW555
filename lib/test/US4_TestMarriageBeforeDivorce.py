import unittest

from lib.GedObjects import *

_families1 = [
    Family('F1', married = datetime(day = 24, month = 3, year = 1998), divorced = datetime(day = 3, month = 2, year = 2019)),
    Family('F2', married = datetime(day = 30, month = 9, year = 1956), divorced = datetime(day =12, month = 11, year = 2000)),
    Family('F3', married = datetime(day = 2, month = 6, year = 1980), divorced = datetime(day = 9, month = 3, year = 1997))
]

all_correct = Tree()
[all_correct.add_families(f) for f in _families1]

_families2 = [
     Family('F1', married = datetime(day = 24, month = 3, year = 1998), divorced = datetime(day = 3, month = 2, year = 1919)),
    Family('F2', married = datetime(day = 30, month = 9, year = 1956), divorced = datetime(day =12, month = 11, year = 1900)),
    Family('F3', married = datetime(day = 2, month = 6, year = 1998), divorced = datetime(day = 9, month = 3, year = 1997))
]

all_wrong = Tree()
[all_wron.addfamilies(f) for f in _families2]


def TestAllCorrect(self):
    self.assertTrue(all_correct.marr_bef_div())

def TestAllWrong(self):
    self.assertFalse(all_wrong.marr_bef_div())