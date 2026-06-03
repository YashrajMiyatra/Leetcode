import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2), 45)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2), 16)

    def test_no_overlap(self):
        s = Solution()
        self.assertEqual(s.computeArea(0, 0, 2, 2, 3, 3, 5, 5), 8)

    def test_touching(self):
        s = Solution()
        self.assertEqual(s.computeArea(0, 0, 2, 2, 2, 0, 4, 2), 8)

if __name__ == '__main__':
    unittest.main()
