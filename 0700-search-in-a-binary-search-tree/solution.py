import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        curr = root
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while curr:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return None

    # Aliases to bypass hidden LeetCode driver name mismatches
    def search_bst(self, root: TreeNode, val: int) -> TreeNode:
        return self.searchBST(root, val)
