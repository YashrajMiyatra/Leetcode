import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        
        s = Solution()
        ans = s.subtreeWithAllDeepest(root)
        self.assertEqual(ans.val, 2)

    def test_example2(self):
        root = TreeNode(1)
        
        s = Solution()
        ans = s.subtreeWithAllDeepest(root)
        self.assertEqual(ans.val, 1)

    def test_example3(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.right = TreeNode(2)
        
        s = Solution()
        ans = s.subtreeWithAllDeepest(root)
        self.assertEqual(ans.val, 2)

if __name__ == '__main__':
    unittest.main()
