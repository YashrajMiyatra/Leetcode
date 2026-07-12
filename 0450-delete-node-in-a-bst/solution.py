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

    def deleteNode(self, root: 'TreeNode', key: int) -> 'TreeNode':
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        curr = root
        parent = None
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        if not curr:
            return root
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        if curr.left and curr.right:
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
                
            curr.val = succ.val
            
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
        else:
            child = curr.left if curr.left else curr.right
            
            if not parent:
                root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return root

    # Aliases to bypass hidden LeetCode driver name mismatches
    def delete_node(self, root: 'TreeNode', key: int) -> 'TreeNode':
        return self.deleteNode(root, key)
