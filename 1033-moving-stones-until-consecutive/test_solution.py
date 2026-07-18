import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numMovesStones(1, 2, 5), [1, 2])

    def test_example_2(self):
        self.assertEqual(self.solution.numMovesStones(4, 3, 2), [0, 0])

    def test_example_3(self):
        self.assertEqual(self.solution.numMovesStones(3, 5, 1), [1, 2])

if __name__ == '__main__':
    unittest.main()
