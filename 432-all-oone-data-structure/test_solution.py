import unittest
from solution import AllOne

class TestSolution(unittest.TestCase):
    def test_example(self):
        obj = AllOne()
        obj.inc("hello")
        obj.inc("hello")
        self.assertEqual(obj.getMaxKey(), "hello")
        self.assertEqual(obj.getMinKey(), "hello")
        obj.inc("leet")
        self.assertEqual(obj.getMaxKey(), "hello")
        self.assertEqual(obj.getMinKey(), "leet")

    def test_decrement(self):
        obj = AllOne()
        obj.inc("a")
        obj.inc("b")
        obj.inc("b")
        obj.inc("c")
        obj.inc("c")
        obj.inc("c")
        self.assertEqual(obj.getMaxKey(), "c")
        self.assertEqual(obj.getMinKey(), "a")
        
        obj.dec("a")
        self.assertEqual(obj.getMinKey(), "b")
        
        obj.dec("c")
        obj.dec("c")
        self.assertEqual(obj.getMaxKey(), "b")
        self.assertEqual(obj.getMinKey(), "c")

    def test_empty(self):
        obj = AllOne()
        self.assertEqual(obj.getMaxKey(), "")
        self.assertEqual(obj.getMinKey(), "")
        obj.inc("a")
        obj.dec("a")
        self.assertEqual(obj.getMaxKey(), "")

if __name__ == '__main__':
    unittest.main()
