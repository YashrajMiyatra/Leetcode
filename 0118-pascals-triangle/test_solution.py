import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.generate(1), [[1]])

    def test_two_rows(self):
        s = Solution()
        self.assertEqual(s.generate(2), [[1], [1,1]])

if __name__ == '__main__':
    unittest.main()
