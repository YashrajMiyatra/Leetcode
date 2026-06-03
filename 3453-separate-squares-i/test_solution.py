import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        # Allows delta of 1e-5
        self.assertAlmostEqual(s.separateSquares([[0,0,1],[2,2,1]]), 1.00000, places=5)

    def test_example2(self):
        s = Solution()
        self.assertAlmostEqual(s.separateSquares([[0,0,2],[1,1,1]]), 1.16666666, places=5)

    def test_gap(self):
        s = Solution()
        # Squares are disjoint. Area 1 and Area 1. Gap is [1, 10]. Answer should be the very bottom of the gap (1.0).
        self.assertAlmostEqual(s.separateSquares([[0,0,1],[10,10,1]]), 1.00000, places=5)

if __name__ == '__main__':
    unittest.main()
