import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.hasEqualSumPartition([[1,4],[2,3]]))

    def test_example_2(self):
        self.assertTrue(self.solution.hasEqualSumPartition([[1,2],[3,4]]))

    def test_example_3(self):
        self.assertFalse(self.solution.hasEqualSumPartition([[1,2,4],[2,3,5]]))

    def test_example_4(self):
        self.assertFalse(self.solution.hasEqualSumPartition([[4,1,8],[3,2,6]]))

if __name__ == '__main__':
    unittest.main()
