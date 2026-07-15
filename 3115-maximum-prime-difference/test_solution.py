import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumPrimeDifference([4,2,9,5,3]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumPrimeDifference([4,8,2,8]), 0)

if __name__ == '__main__':
    unittest.main()
