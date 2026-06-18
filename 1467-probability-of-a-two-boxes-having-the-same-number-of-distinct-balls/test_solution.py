import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.getProbability([1,1]), 1.00000, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.getProbability([2,1,1]), 0.66667, places=5)

    def test_example_3(self):
        self.assertAlmostEqual(self.solution.getProbability([1,2,1,2]), 0.60000, places=5)

if __name__ == '__main__':
    unittest.main()
