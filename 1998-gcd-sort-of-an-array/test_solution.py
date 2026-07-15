import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.gcdSort([7,21,3]))

    def test_example_2(self):
        self.assertFalse(self.solution.gcdSort([5,2,6,2]))

    def test_example_3(self):
        self.assertTrue(self.solution.gcdSort([10,5,9,3,15]))

if __name__ == '__main__':
    unittest.main()
