import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
        self.assertTrue(self.solution.isRectangleCover(rectangles))

    def test_example_2(self):
        rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
        self.assertFalse(self.solution.isRectangleCover(rectangles))

    def test_example_3(self):
        rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
        self.assertFalse(self.solution.isRectangleCover(rectangles))

if __name__ == '__main__':
    unittest.main()
