import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [1, 2, 3]
        s = Solution(nums)
        
        # Test shuffle maintains elements
        shuffled = s.shuffle()
        self.assertEqual(sorted(shuffled), sorted(nums))
        
        # Test reset restores original
        self.assertEqual(s.reset(), [1, 2, 3])
        
        # Test another shuffle
        shuffled2 = s.shuffle()
        self.assertEqual(sorted(shuffled2), sorted(nums))
        
    def test_single_element(self):
        s = Solution([5])
        self.assertEqual(s.shuffle(), [5])
        self.assertEqual(s.reset(), [5])

if __name__ == '__main__':
    unittest.main()
