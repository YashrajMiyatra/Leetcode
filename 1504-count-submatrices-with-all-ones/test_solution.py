import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.numSubmat([[1,0,1],[1,1,0],[1,1,0]]), 13)

    def test_example_2(self):
        self.assertEqual(self.solution.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]), 24)

if __name__ == '__main__':
    unittest.main()
