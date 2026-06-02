import unittest
from solution import FrontMiddleBackQueue

class TestFrontMiddleBackQueue(unittest.TestCase):
    def test_example(self):
        q = FrontMiddleBackQueue()
        q.pushFront(1)
        q.pushBack(2)
        q.pushMiddle(3)
        q.pushMiddle(4)
        self.assertEqual(q.popFront(), 1)
        self.assertEqual(q.popMiddle(), 3)
        self.assertEqual(q.popMiddle(), 4)
        self.assertEqual(q.popBack(), 2)
        self.assertEqual(q.popFront(), -1)

if __name__ == '__main__':
    unittest.main()
