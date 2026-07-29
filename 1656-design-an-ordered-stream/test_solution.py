import unittest
from solution import OrderedStream

class TestOrderedStream(unittest.TestCase):
    def test_example_1(self):
        os = OrderedStream(5)
        self.assertEqual(os.insert(3, "ccccc"), [])
        self.assertEqual(os.insert(1, "aaaaa"), ["aaaaa"])
        self.assertEqual(os.insert(2, "bbbbb"), ["bbbbb", "ccccc"])
        self.assertEqual(os.insert(5, "eeeee"), [])
        self.assertEqual(os.insert(4, "ddddd"), ["ddddd", "eeeee"])

if __name__ == '__main__':
    unittest.main()
