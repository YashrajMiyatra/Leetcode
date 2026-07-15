import unittest
from solution import NumArray

class TestNumArray(unittest.TestCase):
    def test_example_1(self):
        numArray = NumArray([1, 3, 5])
        self.assertEqual(numArray.sumRange(0, 2), 9)
        numArray.update(1, 2)
        self.assertEqual(numArray.sumRange(0, 2), 8)

if __name__ == '__main__':
    unittest.main()
