import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxResult([1, -1, -2, 4, -7, 3], 2), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.maxResult([10, -5, -2, 4, 0, 3], 3), 17)

    def test_example_3(self):
        self.assertEqual(self.solution.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2), 0)

if __name__ == '__main__':
    unittest.main()
