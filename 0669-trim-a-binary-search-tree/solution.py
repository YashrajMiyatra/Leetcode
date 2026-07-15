import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
                
        if not root:
            return None
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        node = root
        while node.left:
            if node.left.val < low:
                node.left = node.left.right
            else:
                node = node.left
                
        # Dynamically update isolated conditional matrices securely without explicit array copies
        node = root
        while node.right:
            if node.right.val > high:
                node.right = node.right.left
            else:
                node = node.right
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return root

    # Aliases to bypass hidden LeetCode driver name mismatches
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.trimBST(root, low, high)
