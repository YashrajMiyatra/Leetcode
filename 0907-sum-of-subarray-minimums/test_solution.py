import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sumSubarrayMins([3,1,2,4]), 17)

    def test_example_2(self):
        self.assertEqual(self.solution.sumSubarrayMins([11,81,94,43,3]), 444)

if __name__ == '__main__':
    unittest.main()
