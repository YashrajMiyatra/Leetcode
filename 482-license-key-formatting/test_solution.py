import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.licenseKeyFormatting("5F3Z-2e-9-w", 4), "5F3Z-2E9W")

    def test_example_2(self):
        self.assertEqual(self.solution.licenseKeyFormatting("2-5g-3-J", 2), "2-5G-3J")

    def test_empty(self):
        self.assertEqual(self.solution.licenseKeyFormatting("---", 3), "")

    def test_single(self):
        self.assertEqual(self.solution.licenseKeyFormatting("2", 2), "2")

if __name__ == '__main__':
    unittest.main()
