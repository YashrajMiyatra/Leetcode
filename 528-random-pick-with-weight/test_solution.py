import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        s = Solution([1, 3])
        
        counts = {0: 0, 1: 0}
        iterations = 40000
        
        for _ in range(iterations):
            idx = s.pickIndex()
            counts[idx] += 1
            
        # Index 0 should have ~25%
        # Index 1 should have ~75%
        pct_0 = counts[0] / iterations
        pct_1 = counts[1] / iterations
        
        self.assertTrue(0.23 <= pct_0 <= 0.27)
        self.assertTrue(0.73 <= pct_1 <= 0.77)

    def test_single_element(self):
        s = Solution([10])
        self.assertEqual(s.pickIndex(), 0)
        self.assertEqual(s.pickIndex(), 0)

if __name__ == '__main__':
    unittest.main()
