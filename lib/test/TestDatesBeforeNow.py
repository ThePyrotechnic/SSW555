import unittest

from lib.GedObjects import Tree
from lib.test.old_trees.AngelicaTree import correct_dates
from lib.test.old_trees.AngelicaTree import correct_inds
from lib.test.old_trees.AngelicaTree import correct_fams
from lib.test.old_trees.AngelicaTree import incorrect_fam
from lib.test.old_trees.AngelicaTree import correct_incorrect

class TestDatesBeforeCurrent(unittest.TestCase):
    def test_correct_dates(self):
        self.assertTrue(correct_dates.dates_check())

    def test_correct_individ(self):
        self.assertTrue(correct_inds.dates_check())

    def test_all_correct_fams(self):
        self.assertTrue(correct_fams.dates_check())

    def test_incorrect_fam(self):
        self.assertFalse(incorrect_fam.dates_check())

    def test_corr_fam_incorr_ind(self):
        self.assertFalse(correct_incorrect.dates_check())