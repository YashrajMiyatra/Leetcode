import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxCoins([2, 4, 1, 2, 7, 8]), 9)

    def test_example_2(self):
        self.assertEqual(self.solution.maxCoins([2, 4, 5]), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]), 18)

if __name__ == '__main__':
    unittest.main()
