import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])

    def test_example_2(self):
        self.assertEqual(self.solution.merge([[1,4],[4,5]]), [[1,5]])

    def test_example_3(self):
        self.assertEqual(self.solution.merge([[4,7],[1,4]]), [[1,7]])

if __name__ == '__main__':
    unittest.main()
