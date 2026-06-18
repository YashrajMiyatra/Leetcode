import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1,4],[2,4],[3,6],[4,4]]
        queries = [2,3,4,5]
        self.assertEqual(self.solution.minInterval(intervals, queries), [3,3,1,4])

    def test_example_2(self):
        intervals = [[2,3],[2,5],[1,8],[20,25]]
        queries = [2,19,5,22]
        self.assertEqual(self.solution.minInterval(intervals, queries), [2,-1,4,6])

if __name__ == '__main__':
    unittest.main()
