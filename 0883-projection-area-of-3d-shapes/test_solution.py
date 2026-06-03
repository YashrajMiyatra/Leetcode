import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.projectionArea([[1,2],[3,4]]), 17)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.projectionArea([[2]]), 5)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.projectionArea([[1,0],[0,2]]), 8)

if __name__ == '__main__':
    unittest.main()
