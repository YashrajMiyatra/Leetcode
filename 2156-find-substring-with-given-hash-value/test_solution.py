import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.subStrHash("leetcode", 7, 20, 2, 0), "ee")

    def test_example_2(self):
        self.assertEqual(self.solution.subStrHash("fbxzaad", 31, 100, 3, 32), "fbx")

if __name__ == '__main__':
    unittest.main()
