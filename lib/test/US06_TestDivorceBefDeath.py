import unittest
from lib.test.trees import us06_div_bef_death
from lib.test.trees import sprint_one_tree


class Death_After_Div(unittest.TestCase):
    def test_for_pero_like_how(self):
        self.assertFalse(us06_div_bef_death.div_bef_deat())

