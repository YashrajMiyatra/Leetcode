import unittest
from solution import RecentCounter

class TestRecentCounter(unittest.TestCase):
    def test_example_1(self):
        counter = RecentCounter()
        self.assertEqual(counter.ping(1), 1)
        self.assertEqual(counter.ping(100), 2)
        self.assertEqual(counter.ping(3001), 3)
        self.assertEqual(counter.ping(3002), 3)

if __name__ == '__main__':
    unittest.main()
