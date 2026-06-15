import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def to_list(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    def to_nodes(self, arr):
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def test_example_1(self):
        head = self.to_nodes([1,3,4,7,1,2,6])
        res = self.solution.deleteMiddle(head)
        self.assertEqual(self.to_list(res), [1,3,4,1,2,6])

    def test_example_2(self):
        head = self.to_nodes([1,2,3,4])
        res = self.solution.deleteMiddle(head)
        self.assertEqual(self.to_list(res), [1,2,4])

    def test_example_3(self):
        head = self.to_nodes([2,1])
        res = self.solution.deleteMiddle(head)
        self.assertEqual(self.to_list(res), [2])

if __name__ == '__main__':
    unittest.main()
