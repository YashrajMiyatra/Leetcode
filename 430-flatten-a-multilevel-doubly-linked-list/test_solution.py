import unittest
from solution import Solution, Node

class TestSolution(unittest.TestCase):
    def test_example1(self):
        # 1-2-3
        #   |
        #   4-5
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n5 = Node(5)
        
        n1.next = n2; n2.prev = n1
        n2.next = n3; n3.prev = n2
        n4.next = n5; n5.prev = n4
        n2.child = n4
        
        s = Solution()
        res = s.flatten(n1)
        
        vals = []
        curr = res
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        self.assertEqual(vals, [1, 2, 4, 5, 3])
        
    def test_empty(self):
        s = Solution()
        self.assertIsNone(s.flatten(None))

if __name__ == '__main__':
    unittest.main()
