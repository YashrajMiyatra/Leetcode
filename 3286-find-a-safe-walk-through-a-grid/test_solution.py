import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1))

    def test_example_2(self):
        self.assertFalse(self.solution.findSafeWalk([[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3))

    def test_example_3(self):
        self.assertTrue(self.solution.findSafeWalk([[1,1,1],[1,0,1],[1,1,1]], 5))

if __name__ == '__main__':
    unittest.main()
