import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestSubarray([8, 2, 4, 7], 4), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.longestSubarray([10, 1, 2, 4, 7, 2], 5), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0), 3)

if __name__ == '__main__':
    unittest.main()
