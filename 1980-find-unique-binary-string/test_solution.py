import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Cantor's diagonal for ["01", "10"] gives "11"
        self.assertEqual(self.solution.findDifferentBinaryString(["01","10"]), "11")

    def test_example_2(self):
        # Cantor's diagonal for ["00", "01"] gives "10"
        self.assertEqual(self.solution.findDifferentBinaryString(["00","01"]), "10")

    def test_example_3(self):
        # Cantor's diagonal for ["111", "011", "001"] gives "000"
        self.assertEqual(self.solution.findDifferentBinaryString(["111","011","001"]), "000")

if __name__ == '__main__':
    unittest.main()
