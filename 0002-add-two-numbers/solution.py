# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Conditionally define ListNode for local testing/running without overriding Leetcode's global definition
if 'ListNode' not in globals():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        Adds two numbers represented by linked lists in reverse order.
        
        Time Complexity: O(max(N, M)) - Single pass traversing both lists.
        Space Complexity: O(max(N, M)) - Memory for the result linked list.
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 is not None or l2 is not None or carry > 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create next node
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Advance pointers
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy.next
