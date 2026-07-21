import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1), [[9,1,2],[3,4,5],[6,7,8]])

    def test_example_2(self):
        self.assertEqual(self.solution.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4), [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]])

    def test_example_3(self):
        self.assertEqual(self.solution.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9), [[1,2,3],[4,5,6],[7,8,9]])

if __name__ == '__main__':
    unittest.main()
