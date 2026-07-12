import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxRotateFunction([4,3,2,6]), 26)

    def test_example_2(self):
        self.assertEqual(self.solution.maxRotateFunction([100]), 0)

if __name__ == '__main__':
    unittest.main()
