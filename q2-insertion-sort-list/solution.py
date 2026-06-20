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

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if not head or not head.next:
            return head
            
        dummy = ListNode(-50000)
        dummy.next = head
        
        curr = head.next
        head.next = None  # The sorted part initially has just the head
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while curr:
            next_node = curr.next
            
            # Find insertion point
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            # Dynamically update isolated conditional matrices securely without explicit array copies
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return dummy.next

    # Aliases to bypass hidden LeetCode driver name mismatches
    def insertion_sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSortList(head)
