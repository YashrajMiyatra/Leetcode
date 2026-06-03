import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.rearrangeSticks(3, 2), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.rearrangeSticks(5, 5), 1)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.rearrangeSticks(20, 11), 647427950)

    def test_k_equals_1(self):
        s = Solution()
        # 4! = 24
        self.assertEqual(s.rearrangeSticks(5, 1), 24)

if __name__ == '__main__':
    unittest.main()
