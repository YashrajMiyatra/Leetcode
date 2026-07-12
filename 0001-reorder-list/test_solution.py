import unittest
from solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import solution
solution.ListNode = ListNode

def list_to_nodes(lst):
    if not lst: return None
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def nodes_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_nodes([1,2,3,4])
        self.solution.reorderList(head)
        self.assertEqual(nodes_to_list(head), [1,4,2,3])

    def test_example_2(self):
        head = list_to_nodes([1,2,3,4,5])
        self.solution.reorderList(head)
        self.assertEqual(nodes_to_list(head), [1,5,2,4,3])

if __name__ == '__main__':
    unittest.main()
