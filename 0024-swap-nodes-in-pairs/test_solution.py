import unittest
from solution import Solution, ListNode

def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = build_list([1,2,3,4])
        res = self.solution.swapPairs(head)
        self.assertEqual(list_to_array(res), [2,1,4,3])

    def test_example_2(self):
        head = build_list([])
        res = self.solution.swapPairs(head)
        self.assertEqual(list_to_array(res), [])

    def test_example_3(self):
        head = build_list([1])
        res = self.solution.swapPairs(head)
        self.assertEqual(list_to_array(res), [1])

    def test_example_4(self):
        head = build_list([1,2,3])
        res = self.solution.swapPairs(head)
        self.assertEqual(list_to_array(res), [2,1,3])

if __name__ == '__main__':
    unittest.main()
