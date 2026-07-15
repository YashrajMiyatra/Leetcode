import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.stoneGame([5,3,4,5]))

    def test_example_2(self):
        self.assertTrue(self.solution.stoneGame([3,7,2,3]))

if __name__ == '__main__':
    unittest.main()
