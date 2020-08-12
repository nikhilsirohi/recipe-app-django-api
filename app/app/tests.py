from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):    # STARTS WITH WORD TEST else not read.
        """Test that values are added together.....
        Triple quotes are not comments as they are treated as regular strings
        with the exception that they can span multiple lines. By regular
        stringsI mean that if they are not assigned to a variable they will be
        immediately garbage collected as soon as that code executes. hence are
        not ignored by the interpreter in the same way that #a comment is. """

        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
