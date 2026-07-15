import unittest
from solution import RandomizedSet

class TestRandomizedSet(unittest.TestCase):
    def test_example_1(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(1))
        self.assertFalse(obj.remove(2))
        self.assertTrue(obj.insert(2))
        val = obj.getRandom()
        self.assertTrue(val in [1, 2])
        self.assertTrue(obj.remove(1))
        self.assertFalse(obj.insert(2))
        self.assertEqual(obj.getRandom(), 2)

if __name__ == '__main__':
    unittest.main()
