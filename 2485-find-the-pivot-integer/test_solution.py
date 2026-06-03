import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.pivotInteger(8), 6)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.pivotInteger(1), 1)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.pivotInteger(4), -1)

if __name__ == '__main__':
    unittest.main()
