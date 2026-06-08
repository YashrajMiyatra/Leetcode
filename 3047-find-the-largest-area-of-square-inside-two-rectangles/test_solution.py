import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        bottomLeft = [[1,1],[2,2],[3,1]]
        topRight = [[3,3],[4,4],[6,6]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 1)

    def test_example_2(self):
        bottomLeft = [[1,1],[1,3],[1,5]]
        topRight = [[5,5],[5,7],[5,9]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 4)

    def test_example_3(self):
        bottomLeft = [[1,1],[2,2],[1,2]]
        topRight = [[3,3],[4,4],[3,4]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 1)

    def test_example_4(self):
        bottomLeft = [[1,1],[3,3],[3,1]]
        topRight = [[2,2],[4,4],[4,2]]
        self.assertEqual(self.solution.largestSquareArea(bottomLeft, topRight), 0)

if __name__ == '__main__':
    unittest.main()
