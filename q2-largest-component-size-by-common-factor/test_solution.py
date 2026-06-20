import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largestComponentSize([4,6,15,35]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.largestComponentSize([20,50,9,63]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.largestComponentSize([2,3,6,7,4,12,21,39]), 8)

if __name__ == '__main__':
    unittest.main()
