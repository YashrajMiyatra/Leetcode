import unittest
from solution import LFUCache

class TestLFUCache(unittest.TestCase):
    def test_example(self):
        lfu = LFUCache(2)
        lfu.put(1, 1)
        lfu.put(2, 2)
        self.assertEqual(lfu.get(1), 1)
        lfu.put(3, 3)
        self.assertEqual(lfu.get(2), -1)
        self.assertEqual(lfu.get(3), 3)
        lfu.put(4, 4)
        self.assertEqual(lfu.get(1), -1)
        self.assertEqual(lfu.get(3), 3)
        self.assertEqual(lfu.get(4), 4)

    def test_capacity_zero(self):
        lfu = LFUCache(0)
        lfu.put(1, 1)
        self.assertEqual(lfu.get(1), -1)

if __name__ == '__main__':
    unittest.main()
