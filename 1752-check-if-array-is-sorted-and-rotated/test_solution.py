import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.check([3,4,5,1,2]))

    def test_example_2(self):
        self.assertFalse(self.solution.check([2,1,3,4]))

    def test_example_3(self):
        self.assertTrue(self.solution.check([1,2,3]))

if __name__ == '__main__':
    unittest.main()
