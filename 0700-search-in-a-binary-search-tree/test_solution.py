import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        res = self.solution.searchBST(root, 2)
        self.assertIsNotNone(res)
        self.assertEqual(res.val, 2)
        self.assertEqual(res.left.val, 1)
        self.assertEqual(res.right.val, 3)

    def test_example_2(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        res = self.solution.searchBST(root, 5)
        self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()
