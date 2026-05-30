import unittest
from solution import RandomizedCollection

class TestSolution(unittest.TestCase):
    def test_example(self):
        rc = RandomizedCollection()
        self.assertTrue(rc.insert(1))
        self.assertFalse(rc.insert(1))
        self.assertTrue(rc.insert(2))
        
        # Should return 1 or 2
        val = rc.getRandom()
        self.assertIn(val, [1, 2])
        
        self.assertTrue(rc.remove(1))
        
        # Collection should now contain [1, 2]
        val = rc.getRandom()
        self.assertIn(val, [1, 2])

    def test_repeated_insert_remove(self):
        rc = RandomizedCollection()
        self.assertTrue(rc.insert(0))
        self.assertFalse(rc.insert(0))
        self.assertTrue(rc.remove(0))
        self.assertTrue(rc.remove(0))
        self.assertFalse(rc.remove(0))
        self.assertTrue(rc.insert(0))
        self.assertEqual(rc.getRandom(), 0)

    def test_swap_same_value(self):
        rc = RandomizedCollection()
        rc.insert(1)
        rc.insert(1)
        rc.remove(1)
        self.assertEqual(rc.getRandom(), 1)
        rc.remove(1)
        self.assertFalse(rc.remove(1))

if __name__ == '__main__':
    unittest.main()
