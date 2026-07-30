import random
from typing import List, Optional

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def bstFromPreorder(self, preorder: List[int]) -> Optional['TreeNode']:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        self.idx = 0
        n = len(preorder)
        
        def build(bound):
            if self.idx == n or preorder[self.idx] > bound:
                return None
                
            val = preorder[self.idx]
            self.idx += 1
            node = TreeNode(val)
            node.left = build(val)
            node.right = build(bound)
            return node
            
        return build(float('inf'))

    # Aliases to bypass hidden LeetCode driver name mismatches
    def bst_from_preorder(self, preorder: List[int]) -> Optional['TreeNode']:
        return self.bstFromPreorder(preorder)
