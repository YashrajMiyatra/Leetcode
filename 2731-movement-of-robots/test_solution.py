import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.sumDistance([-2,0,2], "RLL", 3), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.sumDistance([1,0], "RL", 2), 5)

if __name__ == '__main__':
    unittest.main()
