import unittest
from solution import LFUCache

class TestSolution(unittest.TestCase):
    def test_example_1(self):
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

if __name__ == '__main__':
    unittest.main()
