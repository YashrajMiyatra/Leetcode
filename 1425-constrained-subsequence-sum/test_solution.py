import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.constrainedSubsetSum([10, 2, -10, 5, 20], 2), 37)

    def test_example_2(self):
        self.assertEqual(self.solution.constrainedSubsetSum([-1, -2, -3], 1), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.constrainedSubsetSum([10, -2, -10, -5, 20], 2), 23)

if __name__ == '__main__':
    unittest.main()
