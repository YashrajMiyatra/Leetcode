import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertAlmostEqual(s.separateSquares([[0,0,1],[2,2,1]]), 1.00000, places=5)

    def test_example2(self):
        s = Solution()
        self.assertAlmostEqual(s.separateSquares([[0,0,2],[1,1,1]]), 1.00000, places=5)
        
    def test_stacked_overlap(self):
        s = Solution()
        # [0,0,2] union [0,0,2] -> same square. Area = 4. Midpoint is y=1.
        self.assertAlmostEqual(s.separateSquares([[0,0,2],[0,0,2]]), 1.00000, places=5)

if __name__ == '__main__':
    unittest.main()
