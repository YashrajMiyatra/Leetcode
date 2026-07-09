import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.pathsWithMaxScore(["E23","2X2","12S"]), [7, 1])

    def test_example_2(self):
        self.assertEqual(self.solution.pathsWithMaxScore(["E12","1X1","21S"]), [4, 2])

    def test_example_3(self):
        self.assertEqual(self.solution.pathsWithMaxScore(["E11","XXX","11S"]), [0, 0])

if __name__ == '__main__':
    unittest.main()
