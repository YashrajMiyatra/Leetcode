import unittest
from solution import RangeModule

class TestSolution(unittest.TestCase):
    def test_example(self):
        rm = RangeModule()
        rm.addRange(10, 20)
        rm.removeRange(14, 16)
        self.assertTrue(rm.queryRange(10, 14))
        self.assertFalse(rm.queryRange(13, 15))
        self.assertTrue(rm.queryRange(16, 17))
        
    def test_merges(self):
        rm = RangeModule()
        rm.addRange(10, 20)
        rm.addRange(20, 30)
        # Should seamlessly merge into [10, 30]
        self.assertTrue(rm.queryRange(15, 25))
        
        rm.removeRange(15, 25)
        # Should fragment into [10, 15) and [25, 30)
        self.assertTrue(rm.queryRange(10, 15))
        self.assertTrue(rm.queryRange(25, 30))
        self.assertFalse(rm.queryRange(14, 16))
        self.assertFalse(rm.queryRange(24, 26))
        
    def test_overwrites(self):
        rm = RangeModule()
        rm.addRange(10, 20)
        rm.addRange(30, 40)
        # Overwrite the hole
        rm.addRange(15, 35)
        self.assertTrue(rm.queryRange(10, 40))

if __name__ == '__main__':
    unittest.main()
