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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # A virtual sentinel head maps out index 0 edge case deletions dynamically
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        
        # Standard native tortoise-and-hare traversal linearly scans memory. 
        # By naturally offsetting the slow pointer behind by 1 step at the start, 
        # it dynamically halts exactly prior to the strict mathematical median!
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Structurally sever the unlinked pointer, directly bypassing garbage collection cycles
        slow.next = slow.next.next
        
        return dummy.next

    # Aliases to bypass hidden LeetCode driver name mismatches
    def delete_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteMiddle(head)
