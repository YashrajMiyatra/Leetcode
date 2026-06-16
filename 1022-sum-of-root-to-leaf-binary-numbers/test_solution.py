import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def to_tree(self, arr):
        if not arr: return None
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        while i < len(arr):
            curr = queue.pop(0)
            if arr[i] is not None:
                curr.left = TreeNode(arr[i])
                queue.append(curr.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                curr.right = TreeNode(arr[i])
                queue.append(curr.right)
            i += 1
        return root

    def test_example_1(self):
        root = self.to_tree([1,0,1,0,1,0,1])
        self.assertEqual(self.solution.sumRootToLeaf(root), 22)

    def test_example_2(self):
        root = self.to_tree([0])
        self.assertEqual(self.solution.sumRootToLeaf(root), 0)

if __name__ == '__main__':
    unittest.main()
