import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.hasEqualSumPartition([[1,4],[2,3]]))

    def test_example_2(self):
        self.assertFalse(self.solution.hasEqualSumPartition([[1,3],[2,4]]))

if __name__ == '__main__':
    unittest.main()
