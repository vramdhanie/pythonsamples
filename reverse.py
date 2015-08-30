"""Implements a string reversal function

   A simple test program to illustrate one way to reverse a string. This program
   includes test cases for the function.
"""
import unittest

def reverse(s):
    """Reverses a string

       If the string s is 0 or 1 characters long the string remains unchanged,
       otherwise the first character of s is concatenated onto the reversed
       tail of the string.
    """
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0:1]

# Define a test suite to test the function
class ReverseTest(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse("abcd"), "dcba")
        self.assertEqual(reverse("abcde"), "edcba")

# Execute the test suite when this file is run
suite = unittest.TestLoader().loadTestsFromTestCase(ReverseTest)
unittest.TextTestRunner(verbosity=2).run(suite)
