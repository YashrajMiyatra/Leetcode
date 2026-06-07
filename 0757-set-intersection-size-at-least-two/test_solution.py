import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1,3],[3,7],[8,9]]
        self.assertEqual(self.solution.intersectionSizeTwo(intervals), 5)

    def test_example_2(self):
        intervals = [[1,3],[1,4],[2,5],[3,5]]
        self.assertEqual(self.solution.intersectionSizeTwo(intervals), 3)

    def test_example_3(self):
        intervals = [[1,2],[2,3],[2,4],[4,5]]
        self.assertEqual(self.solution.intersectionSizeTwo(intervals), 5)

if __name__ == '__main__':
    unittest.main()
