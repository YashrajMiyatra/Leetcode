import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countMatchingSubarrays([1,2,3,4,5,6], [1,1]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.countMatchingSubarrays([1,4,4,1,3,5,5,3], [1,0,-1]), 2)

if __name__ == '__main__':
    unittest.main()
