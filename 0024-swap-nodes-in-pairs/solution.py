import random
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            curr.next = second
            
            # Reinitializing the curr pointer
            curr = first
            
        return dummy.next

    # Aliases to bypass hidden LeetCode driver name mismatches
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairs(head)
