import unittest
from typing import Optional
from solution import Solution, TreeNode

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def is_balanced(node):
    def check(n):
        if not n: return 0
        l = check(n.left)
        if l == -1: return -1
        r = check(n.right)
        if r == -1: return -1
        if abs(l - r) > 1: return -1
        return max(l, r) + 1
    return check(node) != -1

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return is_bst(node.left, min_val, node.val) and is_bst(node.right, node.val, max_val)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = build_tree([1,None,2,None,3,None,4,None,None])
        res = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(res))
        self.assertTrue(is_bst(res))

    def test_example_2(self):
        root = build_tree([2,1,3])
        res = self.solution.balanceBST(root)
        self.assertTrue(is_balanced(res))
        self.assertTrue(is_bst(res))

if __name__ == '__main__':
    unittest.main()
