import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kConcatenationMaxSum([1,2], 3), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.kConcatenationMaxSum([1,-2,1], 5), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.kConcatenationMaxSum([-1,-2], 7), 0)

if __name__ == '__main__':
    unittest.main()
