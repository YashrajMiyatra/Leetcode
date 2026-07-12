import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]), 1)

if __name__ == '__main__':
    unittest.main()
