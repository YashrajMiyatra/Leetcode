import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maxLength(["un","iq","ue"]), 4)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maxLength(["cha","r","act","ers"]), 6)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]), 26)

    def test_duplicate_self(self):
        s = Solution()
        self.assertEqual(s.maxLength(["aa", "bb"]), 0)

if __name__ == '__main__':
    unittest.main()
