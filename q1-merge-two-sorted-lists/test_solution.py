import unittest
from solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import solution
solution.ListNode = ListNode

def list_to_nodes(lst):
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
        l1 = list_to_nodes([1,2,4])
        l2 = list_to_nodes([1,3,4])
        res = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(nodes_to_list(res), [1,1,2,3,4,4])

    def test_example_2(self):
        res = self.solution.mergeTwoLists(None, None)
        self.assertEqual(nodes_to_list(res), [])

    def test_example_3(self):
        l2 = list_to_nodes([0])
        res = self.solution.mergeTwoLists(None, l2)
        self.assertEqual(nodes_to_list(res), [0])

if __name__ == '__main__':
    unittest.main()
