import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.predictTheWinner([1, 5, 2]))

    def test_example_2(self):
        self.assertTrue(self.solution.predictTheWinner([1, 5, 233, 7]))

if __name__ == '__main__':
    unittest.main()
