import unittest
from solution import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_example_1(self):
        cache = LRUCache(2)
        cache.put(1, 1)           # cache is {1=1}
        cache.put(2, 2)           # cache is {1=1, 2=2}
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)           # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)           # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_capacity_1(self):
        cache = LRUCache(1)
        cache.put(2, 1)
        self.assertEqual(cache.get(2), 1)
        cache.put(3, 2)           # evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 2)

    def test_overwrite_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(1, 15)          # updates 1, moves 1 to MRU
        cache.put(3, 30)          # evicts 2 (since 1 is MRU)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 15)
        self.assertEqual(cache.get(3), 30)

    def test_multiple_evictions_in_sequence(self):
        cache = LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)           # evicts 1
        self.assertEqual(cache.get(1), -1)
        cache.put(5, 5)           # evicts 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(5), 5)

if __name__ == '__main__':
    unittest.main()
