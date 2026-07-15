import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 1)

if __name__ == '__main__':
    unittest.main()
