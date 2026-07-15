import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.bagOfTokensScore([100], 50), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.bagOfTokensScore([200,100], 150), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.bagOfTokensScore([100,200,300,400], 200), 2)

if __name__ == '__main__':
    unittest.main()
