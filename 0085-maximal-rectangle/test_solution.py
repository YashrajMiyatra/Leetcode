import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
        self.assertEqual(s.maximalRectangle(matrix), 6)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.maximalRectangle([["0"]]), 0)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.maximalRectangle([["1"]]), 1)

    def test_empty(self):
        s = Solution()
        self.assertEqual(s.maximalRectangle([]), 0)
        self.assertEqual(s.maximalRectangle([[]]), 0)

if __name__ == '__main__':
    unittest.main()
