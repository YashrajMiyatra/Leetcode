import unittest
import math
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        s = Solution(1.0, 0.0, 0.0)
        
        # Test 1000 points to ensure they mathematically fall within the circle
        for _ in range(1000):
            p = s.randPoint()
            # Distance from center should be <= radius
            dist = math.sqrt(p[0]**2 + p[1]**2)
            self.assertTrue(dist <= 1.0)
            
    def test_offset_center(self):
        s = Solution(5.0, 10.0, -10.0)
        
        for _ in range(1000):
            p = s.randPoint()
            # Calculate offset distance
            dist = math.sqrt((p[0] - 10.0)**2 + (p[1] + 10.0)**2)
            self.assertTrue(dist <= 5.0)

if __name__ == '__main__':
    unittest.main()
