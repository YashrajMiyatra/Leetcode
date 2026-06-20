import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]), [2,2,1,0])

    def test_example_2(self):
        self.assertEqual(self.solution.smallestTrimmedNumbers(["24","37","96","04"], [[2,1],[2,2]]), [3,0])

if __name__ == '__main__':
    unittest.main()
