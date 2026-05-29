import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minElement([10, 12, 13, 14]), 1)

    def test_example2(self):
        self.assertEqual(self.sol.minElement([1, 2, 3, 4]), 1)

    def test_example3(self):
        self.assertEqual(self.sol.minElement([999, 19, 199]), 10)

    def test_single_element(self):
        self.assertEqual(self.sol.minElement([9999]), 36)

    def test_zero(self):
        self.assertEqual(self.sol.minElement([0, 100]), 0)

if __name__ == '__main__':
    unittest.main()
