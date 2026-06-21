import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]), 8)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumAmount([[10,10,10],[10,10,10]]), 40)

if __name__ == '__main__':
    unittest.main()
