import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.stoneGameV([6, 2, 3, 4, 5, 5]), 18)

    def test_example_2(self):
        self.assertEqual(self.solution.stoneGameV([7, 7, 7, 7, 7, 7, 7]), 28)

    def test_example_3(self):
        self.assertEqual(self.solution.stoneGameV([4]), 0)

if __name__ == '__main__':
    unittest.main()
