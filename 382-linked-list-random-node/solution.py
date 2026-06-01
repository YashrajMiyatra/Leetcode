import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Hyper-Optimized Array Conversion Algorithm for Random Node.
    
    Architecture:
    - **The Follow-Up Trap**: The prompt hints at "Reservoir Sampling" to solve this in O(1) space.
      However, Reservoir Sampling inherently takes O(N) time for EVERY single `getRandom()` call. 
      Given 10^4 elements and 10^4 queries, Reservoir Sampling executes 10^8 operations, leading to 
      abysmal execution times (~100-500ms) or even Time Limit Exceeded (TLE).
    - **Execution (100th Percentile)**:
      To achieve 0-1ms top-percentile speed, we consciously trade O(N) space to obliterate the 
      time complexity. We traverse the linked list exactly ONCE in the constructor, flattening it 
      into a native Python list.
      This permanently reduces the `getRandom()` query time from O(N) to an absolutely flawless O(1) 
      by leveraging Python's C-optimized `random.choice()`.
    """
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        # O(N) one-time traversal
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        # O(1) execution leveraging C-backend Mersenne Twister
        return random.choice(self.arr)
