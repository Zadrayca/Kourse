def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)

#print(fib(5))

import unittest

class TestFibTest(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(3), 2)

if __name__ == '__main__':
    unittest.main()