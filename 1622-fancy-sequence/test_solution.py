import unittest
from solution import Fancy

class TestFancy(unittest.TestCase):
    def test_example_1(self):
        fancy = Fancy()
        fancy.append(2)
        fancy.addAll(3)
        fancy.append(7)
        fancy.multAll(2)
        self.assertEqual(fancy.getIndex(0), 10)
        fancy.addAll(3)
        fancy.append(10)
        fancy.multAll(2)
        self.assertEqual(fancy.getIndex(0), 26)
        self.assertEqual(fancy.getIndex(1), 34)
        self.assertEqual(fancy.getIndex(2), 20)

if __name__ == '__main__':
    unittest.main()
