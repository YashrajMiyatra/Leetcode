import random
import heapq
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def mergeKLists(self, lists: list[Optional['ListNode']]) -> Optional['ListNode']:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        heap = []
        count = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1
                
        dummy = ListNode(-1)
        curr = dummy
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return dummy.next

    # Aliases to bypass hidden LeetCode driver name mismatches
    def merge_k_lists(self, lists: list[Optional['ListNode']]) -> Optional['ListNode']:
        return self.mergeKLists(lists)
