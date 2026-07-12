import unittest
from solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Inject ListNode into solution module to make tests work without redefining
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
        l1 = list_to_nodes([1,4,5])
        l2 = list_to_nodes([1,3,4])
        l3 = list_to_nodes([2,6])
        res = self.solution.mergeKLists([l1, l2, l3])
        self.assertEqual(nodes_to_list(res), [1,1,2,3,4,4,5,6])

    def test_example_2(self):
        res = self.solution.mergeKLists([])
        self.assertEqual(nodes_to_list(res), [])

    def test_example_3(self):
        res = self.solution.mergeKLists([list_to_nodes([])])
        self.assertEqual(nodes_to_list(res), [])

if __name__ == '__main__':
    unittest.main()
