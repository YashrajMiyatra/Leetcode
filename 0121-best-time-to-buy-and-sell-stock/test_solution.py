import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxProfit([7,1,5,3,6,4]), 5)

    def test_example_2(self):
        self.assertEqual(self.solution.maxProfit([7,6,4,3,1]), 0)

if __name__ == '__main__':
    unittest.main()
