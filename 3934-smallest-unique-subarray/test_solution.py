import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.smallestUniqueSubarray([3,3,3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.smallestUniqueSubarray([2,1,2,3,3]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.smallestUniqueSubarray([1,1,2,2,1]), 2)

if __name__ == '__main__':
    unittest.main()
