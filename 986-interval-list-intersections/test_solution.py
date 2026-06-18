import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        firstList = [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]
        self.assertEqual(self.solution.intervalIntersection(firstList, secondList), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])

    def test_example_2(self):
        firstList = [[1,3],[5,9]]
        secondList = []
        self.assertEqual(self.solution.intervalIntersection(firstList, secondList), [])

if __name__ == '__main__':
    unittest.main()
