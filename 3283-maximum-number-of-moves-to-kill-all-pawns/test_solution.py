import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxMoves(1, 1, [[0,0]]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxMoves(0, 2, [[1,1],[2,2],[3,3]]), 8)

    def test_example_3(self):
        self.assertEqual(self.solution.maxMoves(0, 0, [[1,2],[2,4]]), 3)

if __name__ == '__main__':
    unittest.main()
