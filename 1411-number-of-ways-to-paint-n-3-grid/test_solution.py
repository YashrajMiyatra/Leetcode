import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        s = Solution()
        self.assertEqual(s.numOfWays(1), 12)

    def test_example_2(self):
        s = Solution()
        self.assertEqual(s.numOfWays(5000), 30228214)

    def test_small_grid(self):
        s = Solution()
        self.assertEqual(s.numOfWays(2), 54)
        
    def test_three(self):
        s = Solution()
        self.assertEqual(s.numOfWays(3), 246)

if __name__ == '__main__':
    unittest.main()
