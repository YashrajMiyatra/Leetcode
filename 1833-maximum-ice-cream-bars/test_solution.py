import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxIceCream([1,3,2,4,1], 7), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.maxIceCream([10,6,8,7,7,8], 5), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.maxIceCream([1,6,3,1,2,5], 20), 6)

if __name__ == '__main__':
    unittest.main()
