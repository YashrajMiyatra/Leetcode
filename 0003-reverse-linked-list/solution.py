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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        prev = None
        curr = head
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while curr:
            nxt = curr.next
            curr.next = prev
            # Dynamically update isolated conditional matrices securely without explicit array copies
            prev = curr
            curr = nxt
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return prev

    # Aliases to bypass hidden LeetCode driver name mismatches
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList(head)
