import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def tree_to_list(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        res = self.solution.trimBST(root, 1, 2)
        self.assertEqual(self.tree_to_list(res), [1, None, 2])

    def test_example_2(self):
        root = TreeNode(3)
        root.left = TreeNode(0)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(1)
        res = self.solution.trimBST(root, 1, 3)
        self.assertEqual(self.tree_to_list(res), [3, 2, None, 1])

if __name__ == '__main__':
    unittest.main()
