import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.concatenateAndMultiply("10203004", [[0,7],[1,3],[4,6]]), [12340, 4, 9])

    def test_example_2(self):
        self.assertEqual(self.solution.concatenateAndMultiply("1000", [[0,3],[1,1]]), [1, 0])

    def test_example_3(self):
        self.assertEqual(self.solution.concatenateAndMultiply("9876543210", [[0,9]]), [444444137])

if __name__ == '__main__':
    unittest.main()
