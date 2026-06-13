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

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = build_tree([3,9,20,None,None,15,7])
        self.assertEqual(self.solution.isBalanced(root), True)

    def test_example_2(self):
        root = build_tree([1,2,2,3,3,None,None,4,4])
        self.assertEqual(self.solution.isBalanced(root), False)

    def test_example_3(self):
        root = build_tree([])
        self.assertEqual(self.solution.isBalanced(root), True)

if __name__ == '__main__':
    unittest.main()
