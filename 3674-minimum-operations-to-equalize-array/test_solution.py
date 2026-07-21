import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minOperations([1,2]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minOperations([5,5,5]), 0)

if __name__ == '__main__':
    unittest.main()
