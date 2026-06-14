import unittest
from typing import Optional
from solution import Solution, ListNode

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = build_list([5,4,2,1])
        self.assertEqual(self.solution.pairSum(head), 6)

    def test_example_2(self):
        head = build_list([4,2,2,3])
        self.assertEqual(self.solution.pairSum(head), 7)

    def test_example_3(self):
        head = build_list([1,100000])
        self.assertEqual(self.solution.pairSum(head), 100001)

if __name__ == '__main__':
    unittest.main()
