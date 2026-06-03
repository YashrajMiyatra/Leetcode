import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.combine(4, 2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.combine(1, 1), [[1]])

    def test_max_constraints(self):
        s = Solution()
        ans = s.combine(20, 3)
        self.assertEqual(len(ans), 1140)

if __name__ == '__main__':
    unittest.main()
