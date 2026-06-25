import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
        self.assertEqual(self.solution.longestUnivaluePath(root), 2)

    def test_example_2(self):
        root = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))
        self.assertEqual(self.solution.longestUnivaluePath(root), 2)

if __name__ == '__main__':
    unittest.main()
