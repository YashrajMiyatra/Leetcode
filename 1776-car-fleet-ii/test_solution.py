import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        result = self.solution.getCollisionTimes([[1,2],[2,1],[4,3],[7,2]])
        expected = [1.00000,-1.00000,3.00000,-1.00000]
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example_2(self):
        result = self.solution.getCollisionTimes([[3,4],[5,4],[6,3],[9,1]])
        expected = [2.00000,1.00000,1.50000,-1.00000]
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

if __name__ == '__main__':
    unittest.main()
