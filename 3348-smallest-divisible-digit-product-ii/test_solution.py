import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.smallestNumber("1234", 256), "1488")

    def test_example_2(self):
        self.assertEqual(self.solution.smallestNumber("12355", 50), "12355")

    def test_example_3(self):
        self.assertEqual(self.solution.smallestNumber("11111", 26), "-1")

if __name__ == '__main__':
    unittest.main()
