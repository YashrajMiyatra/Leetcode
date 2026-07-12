import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.closestEqualElementQueries([1,3,1,4,1,3,2], [0,3,5]), [2,-1,3])

    def test_example_2(self):
        self.assertEqual(self.solution.closestEqualElementQueries([1,2,3,4], [0,1,2,3]), [-1,-1,-1,-1])

if __name__ == '__main__':
    unittest.main()
