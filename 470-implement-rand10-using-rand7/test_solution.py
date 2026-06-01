import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_distribution(self):
        s = Solution()
        counts = {i: 0 for i in range(1, 11)}
        
        # Run 100,000 times to verify uniform distribution
        iterations = 100000
        for _ in range(iterations):
            val = s.rand10()
            self.assertTrue(1 <= val <= 10)
            counts[val] += 1
            
        # Verify uniform distribution roughly ~10% each
        for i in range(1, 11):
            percentage = counts[i] / iterations
            self.assertTrue(0.09 <= percentage <= 0.11)

if __name__ == '__main__':
    unittest.main()
