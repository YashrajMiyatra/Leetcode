import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        self.assertEqual(self.solution.getSkyline(buildings), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])

    def test_example_2(self):
        buildings = [[0,2,3],[2,5,3]]
        self.assertEqual(self.solution.getSkyline(buildings), [[0,3],[5,0]])

if __name__ == '__main__':
    unittest.main()
