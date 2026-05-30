import unittest
from solution import KthLargest

class TestSolution(unittest.TestCase):
    def test_example1(self):
        obj = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(obj.add(3), 4)
        self.assertEqual(obj.add(5), 5)
        self.assertEqual(obj.add(10), 5)
        self.assertEqual(obj.add(9), 8)
        self.assertEqual(obj.add(4), 8)

    def test_example2(self):
        obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
        self.assertEqual(obj.add(2), 7)
        self.assertEqual(obj.add(10), 7)
        self.assertEqual(obj.add(9), 7)
        self.assertEqual(obj.add(9), 8)
        
    def test_empty_init(self):
        obj = KthLargest(1, [])
        self.assertEqual(obj.add(-3), -3)
        self.assertEqual(obj.add(-2), -2)
        self.assertEqual(obj.add(-4), -2)
        self.assertEqual(obj.add(0), 0)
        self.assertEqual(obj.add(4), 4)

if __name__ == '__main__':
    unittest.main()
