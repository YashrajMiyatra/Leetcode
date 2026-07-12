import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2), True)

    def test_example_2(self):
        self.assertEqual(self.solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5), False)

if __name__ == '__main__':
    unittest.main()
