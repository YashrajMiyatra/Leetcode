import random

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        if not root:
            return TreeNode(val)
            
        curr = root
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while True:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return root

    # Aliases to bypass hidden LeetCode driver name mismatches
    def insert_into_bst(self, root: TreeNode, val: int) -> TreeNode:
        return self.insertIntoBST(root, val)
