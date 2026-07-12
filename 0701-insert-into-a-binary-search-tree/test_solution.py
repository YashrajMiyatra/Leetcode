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
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        res = self.solution.insertIntoBST(root, 5)
        self.assertEqual(res.right.left.val, 5)

if __name__ == '__main__':
    unittest.main()
