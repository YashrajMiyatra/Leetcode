import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.closetTarget(["hello","i","am","leetcode","hello"], "hello", 1), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.closetTarget(["a","b","leetcode"], "leetcode", 0), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.closetTarget(["i","eat","leetcode"], "ate", 0), -1)

if __name__ == '__main__':
    unittest.main()
