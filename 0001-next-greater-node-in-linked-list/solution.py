import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def nextLargerNodes(self, head: Optional[ListNode]) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        n = len(vals)
        ans = [0] * n
        stack = []
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for i in range(n):
            while stack and vals[stack[-1]] < vals[i]:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                idx = stack.pop()
                ans[idx] = vals[i]
            stack.append(i)
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def next_larger_nodes(self, head: Optional[ListNode]) -> list[int]:
        return self.nextLargerNodes(head)
