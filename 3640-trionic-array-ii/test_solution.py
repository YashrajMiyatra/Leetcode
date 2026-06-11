import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSumTrionic([0,-2,-1,-3,0,2,-1]), -4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxSumTrionic([1,4,2,7]), 14)

if __name__ == '__main__':
    unittest.main()
