import unittest
from solution import DataStream

class TestDataStream(unittest.TestCase):
    def test_example_1(self):
        dataStream = DataStream(4, 3)
        self.assertFalse(dataStream.consec(4))
        self.assertFalse(dataStream.consec(4))
        self.assertTrue(dataStream.consec(4))
        self.assertFalse(dataStream.consec(3))

if __name__ == '__main__':
    unittest.main()
