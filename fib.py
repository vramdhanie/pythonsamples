"""This program implements finding the nth fibonacci number using an efficient
   memoization technique. A dictionary of the fibonacci sequence is built up to
   the nth number.
"""
import unittest

t = {0:0, 1:1}

def fib(n):
    """Return the nth fibonacci number

       Use a dictionary to track the values
    """
    if n < 0:
        raise TypeError, "fibonacci not defined for values less than 0"
    if n in t:
        return t[n]
    else:
        t[n] = fib(n-1) + fib(n-2)
        return t[n]

# Define a test suite to test the function
class FibTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(8), 21)
        with self.assertRaises(TypeError):
            fib(-1)

# Execute the test suite when this file is run
suite = unittest.TestLoader().loadTestsFromTestCase(FibTest)
unittest.TextTestRunner(verbosity=2).run(suite)

# This is a test set using py.test
# Running py.test fib.py from the command line will execute this test
def test_fib():
    assert fib(6) == 8
    assert fib(1) == 1
