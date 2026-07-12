import unittest
from solution import Solution

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Inject ListNode into solution module to make tests work without redefining
import solution
solution.ListNode = ListNode

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    cycle_node = None
    if pos == 0:
        cycle_node = head
    
    for i in range(1, len(values)):
        curr.next = ListNode(values[i])
        curr = curr.next
        if i == pos:
            cycle_node = curr
            
    if cycle_node:
        curr.next = cycle_node
        
    return head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = create_linked_list_with_cycle([3,2,0,-4], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_example_2(self):
        head = create_linked_list_with_cycle([1,2], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_example_3(self):
        head = create_linked_list_with_cycle([1], -1)
        self.assertFalse(self.solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main()
