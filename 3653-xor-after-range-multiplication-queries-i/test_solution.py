import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.xorAfterQueries([1,1,1], [[0,2,1,4]]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.xorAfterQueries([2,3,1,5,4], [[1,4,2,3],[0,2,1,2]]), 31)

if __name__ == '__main__':
    unittest.main()
