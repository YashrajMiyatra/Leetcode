import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isPossible(5, [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.isPossible(4, [[1,2],[3,4]]), True)

    def test_example_3(self):
        self.assertEqual(self.solution.isPossible(4, [[1,2],[1,3],[1,4]]), False)

if __name__ == '__main__':
    unittest.main()
