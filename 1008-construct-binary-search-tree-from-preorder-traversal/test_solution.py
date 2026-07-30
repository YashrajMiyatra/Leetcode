import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import builtins
builtins.TreeNode = TreeNode

from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = self.solution.bstFromPreorder([8,5,1,7,10,12])
        self.assertEqual(root.val, 8)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.right.val, 10)
        self.assertEqual(root.left.left.val, 1)
        self.assertEqual(root.left.right.val, 7)
        self.assertEqual(root.right.right.val, 12)

    def test_example_2(self):
        root = self.solution.bstFromPreorder([1,3])
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 3)

if __name__ == '__main__':
    unittest.main()
