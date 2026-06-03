import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maxPoints([[1,1],[2,2],[3,3]]), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4)

    def test_vertical(self):
        s = Solution()
        self.assertEqual(s.maxPoints([[0,0],[0,1],[0,2],[0,3]]), 4)

    def test_horizontal(self):
        s = Solution()
        self.assertEqual(s.maxPoints([[0,0],[1,0],[2,0],[-1,0]]), 4)

if __name__ == '__main__':
    unittest.main()
