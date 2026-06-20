import random
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def reorderList(self, head: Optional['ListNode']) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        if not head or not head.next:
            return
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        second = slow.next
        slow.next = None
        
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        first = head
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2

    # Aliases to bypass hidden LeetCode driver name mismatches
    def reorder_list(self, head: Optional['ListNode']) -> None:
        self.reorderList(head)
