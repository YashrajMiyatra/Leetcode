import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largestRectangleArea([2,1,5,6,2,3]), 10)

    def test_example_2(self):
        self.assertEqual(self.solution.largestRectangleArea([2,4]), 4)

if __name__ == '__main__':
    unittest.main()
