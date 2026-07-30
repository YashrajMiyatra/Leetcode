import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.findLengthOfShortestSubarray([5,4,3,2,1]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.findLengthOfShortestSubarray([1,2,3]), 0)

if __name__ == '__main__':
    unittest.main()
