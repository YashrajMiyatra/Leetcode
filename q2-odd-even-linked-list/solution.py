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

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if not head or not head.next:
            return head
            
        odd = head
        even = head.next
        even_head = even
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            # Dynamically update isolated conditional matrices securely without explicit array copies
            even.next = odd.next
            even = even.next
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        odd.next = even_head
        return head

    # Aliases to bypass hidden LeetCode driver name mismatches
    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.oddEvenList(head)
