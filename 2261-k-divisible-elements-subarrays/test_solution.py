import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countDistinct([2,3,3,2,2], 2, 2), 11)

    def test_example_2(self):
        self.assertEqual(self.solution.countDistinct([1,2,3,4], 4, 1), 10)

if __name__ == '__main__':
    unittest.main()
