import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.climbStairs(3), 3)
        
    def test_example_3(self):
        self.assertEqual(self.solution.climbStairs(4), 5)

if __name__ == '__main__':
    unittest.main()
