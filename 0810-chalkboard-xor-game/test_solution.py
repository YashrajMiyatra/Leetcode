import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.xorGame([1,1,2]), False)

    def test_example_2(self):
        self.assertEqual(self.solution.xorGame([0,1]), True)

    def test_example_3(self):
        self.assertEqual(self.solution.xorGame([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()
