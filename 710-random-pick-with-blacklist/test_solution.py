import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        # N = 7, blacklist = [2, 3, 5]
        # Valid: 0, 1, 4, 6
        s = Solution(7, [2, 3, 5])
        
        counts = {0: 0, 1: 0, 4: 0, 6: 0}
        iterations = 40000
        
        for _ in range(iterations):
            val = s.pick()
            self.assertIn(val, counts)
            counts[val] += 1
            
        # ~25% each
        for v, c in counts.items():
            pct = c / iterations
            self.assertTrue(0.23 <= pct <= 0.27)

    def test_empty_blacklist(self):
        s = Solution(5, [])
        counts = {i: 0 for i in range(5)}
        for _ in range(10000):
            val = s.pick()
            counts[val] += 1
            
        for c in counts.values():
            self.assertTrue(c > 0)

if __name__ == '__main__':
    unittest.main()
