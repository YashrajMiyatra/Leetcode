import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.minimumDeleteSum("sea", "eat"), 231)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.minimumDeleteSum("delete", "leet"), 403)

    def test_no_common(self):
        s = Solution()
        self.assertEqual(s.minimumDeleteSum("a", "b"), 195) # 97 + 98 = 195

    def test_exact_match(self):
        s = Solution()
        self.assertEqual(s.minimumDeleteSum("hello", "hello"), 0)

if __name__ == '__main__':
    unittest.main()
