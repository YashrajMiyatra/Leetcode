import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameII([2, 7, 9, 4, 4]), 10)

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameII([1, 2, 3, 4, 5, 100]), 104)

if __name__ == '__main__':
    unittest.main()
