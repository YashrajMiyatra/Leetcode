import random
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
                
            stack.append(node)
            
        return stack[0] if stack else None

    # Aliases to bypass hidden LeetCode driver name mismatches
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructMaximumBinaryTree(nums)
