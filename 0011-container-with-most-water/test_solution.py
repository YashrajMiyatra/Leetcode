import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_example_2(self):
        self.assertEqual(self.solution.maxArea([1,1]), 1)

if __name__ == '__main__':
    unittest.main()
