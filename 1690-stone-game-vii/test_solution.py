import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameVII([5, 3, 1, 4, 2]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]), 122)

if __name__ == '__main__':
    unittest.main()
