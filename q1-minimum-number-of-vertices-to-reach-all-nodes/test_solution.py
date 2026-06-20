import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]), [0,3])

    def test_example_2(self):
        self.assertEqual(self.solution.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]), [0,2,3])

if __name__ == '__main__':
    unittest.main()
