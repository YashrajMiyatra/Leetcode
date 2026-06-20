import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
        self.assertEqual(self.solution.findTheString(lcp), "abab")

    def test_example_2(self):
        lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
        self.assertEqual(self.solution.findTheString(lcp), "aaaa")

    def test_example_3(self):
        lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
        self.assertEqual(self.solution.findTheString(lcp), "")

    def test_invalid_zero(self):
        lcp = [[0]]
        self.assertEqual(self.solution.findTheString(lcp), "")

if __name__ == '__main__':
    unittest.main()
