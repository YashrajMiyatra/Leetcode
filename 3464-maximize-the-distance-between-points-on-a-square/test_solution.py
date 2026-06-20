import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximizeTheDistance(2, [[0,2],[2,0],[2,2],[0,0]], 4), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maximizeTheDistance(2, [[0,0],[1,2],[2,0],[2,2],[2,1]], 4), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maximizeTheDistance(2, [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], 5), 1)

if __name__ == '__main__':
    unittest.main()
