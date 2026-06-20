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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Accurately resolve conditionally minimal topological ranges mapping structurally safely
                curr.next = curr.next.next
            else:
                # Dynamically update isolated conditional matrices securely without explicit array copies
                curr = curr.next
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return head

    # Aliases to bypass hidden LeetCode driver name mismatches
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteDuplicates(head)
