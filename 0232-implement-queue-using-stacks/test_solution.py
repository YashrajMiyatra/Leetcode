import unittest
from solution import MyQueue

class TestMyQueue(unittest.TestCase):
    def test_example(self):
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.empty(), False)

if __name__ == '__main__':
    unittest.main()
