import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxTotalValue([1,3,2], 2), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxTotalValue([4,2,5,1], 3), 12)

if __name__ == '__main__':
    unittest.main()
