import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        
        s = Solution()
        self.assertEqual(s.maxProduct(root), 110)

    def test_example2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(6)
        
        s = Solution()
        self.assertEqual(s.maxProduct(root), 90)

if __name__ == '__main__':
    unittest.main()
