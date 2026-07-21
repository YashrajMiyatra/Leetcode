import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestString(2, 5, 1), 12)

    def test_example_2(self):
        self.assertEqual(self.solution.longestString(3, 2, 2), 14)

if __name__ == '__main__':
    unittest.main()
