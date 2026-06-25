import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2), 0)

if __name__ == '__main__':
    unittest.main()
