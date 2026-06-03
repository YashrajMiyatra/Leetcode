import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        
        s = Solution()
        self.assertEqual(s.maxLevelSum(root), 2)

    def test_example2(self):
        root = TreeNode(989)
        root.right = TreeNode(10250)
        root.right.left = TreeNode(98693)
        root.right.right = TreeNode(-89388)
        root.right.right.right = TreeNode(-32127)
        
        s = Solution()
        self.assertEqual(s.maxLevelSum(root), 2)

if __name__ == '__main__':
    unittest.main()
