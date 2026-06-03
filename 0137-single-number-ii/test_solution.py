import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.singleNumber([2, 2, 3, 2]), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)

    def test_negative(self):
        s = Solution()
        self.assertEqual(s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]), -4)

if __name__ == '__main__':
    unittest.main()
