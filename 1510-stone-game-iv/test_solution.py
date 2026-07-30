import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.winnerSquareGame(1))

    def test_example_2(self):
        self.assertFalse(self.solution.winnerSquareGame(2))

    def test_example_3(self):
        self.assertTrue(self.solution.winnerSquareGame(4))

if __name__ == '__main__':
    unittest.main()
