import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMaxValueOfEquation([[1,3],[2,0],[5,10],[6,-10]], 1), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3), 3)

if __name__ == '__main__':
    unittest.main()
