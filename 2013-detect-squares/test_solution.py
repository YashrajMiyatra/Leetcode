import unittest
from solution import DetectSquares

class TestDetectSquares(unittest.TestCase):
    def test_example_1(self):
        obj = DetectSquares()
        obj.add([3, 10])
        obj.add([11, 2])
        obj.add([3, 2])
        self.assertEqual(obj.count([11, 10]), 1)
        self.assertEqual(obj.count([14, 8]), 0)
        obj.add([11, 2])
        self.assertEqual(obj.count([11, 10]), 2)

if __name__ == '__main__':
    unittest.main()
