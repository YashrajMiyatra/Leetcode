import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
        self.assertEqual(self.solution.rectangleArea(rectangles), 6)

    def test_example_2(self):
        rectangles = [[0,0,1000000000,1000000000]]
        self.assertEqual(self.solution.rectangleArea(rectangles), 49)

if __name__ == '__main__':
    unittest.main()
