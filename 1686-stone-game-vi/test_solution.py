import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameVI([1, 3], [2, 1]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameVI([1, 2], [3, 1]), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.stoneGameVI([2, 4, 3], [1, 6, 7]), -1)

if __name__ == '__main__':
    unittest.main()
