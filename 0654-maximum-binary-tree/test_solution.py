import unittest
from solution import Solution, TreeNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = self.solution.constructMaximumBinaryTree([3,2,1,6,0,5])
        self.assertEqual(root.val, 6)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 5)

if __name__ == '__main__':
    unittest.main()
