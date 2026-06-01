import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_distribution(self):
        # A 2x2 square and a 1x1 square
        rects = [[0, 0, 1, 1], [3, 3, 3, 3]]
        s = Solution(rects)
        
        # Point count: rect1 has 4 points. rect2 has 1 point. Total = 5 points.
        points_count = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0, (3, 3): 0}
        
        iterations = 50000
        for _ in range(iterations):
            p = s.pick()
            t = tuple(p)
            self.assertIn(t, points_count)
            points_count[t] += 1
            
        # Expect ~20% distribution for each point
        for pt, count in points_count.items():
            percentage = count / iterations
            self.assertTrue(0.18 <= percentage <= 0.22)

if __name__ == '__main__':
    unittest.main()
