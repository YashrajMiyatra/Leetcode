import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    def test_example(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        s = Solution(head)
        
        # Test if it returns valid values
        valid_values = {1, 2, 3}
        for _ in range(10):
            val = s.getRandom()
            self.assertIn(val, valid_values)
            
    def test_single_node(self):
        head = ListNode(5)
        s = Solution(head)
        self.assertEqual(s.getRandom(), 5)
        self.assertEqual(s.getRandom(), 5)

if __name__ == '__main__':
    unittest.main()
