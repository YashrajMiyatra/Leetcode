import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_example2(self):
        self.assertEqual(self.sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_example3(self):
        self.assertEqual(self.sol.convert("A", 1), "A")

    def test_two_rows(self):
        self.assertEqual(self.sol.convert("ABCD", 2), "ACBD")

    def test_numrows_greater_than_length(self):
        self.assertEqual(self.sol.convert("ABC", 5), "ABC")

if __name__ == '__main__':
    unittest.main()
