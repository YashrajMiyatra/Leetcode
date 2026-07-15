import unittest
from solution import Solution, ListNode

def build_list(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def list_to_array(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        lists = [build_list([1,4,5]), build_list([1,3,4]), build_list([2,6])]
        res = self.solution.mergeKLists(lists)
        self.assertEqual(list_to_array(res), [1,1,2,3,4,4,5,6])

    def test_example_2(self):
        res = self.solution.mergeKLists([])
        self.assertEqual(list_to_array(res), [])

    def test_example_3(self):
        res = self.solution.mergeKLists([build_list([])])
        self.assertEqual(list_to_array(res), [])

if __name__ == '__main__':
    unittest.main()
