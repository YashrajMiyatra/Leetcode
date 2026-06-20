import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minSubarray([3,1,4,2], 6), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minSubarray([6,3,5,2], 9), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.minSubarray([1,2,3], 3), 0)

if __name__ == '__main__':
    unittest.main()
