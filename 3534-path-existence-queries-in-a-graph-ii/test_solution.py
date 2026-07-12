import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.pathExistenceQueries(5, [1,8,3,4,2], 3, [[0,3],[2,4]]), [1,1])

    def test_example_2(self):
        self.assertEqual(self.solution.pathExistenceQueries(5, [5,3,1,9,10], 2, [[0,1],[0,2],[2,3],[4,3]]), [1,2,-1,1])

    def test_example_3(self):
        self.assertEqual(self.solution.pathExistenceQueries(3, [3,6,1], 1, [[0,0],[0,1],[1,2]]), [0,-1,-1])

if __name__ == '__main__':
    unittest.main()
