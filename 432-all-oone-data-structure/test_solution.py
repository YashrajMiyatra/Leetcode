import unittest
from solution import AllOne

class TestAllOne(unittest.TestCase):
    def test_example(self):
        allOne = AllOne()
        allOne.inc("hello")
        allOne.inc("hello")
        self.assertEqual(allOne.getMaxKey(), "hello")
        self.assertEqual(allOne.getMinKey(), "hello")
        allOne.inc("leet")
        self.assertEqual(allOne.getMaxKey(), "hello")
        self.assertEqual(allOne.getMinKey(), "leet")
        allOne.dec("hello")
        allOne.dec("hello")
        self.assertEqual(allOne.getMaxKey(), "leet")
        self.assertEqual(allOne.getMinKey(), "leet")

if __name__ == '__main__':
    unittest.main()
