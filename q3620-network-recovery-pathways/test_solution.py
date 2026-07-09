import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxPathScore(4, [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], [True,True,True,True], 10), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maxPathScore(5, [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], [True,True,True,False,True], 12), 6)

if __name__ == '__main__':
    unittest.main()
