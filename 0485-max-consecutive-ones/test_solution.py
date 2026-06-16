import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.findMaxConsecutiveOnes([1,0,1,1,0,1]), 2)

if __name__ == '__main__':
    unittest.main()
