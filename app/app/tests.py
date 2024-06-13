"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class TesCalc(SimpleTestCase):
    """test the calc modul."""

    def test_add_numbers(self):
        """test adding ..."""
        res = calc.add(3, 4)

        self.assertEqual(res, 7)

    def test_subtract_numbers(self):
        """test subtract numbers."""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
