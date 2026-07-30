import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameVIII([-1, 2, -3, 4, -5]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]), 13)

    def test_example_3(self):
        self.assertEqual(self.solution.stoneGameVIII([-10, -12]), -22)

if __name__ == '__main__':
    unittest.main()
