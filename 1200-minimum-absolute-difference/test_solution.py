import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minimumAbsDifference([4,2,1,3]), [[1,2],[2,3],[3,4]])

    def test_example_2(self):
        self.assertEqual(self.solution.minimumAbsDifference([1,3,6,10,15]), [[1,3]])

    def test_example_3(self):
        self.assertEqual(self.solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]), [[-14,-10],[19,23],[23,27]])

if __name__ == '__main__':
    unittest.main()
