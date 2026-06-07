import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [1,3,2,8,4,9]
        fee = 2
        self.assertEqual(self.solution.maxProfit(prices, fee), 8)

    def test_example_2(self):
        prices = [1,3,7,5,10,3]
        fee = 3
        self.assertEqual(self.solution.maxProfit(prices, fee), 6)

if __name__ == '__main__':
    unittest.main()
