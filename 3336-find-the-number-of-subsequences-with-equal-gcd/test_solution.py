import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.subsequencePairCount([1,2,3,4]), 10)

    def test_example_2(self):
        self.assertEqual(self.solution.subsequencePairCount([10,20,30]), 2)

    def test_example_3(self):
        self.assertEqual(self.solution.subsequencePairCount([1,1,1,1]), 50)

if __name__ == '__main__':
    unittest.main()
