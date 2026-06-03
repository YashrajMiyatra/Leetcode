import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.reverse(-123), -321)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.reverse(120), 21)

    def test_overflow_positive(self):
        s = Solution()
        self.assertEqual(s.reverse(1534236469), 0)

    def test_overflow_negative(self):
        s = Solution()
        self.assertEqual(s.reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()
