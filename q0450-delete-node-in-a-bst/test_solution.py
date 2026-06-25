import unittest
from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
        res = self.solution.deleteNode(root, 3)
        self.assertEqual(res.val, 5)
        self.assertEqual(res.left.val, 4)
        self.assertEqual(res.left.left.val, 2)
        self.assertIsNone(res.left.right)

if __name__ == '__main__':
    unittest.main()
