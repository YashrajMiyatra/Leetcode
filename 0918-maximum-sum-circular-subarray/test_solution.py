import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSubarraySumCircular([1, -2, 3, -2]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSubarraySumCircular([5, -3, 5]), 10)

    def test_example_3(self):
        self.assertEqual(self.solution.maxSubarraySumCircular([-3, -2, -3]), -2)

if __name__ == '__main__':
    unittest.main()
