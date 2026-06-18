import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.soupServings(50), 0.62500, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.soupServings(100), 0.71875, places=5)

    def test_example_zero(self):
        self.assertAlmostEqual(self.solution.soupServings(0), 0.5, places=5)

if __name__ == '__main__':
    unittest.main()
