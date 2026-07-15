import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxDotProduct([2,1,-2,5], [3,0,-6]), 18)

    def test_example_2(self):
        self.assertEqual(self.solution.maxDotProduct([3,-2], [2,-6,7]), 21)

    def test_example_3(self):
        self.assertEqual(self.solution.maxDotProduct([-1,-1], [1,1]), -1)

if __name__ == '__main__':
    unittest.main()
