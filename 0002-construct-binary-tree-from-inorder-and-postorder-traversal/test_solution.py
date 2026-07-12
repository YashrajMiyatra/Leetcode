import unittest
from solution import Solution, TreeNode

def tree_to_list(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr:
            res.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        res = self.solution.buildTree(inorder, postorder)
        self.assertEqual(tree_to_list(res), [3,9,20,None,None,15,7])

    def test_example_2(self):
        inorder = [-1]
        postorder = [-1]
        res = self.solution.buildTree(inorder, postorder)
        self.assertEqual(tree_to_list(res), [-1])

if __name__ == '__main__':
    unittest.main()
