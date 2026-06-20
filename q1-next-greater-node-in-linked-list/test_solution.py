import unittest
from solution import Solution, ListNode

def list_to_nodes(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = list_to_nodes([2,1,5])
        self.assertEqual(self.solution.nextLargerNodes(head), [5,5,0])

    def test_example_2(self):
        head = list_to_nodes([2,7,4,3,5])
        self.assertEqual(self.solution.nextLargerNodes(head), [7,0,5,5,0])

if __name__ == '__main__':
    unittest.main()
