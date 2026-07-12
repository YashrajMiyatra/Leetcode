import unittest
from solution import Solution, ListNode

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = build_list([1,2,3,4,5])
        res = self.solution.rotateRight(head, 2)
        self.assertEqual(list_to_array(res), [4,5,1,2,3])

    def test_example_2(self):
        head = build_list([0,1,2])
        res = self.solution.rotateRight(head, 4)
        self.assertEqual(list_to_array(res), [2,0,1])

if __name__ == '__main__':
    unittest.main()
