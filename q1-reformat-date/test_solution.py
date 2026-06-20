import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.reformatDate("20th Oct 2052"), "2052-10-20")

    def test_example_2(self):
        self.assertEqual(self.solution.reformatDate("6th Jun 1933"), "1933-06-06")

    def test_example_3(self):
        self.assertEqual(self.solution.reformatDate("26th May 1960"), "1960-05-26")

if __name__ == '__main__':
    unittest.main()
