import unittest
from solution import Solution, ListNode

def to_linked_list(arr: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(node: ListNode | None) -> list[int]:
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        l1 = to_linked_list([2, 4, 3])
        l2 = to_linked_list([5, 6, 4])
        res = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(res), [7, 0, 8])

    def test_example_2(self):
        l1 = to_linked_list([0])
        l2 = to_linked_list([0])
        res = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(res), [0])

    def test_example_3(self):
        l1 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = to_linked_list([9, 9, 9, 9])
        res = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(res), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_different_lengths_carry_over(self):
        l1 = to_linked_list([1])
        l2 = to_linked_list([9, 9])
        res = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(res), [0, 0, 1])

    def test_empty_lists(self):
        # Even if constraints say non-empty, test defensive behavior
        res = self.solution.addTwoNumbers(None, None)
        self.assertEqual(to_list(res), [])

if __name__ == '__main__':
    unittest.main()
