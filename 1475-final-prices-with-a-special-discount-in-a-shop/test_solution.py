import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.finalPrices([8,4,6,2,3]), [4,2,4,2,3])

    def test_example_2(self):
        self.assertEqual(self.solution.finalPrices([1,2,3,4,5]), [1,2,3,4,5])

    def test_example_3(self):
        self.assertEqual(self.solution.finalPrices([10,1,1,6]), [9,0,1,6])

if __name__ == '__main__':
    unittest.main()
