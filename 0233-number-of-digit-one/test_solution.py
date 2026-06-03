import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.countDigitOne(13), 6)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.countDigitOne(0), 0)

    def test_boundary(self):
        s = Solution()
        self.assertEqual(s.countDigitOne(20), 12)

    def test_large(self):
        s = Solution()
        # countDigitOne(100) = 21 (1 in tens place 10 times, 1 in units place 10 times + 1 in hundreds place)
        self.assertEqual(s.countDigitOne(100), 21)

if __name__ == '__main__':
    unittest.main()
