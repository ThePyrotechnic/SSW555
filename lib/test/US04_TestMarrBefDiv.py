import unittest

from lib.test.trees import us04_marr_is_before_div
from lib.test.trees import us04_marr_not_before_div
from lib.test.trees import us04_div_without_marriage


class TestMarrBefDiv(unittest.TestCase):

    def test_marr_is_before_div(self):
        self.assertTrue(us04_marr_is_before_div.marr_bef_div())

    def test_marr_not_before_div(self):
        self.assertFalse(us04_marr_not_before_div.marr_bef_div())

    def test_div_without_marriage(self):
        self.assertFalse(us04_div_without_marriage.marr_bef_div())
