import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.digitFrequencyScore(122), 5)

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.digitFrequencyScore(101), 2)
        
    def test_large_number(self):
        s = Solution()
        self.assertEqual(s.digitFrequencyScore(999999999), 81)

if __name__ == '__main__':
    unittest.main()
