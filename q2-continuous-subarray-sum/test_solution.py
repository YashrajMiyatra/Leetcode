import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.checkSubarraySum([23,2,4,6,7], 6), True)

    def test_example_2(self):
        self.assertEqual(self.solution.checkSubarraySum([23,2,6,4,7], 6), True)

    def test_example_3(self):
        self.assertEqual(self.solution.checkSubarraySum([23,2,6,4,7], 13), False)

if __name__ == '__main__':
    unittest.main()
