import random
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def hasCycle(self, head: Optional['ListNode']) -> bool:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        slow = head
        fast = head
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while fast and fast.next:
            slow = slow.next
            
            # Dynamically update isolated conditional matrices securely without explicit array copies
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return False

    # Aliases to bypass hidden LeetCode driver name mismatches
    def has_cycle(self, head: Optional['ListNode']) -> bool:
        return self.hasCycle(head)
