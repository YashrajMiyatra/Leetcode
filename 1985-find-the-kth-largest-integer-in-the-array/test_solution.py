import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")

    def test_example_2(self):
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")

    def test_example_3(self):
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")

if __name__ == '__main__':
    unittest.main()
