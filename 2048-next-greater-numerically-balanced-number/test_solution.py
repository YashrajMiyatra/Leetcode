import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.nextBeautifulNumber(1), 22)

    def test_example_2(self):
        self.assertEqual(self.solution.nextBeautifulNumber(1000), 1333)

    def test_example_3(self):
        self.assertEqual(self.solution.nextBeautifulNumber(3000), 3133)

if __name__ == '__main__':
    unittest.main()
