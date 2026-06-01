import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        s = Solution([1, 2, 3, 3, 3])
        
        # Target 1 should always return 0
        self.assertEqual(s.pick(1), 0)
        
        # Target 2 should always return 1
        self.assertEqual(s.pick(2), 1)
        
        # Target 3 should return 2, 3, or 4
        valid_indices = {2, 3, 4}
        for _ in range(10):
            self.assertIn(s.pick(3), valid_indices)

    def test_all_duplicates(self):
        s = Solution([5, 5, 5])
        valid_indices = {0, 1, 2}
        for _ in range(10):
            self.assertIn(s.pick(5), valid_indices)

if __name__ == '__main__':
    unittest.main()
