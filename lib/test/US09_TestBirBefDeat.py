import unittest

from lib.test.trees import us09_birt_bef_deaths
from lib.test.trees import us09_birt_after_deaths


class TestBirthBefDeath(unittest.TestCase):

    def test_birth_bed_death(self):
        self.assertTrue(us09_birt_bef_deaths.birth_bef_death())

    def test_birth_after_death(self):
        self.assertFalse(us09_birt_after_deaths.birth_bef_death())

