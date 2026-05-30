import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.myAtoi("42"), 42)

    def test_example2(self):
        self.assertEqual(self.sol.myAtoi("   -042"), -42)

    def test_example3(self):
        self.assertEqual(self.sol.myAtoi("1337c0d3"), 1337)

    def test_example4(self):
        self.assertEqual(self.sol.myAtoi("0-1"), 0)

    def test_example5(self):
        self.assertEqual(self.sol.myAtoi("words and 987"), 0)

    def test_overflow_positive(self):
        self.assertEqual(self.sol.myAtoi("20000000000000000000"), 2147483647)

    def test_overflow_negative(self):
        self.assertEqual(self.sol.myAtoi("-20000000000000000000"), -2147483648)

    def test_empty(self):
        self.assertEqual(self.sol.myAtoi(""), 0)

    def test_just_sign(self):
        self.assertEqual(self.sol.myAtoi("+"), 0)
        self.assertEqual(self.sol.myAtoi("-"), 0)

if __name__ == '__main__':
    unittest.main()
