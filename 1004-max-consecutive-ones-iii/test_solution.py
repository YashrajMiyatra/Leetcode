import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)

if __name__ == '__main__':
    unittest.main()
