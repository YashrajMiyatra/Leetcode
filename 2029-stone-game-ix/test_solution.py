import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.stoneGameIX([2, 1]))

    def test_example_2(self):
        self.assertFalse(self.solution.stoneGameIX([2]))

    def test_example_3(self):
        self.assertFalse(self.solution.stoneGameIX([5, 1, 2, 4, 3]))

if __name__ == '__main__':
    unittest.main()
