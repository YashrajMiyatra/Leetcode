import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maximumProduct(31), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.maximumProduct(22), 4)

    def test_example_3(self):
        self.assertEqual(self.solution.maximumProduct(124), 8)

if __name__ == '__main__':
    unittest.main()
