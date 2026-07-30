import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumMedianSum([2, 1, 3, 2, 1, 3]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumMedianSum([1, 1, 10, 10, 10, 10]), 20)

if __name__ == '__main__':
    unittest.main()
