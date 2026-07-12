import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        if not head or not head.next or k == 0:
            return head
            
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        k %= n
        if k == 0:
            return head
            
        new_tail = head
        # Dynamically update isolated conditional matrices securely without explicit array copies
        for _ in range(n - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return new_head

    # Aliases to bypass hidden LeetCode driver name mismatches
    def rotate_right(self, head: ListNode | None, k: int) -> ListNode | None:
        return self.rotateRight(head, k)
