import unittest
from solution import MKAverage

class TestMKAverage(unittest.TestCase):
    def test_example_1(self):
        obj = MKAverage(3, 1)
        obj.addElement(3)
        obj.addElement(1)
        self.assertEqual(obj.calculateMKAverage(), -1)
        obj.addElement(10)
        self.assertEqual(obj.calculateMKAverage(), 3)
        obj.addElement(5)
        obj.addElement(5)
        obj.addElement(5)
        self.assertEqual(obj.calculateMKAverage(), 5)

if __name__ == '__main__':
    unittest.main()
