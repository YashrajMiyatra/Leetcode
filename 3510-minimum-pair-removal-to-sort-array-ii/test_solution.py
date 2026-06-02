import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.minimumPairRemoval([5, 2, 3, 1]), 2)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.minimumPairRemoval([1, 2, 2]), 0)

    def test_negative_sums(self):
        s = Solution()
        self.assertEqual(s.minimumPairRemoval([10, -5, -2, 8]), 3)

if __name__ == '__main__':
    unittest.main()
