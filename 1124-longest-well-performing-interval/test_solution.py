import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestWPI([9,9,6,0,6,6,9]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.longestWPI([6,6,6]), 0)

if __name__ == '__main__':
    unittest.main()
