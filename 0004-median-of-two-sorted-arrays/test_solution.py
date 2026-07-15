import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1,3], [2]), 2.0)

    def test_example_2(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1,2], [3,4]), 2.5)

if __name__ == '__main__':
    unittest.main()
