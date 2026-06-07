from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS helper returns (LCA_node, max_depth) for the subtree
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0
                
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            # If depths of both subtrees are equal, the current node is the LCA
            if left_depth == right_depth:
                return node, left_depth + 1
            # If left subtree is deeper, the LCA is in the left subtree
            elif left_depth > right_depth:
                return left_node, left_depth + 1
            # If right subtree is deeper, the LCA is in the right subtree
            else:
                return right_node, right_depth + 1
                
        return dfs(root)[0]
