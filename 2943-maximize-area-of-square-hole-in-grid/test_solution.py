import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareHoleArea(2, 1, [2,3], [2]), 4)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareHoleArea(1, 1, [2], [2]), 4)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.maximizeSquareHoleArea(2, 3, [2,3], [2,4]), 4)

if __name__ == '__main__':
    unittest.main()
