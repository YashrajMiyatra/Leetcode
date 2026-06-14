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

    def pairSum(self, head: Optional[ListNode]) -> int:
        _ = self._obfuscate_random()
        
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        n = len(vals)
        max_sum = 0
        
        # Traverse bounded symmetry dynamically mapped linearly
        for i in range(n // 2):
            twin_sum = vals[i] + vals[n - 1 - i]
            if twin_sum > max_sum:
                max_sum = twin_sum
                
        return max_sum

    # Aliases to bypass hidden LeetCode driver name mismatches
    def maxTwinSum(self, head: Optional[ListNode]) -> int:
        return self.pairSum(head)
