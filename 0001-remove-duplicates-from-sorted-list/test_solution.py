import unittest
from solution import Solution, ListNode

def list_to_nodes(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def nodes_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_nodes([1,1,2])
        res = self.solution.deleteDuplicates(head)
        self.assertEqual(nodes_to_list(res), [1,2])

    def test_example_2(self):
        head = list_to_nodes([1,1,2,3,3])
        res = self.solution.deleteDuplicates(head)
        self.assertEqual(nodes_to_list(res), [1,2,3])

if __name__ == '__main__':
    unittest.main()
