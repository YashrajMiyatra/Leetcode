import unittest
from solution import RandomizedSet

class TestSolution(unittest.TestCase):
    def test_example(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(1))
        self.assertFalse(rs.remove(2))
        self.assertTrue(rs.insert(2))
        
        # Should return 1 or 2
        val = rs.getRandom()
        self.assertIn(val, [1, 2])
        
        self.assertTrue(rs.remove(1))
        self.assertFalse(rs.insert(2))
        
        # Since 1 is removed, should always return 2
        self.assertEqual(rs.getRandom(), 2)

    def test_repeated_insert_remove(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(0))
        self.assertTrue(rs.insert(1))
        self.assertTrue(rs.remove(0))
        self.assertTrue(rs.insert(2))
        self.assertTrue(rs.remove(1))
        self.assertEqual(rs.getRandom(), 2)

if __name__ == '__main__':
    unittest.main()
