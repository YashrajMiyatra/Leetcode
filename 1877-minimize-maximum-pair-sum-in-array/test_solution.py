import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minPairSum([3,5,2,3]), 7)

    def test_example_2(self):
        self.assertEqual(self.solution.minPairSum([3,5,4,2,4,6]), 8)

if __name__ == '__main__':
    unittest.main()
