import unittest
from datetime import datetime

from lib.GedObjects import Tree
from lib.GedObjects import Individual
from lib.GedObjects import Family

# from lib.test.trees.US1AllCorrect import correct_dates
# from lib.test.trees.US1IndAllCorrect import correct_inds
# from lib.test.trees.US1IndividIncorr import incorrect_indivs
# from lib.test.trees.US1FamIncorr import incorrect_fam
# from lib.test.trees.US1CorrFamIncorrInd import correct_incorrect

"""Tree for Test Case 1"""
_individuals = [
    Individual('1', name = 'John /Dean/', sex = 'M', birthday = datetime(day = 20, month = 6, year = 1939)),
    Individual('2', name = 'Hannah /Montana/', sex = 'F', birthday = datetime(day = 30, month = 12, year = 1996)),
    Individual('3', name = 'Ethan /Evans/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 2018 )),
    Individual('4', name = 'Leslie /Maple/', sex = 'F', birthday = datetime(day = 12, month = 9, year = 1950))
] 

_families = [
    Family('F1', husband = '1', wife = '4', married = datetime.datetime(1973, 4, 11, 0, 0)),
    Family('F2', husband = '3', wife = '2', married = datetime.datetime(2000, 10, 31, 0, 0), divorced = datetime.datetime(2007, 12, 25, 0, 0))
]
correct_dates = Tree()
[correct_dates.add_individual(i) for i in _individuals]
[correct_dates.add_family(f) for f in _families]

"""Tree for Test Case 2"""
_individuals1 = [
    Individual('1', name = 'Super /Man/', sex = 'M', birthday = datetime(day = 28, month = 1, year = 1954), death = datetime(day = 5, month = 11, year = 2017)),
    Individual('2', name = 'Angela /Brown/', sex = 'F', birthday = datetime(day = 16, month = 2, year = 1987)),
    Individual('3', name = 'Jimmy /Gold/', sex = 'M', birthday = datetime(day = 1, month = 8, year = 1942), death = datetime(day = 23, month = 5, year = 2018 )),
    Individual('4', name = 'Carmen /Sandiego', sex = 'F', birthday = datetime(day = 11, month = 4, year = 2000))
] 
correct_inds = Tree()
[correct_inds.add_individual(i) for i in _individuals1]

"""Tree for Test Case 3"""
_individuals2 = [
    Individual('1', name = 'Dill /Pickles/', sex = 'M', birthday = datetime(day = 20, month = 6, year = 2020)),
    Individual('2', name = 'Sean /John/', sex = 'F', birthday = datetime(day = 30, month = 12, year = 2081)),
    Individual('3', name = 'Paul /Matthews/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 3019 ))
] 
incorrect_indivs = Tree()
[incorrect_indivs.add_individual(i) for i in _individuals2]

"""Tree for Test Case 4"""
_families1 = [
    Family('F1', married = datetime.datetime(2021, 4, 11, 0, 0)),
    Family('F2', married = datetime.datetime(2075, 10, 31, 0, 0), divorced = datetime.datetime(2007, 12, 25, 0, 0)),
    Family('F3', married = datetime.datetime(3004, 12, 5, 0, 0)),
    Family('F4', married = datetime.datetime(2011, 6, 29, 0, 0), divorced = datetime.datetime(2100, 2, 12, 0, 0))
]
incorrect_fam = Tree()
[incorrect_fam.add_family(f) for f in _families1]


"""Tree for Test Case 5"""
_individuals3 = [
    Individual('1', name = ' Dean /Adams/', sex = 'M', birthday = datetime(day = 20, month = 9, year = 2019)),
    Individual('2', name = 'Alex /Russo/', sex = 'F', birthday = datetime(day = 30, month = 1, year = 2020)),
    Individual('3', name = 'Ethan /Evans/', sex = 'M', birthday = datetime(day = 8, month = 3, year = 1970), death = datetime(day = 23, month = 5, year = 2030 )),
    Individual('4', name = 'Lizzie /MacGuire', sex = 'F', birthday = datetime(day = 15, month = 3, year = 2020), death = datetime(day = 7, month = 10, year = 2003))
] 
_families2 = [
    Family('F1', married = datetime.datetime(2015, 1, 18, 0, 0)),
    Family('F2', married = datetime.datetime(1989, 10, 21, 0, 0), divorced = datetime.datetime(2007, 12, 8, 0, 0))
]

correct_incorrect = Tree()

[correct_incorrect.add_individual(i) for i in _individuals3]
[correct_incorrect.add_family(f) for f in _families2]



class TestDatesBeforeCurrent(unittest.TestCase):
    def test_correct_dates(self):
        self.assertTrue(correct_dates.dates_check())

    def test_correct_individ(self):
        self.assertTrue(correct_inds.dates_check())

    def test_incorrect_indivs(self):
        self.assertFalse(incorrect_indivs.dates_check())

    def test_incorrect_fam(self):
        self.assertFalse(incorrect_fam.dates_check())

    def test_corr_fam_incorr_ind(self):
        self.assertFalse(correct_incorrect.dates_check())
    

