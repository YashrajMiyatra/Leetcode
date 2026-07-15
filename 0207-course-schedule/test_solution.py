import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.canFinish(2, [[1,0]]))

    def test_example_2(self):
        self.assertFalse(self.solution.canFinish(2, [[1,0],[0,1]]))

if __name__ == '__main__':
    unittest.main()
