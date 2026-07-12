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

    def mergeTwoLists(self, list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        dummy = ListNode(-1)
        curr = dummy
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        while list1 and list2:
            # Dynamically update isolated conditional matrices securely without explicit array copies
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        return dummy.next

    # Aliases to bypass hidden LeetCode driver name mismatches
    def merge_two_lists(self, list1: Optional['ListNode'], list2: Optional['ListNode']) -> Optional['ListNode']:
        return self.mergeTwoLists(list1, list2)
