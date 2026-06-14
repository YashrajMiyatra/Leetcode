import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.champagneTower(1, 1, 1), 0.00000)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.champagneTower(2, 1, 1), 0.50000)

    def test_example_3(self):
        self.assertAlmostEqual(self.solution.champagneTower(100000009, 33, 17), 1.00000)

if __name__ == '__main__':
    unittest.main()
