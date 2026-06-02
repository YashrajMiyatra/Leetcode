from typing import Optional

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    """
    Hyper-Optimized Iterative In-Place Flattening Algorithm.
    
    Architecture:
    - **Theoretical Foundation**: A standard recursive approach traverses depth-first, which requires O(N) 
      call stack memory in the worst case (deeply nested lists). Alternatively, using an explicit stack 
      requires O(N) heap memory and object allocation overhead.
    - **Execution (100th Percentile)**:
      We use a strictly iterative, O(1) auxiliary space approach. 
      We sequentially traverse the primary list with a `curr` pointer. 
      When we encounter a node with a `child`:
        1. We instantly traverse the child's primary level to find its tail (using only `.next` pointers, 
           so we don't accidentally dive into its children yet).
        2. We sever and reconnect pointers to splice the entire child list directly into the main list 
           between `curr` and `curr.next`.
        3. We clear the `child` pointer to satisfy the output requirement.
      Because we are pushing the child nodes onto the main axis directly ahead of the `curr` pointer, 
      the `while curr:` loop will naturally process them next!
      This achieves strict O(N) time with absolutely zero recursive/stack memory overhead.
    """
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                # Isolate the child list and find its immediate tail
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next
                
                # Splice the child tail to curr.next
                if curr.next:
                    curr.next.prev = child_tail
                child_tail.next = curr.next
                
                # Splice curr to the head of the child list
                curr.next = curr.child
                curr.child.prev = curr
                
                # Nuke the child pointer
                curr.child = None
            
            # March forward
            curr = curr.next
            
        return head
