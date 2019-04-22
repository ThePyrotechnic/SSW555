import unittest

from lib.test.trees import us08_all_valid_birth_dates
from lib.test.trees import us08_some_children_born_before_marriage
from lib.test.trees import us08_some_children_born_more_than_nine_months_after_divorce
from lib.test.trees import us08_some_children_bef_marr_and_after_div
from lib.test.trees import us08_all_children_have_invalid_birth_dates


class TestBirthOccursAtValidDate(unittest.TestCase):

    def test_all_valid_birth_dates(self):
        self.assertTrue(us08_all_valid_birth_dates.birth_occurs_at_valid_date())

    def test_some_children_born_before_marriage(self):
        self.assertFalse(us08_some_children_born_before_marriage.birth_occurs_at_valid_date())

    def test_some_children_born_more_than_nine_months_after_divorce(self):
        self.assertFalse(us08_some_children_born_more_than_nine_months_after_divorce.birth_occurs_at_valid_date())

    def test_some_births_bef_marr_and_after_div(self):
        self.assertFalse(us08_some_children_bef_marr_and_after_div.birth_occurs_at_valid_date())

    def test_all_children_have_invalid_birth_dates(self):
        self.assertFalse(us08_all_children_have_invalid_birth_dates.birth_occurs_at_valid_date())
