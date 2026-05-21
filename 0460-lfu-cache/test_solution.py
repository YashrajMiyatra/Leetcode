import unittest
from solution import LFUCache

class TestLFUCache(unittest.TestCase):
    def test_example_1(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)       # cache=[1,2], cnt(1)=2, cnt(2)=1
        cache.put(3, 3)                         # cnt(2)=1 is smallest -> evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)       # cnt(3)=2
        cache.put(4, 4)                         # cnt(1)=2, cnt(3)=2. Both tied but 1 is LRU -> evicts 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_capacity_0(self):
        cache = LFUCache(0)
        cache.put(1, 1)                         # capacity is 0, should not insert
        self.assertEqual(cache.get(1), -1)

    def test_capacity_1(self):
        cache = LFUCache(1)
        cache.put(2, 1)
        self.assertEqual(cache.get(2), 1)
        cache.put(3, 2)                         # evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 2)

    def test_frequency_promotion_and_eviction(self):
        cache = LFUCache(3)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)
        
        # Access 1 and 2 multiple times
        cache.get(1)                            # cnt(1) = 2
        cache.get(1)                            # cnt(1) = 3
        cache.get(2)                            # cnt(2) = 2
        
        # Now: cnt(1)=3, cnt(2)=2, cnt(3)=1
        cache.put(4, 40)                        # cnt(3)=1 is smallest -> evicts 3
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(4), 40)

if __name__ == '__main__':
    unittest.main()
