import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])

    def test_example_2(self):
        self.assertEqual(self.solution.maxSlidingWindow([1], 1), [1])

if __name__ == '__main__':
    unittest.main()
