import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]), 4)

if __name__ == '__main__':
    unittest.main()
