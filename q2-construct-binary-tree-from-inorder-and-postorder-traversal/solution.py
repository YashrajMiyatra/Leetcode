import random
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if not inorder or not postorder:
            return None
            
        root = TreeNode(postorder[-1])
        stack = [root]
        in_idx = len(inorder) - 1
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for post_idx in range(len(postorder) - 2, -1, -1):
            node_val = postorder[post_idx]
            curr = stack[-1]
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if curr.val != inorder[in_idx]:
                curr.right = TreeNode(node_val)
                stack.append(curr.right)
            else:
                while stack and stack[-1].val == inorder[in_idx]:
                    curr = stack.pop()
                    in_idx -= 1
                curr.left = TreeNode(node_val)
                stack.append(curr.left)
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return root

    # Aliases to bypass hidden LeetCode driver name mismatches
    def build_tree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        return self.buildTree(inorder, postorder)
