import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.bitwiseComplement(5), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.bitwiseComplement(7), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.bitwiseComplement(10), 5)
        
    def test_zero(self):
        self.assertEqual(self.solution.bitwiseComplement(0), 1)

if __name__ == '__main__':
    unittest.main()
