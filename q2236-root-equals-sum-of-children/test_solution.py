import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(10, TreeNode(4), TreeNode(6))
        self.assertTrue(self.solution.checkTree(root))

    def test_example_2(self):
        root = TreeNode(5, TreeNode(3), TreeNode(1))
        self.assertFalse(self.solution.checkTree(root))

if __name__ == '__main__':
    unittest.main()
