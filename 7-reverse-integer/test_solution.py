import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_positive(self):
        self.assertEqual(self.sol.reverse(123), 321)

    def test_negative(self):
        self.assertEqual(self.sol.reverse(-123), -321)

    def test_trailing_zero(self):
        self.assertEqual(self.sol.reverse(120), 21)

    def test_zero(self):
        self.assertEqual(self.sol.reverse(0), 0)

    def test_overflow_positive(self):
        self.assertEqual(self.sol.reverse(1534236469), 0)

    def test_overflow_negative(self):
        self.assertEqual(self.sol.reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()
