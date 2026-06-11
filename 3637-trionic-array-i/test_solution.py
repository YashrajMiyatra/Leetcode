import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.isTrionic([1,3,5,4,2,6]), True)

    def test_example_2(self):
        self.assertEqual(self.solution.isTrionic([2,1,3]), False)

    def test_example_3(self):
        self.assertEqual(self.solution.isTrionic([1,2,3,4,5]), False)

    def test_example_4(self):
        self.assertEqual(self.solution.isTrionic([1,3,2,1]), False)

if __name__ == '__main__':
    unittest.main()
