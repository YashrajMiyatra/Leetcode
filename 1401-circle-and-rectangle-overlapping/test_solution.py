import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertTrue(s.checkOverlap(1, 0, 0, 1, -1, 3, 1))

    def test_example2(self):
        s = Solution()
        self.assertFalse(s.checkOverlap(1, 1, 1, 1, -3, 2, -1))

    def test_example3(self):
        s = Solution()
        self.assertTrue(s.checkOverlap(1, 0, 0, -1, 0, 0, 1))

if __name__ == '__main__':
    unittest.main()
