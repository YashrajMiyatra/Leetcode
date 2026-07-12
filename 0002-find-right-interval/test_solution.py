import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findRightInterval([[1,2]]), [-1])

    def test_example_2(self):
        self.assertEqual(self.solution.findRightInterval([[3,4],[2,3],[1,2]]), [-1,0,1])

    def test_example_3(self):
        self.assertEqual(self.solution.findRightInterval([[1,4],[2,3],[3,4]]), [-1,2,-1])

if __name__ == '__main__':
    unittest.main()
