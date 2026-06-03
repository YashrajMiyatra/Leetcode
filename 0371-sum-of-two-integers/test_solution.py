import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.getSum(1, 2), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.getSum(2, 3), 5)

    def test_negative(self):
        s = Solution()
        self.assertEqual(s.getSum(-1000, -1000), -2000)

    def test_mixed(self):
        s = Solution()
        self.assertEqual(s.getSum(-1000, 500), -500)

    def test_zero(self):
        s = Solution()
        self.assertEqual(s.getSum(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
