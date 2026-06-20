import unittest
from solution import MyCircularQueue

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        q = MyCircularQueue(3)
        self.assertEqual(q.enQueue(1), True)
        self.assertEqual(q.enQueue(2), True)
        self.assertEqual(q.enQueue(3), True)
        self.assertEqual(q.enQueue(4), False)
        self.assertEqual(q.Rear(), 3)
        self.assertEqual(q.isFull(), True)
        self.assertEqual(q.deQueue(), True)
        self.assertEqual(q.enQueue(4), True)
        self.assertEqual(q.Rear(), 4)

if __name__ == '__main__':
    unittest.main()
