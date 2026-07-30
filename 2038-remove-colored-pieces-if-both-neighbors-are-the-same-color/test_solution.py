import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.winnerOfGame("AAABABB"))

    def test_example_2(self):
        self.assertFalse(self.solution.winnerOfGame("AA"))

    def test_example_3(self):
        self.assertFalse(self.solution.winnerOfGame("ABBBBBBBAAA"))

if __name__ == '__main__':
    unittest.main()
