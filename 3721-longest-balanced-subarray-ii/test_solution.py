import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestBalancedSubarray([2,5,4,3]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.longestBalancedSubarray([3,2,2,5,4]), 5)

    def test_example_3(self):
        self.assertEqual(self.solution.longestBalancedSubarray([1,2,3,2]), 3)

if __name__ == '__main__':
    unittest.main()
