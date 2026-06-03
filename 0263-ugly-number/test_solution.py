import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertTrue(s.isUgly(6))

    def test_example2(self):
        s = Solution()
        self.assertTrue(s.isUgly(1))

    def test_example3(self):
        s = Solution()
        self.assertFalse(s.isUgly(14))

    def test_negative(self):
        s = Solution()
        self.assertFalse(s.isUgly(-2147483648))

    def test_zero(self):
        s = Solution()
        self.assertFalse(s.isUgly(0))

    def test_large_ugly(self):
        s = Solution()
        self.assertTrue(s.isUgly(2**10 * 3**5 * 5**4))

if __name__ == '__main__':
    unittest.main()
