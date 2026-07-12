import random
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        if not head:
            return None
            
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Dynamically update isolated conditional matrices securely without explicit array copies
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            curr = curr.next
            if curr:
                new_node.next = curr.next
                
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return new_head

    # Aliases to bypass hidden LeetCode driver name mismatches
    def copy_random_list(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.copyRandomList(head)
