import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.new21Game(10, 1, 10), 1.00000, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.new21Game(6, 1, 10), 0.60000, places=5)

    def test_example_3(self):
        self.assertAlmostEqual(self.solution.new21Game(21, 17, 10), 0.73278, places=5)

if __name__ == '__main__':
    unittest.main()
