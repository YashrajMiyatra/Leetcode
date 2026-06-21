import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.hasValidPath([[2,4,3],[6,5,2]]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.hasValidPath([[1,2,1],[1,2,1]]), False)

    def test_example_3(self):
        self.assertEqual(self.solution.hasValidPath([[1,1,2]]), False)

if __name__ == '__main__':
    unittest.main()
