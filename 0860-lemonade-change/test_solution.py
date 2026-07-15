import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.lemonadeChange([5,5,5,10,20]))

    def test_example_2(self):
        self.assertFalse(self.solution.lemonadeChange([5,5,10,10,20]))

if __name__ == '__main__':
    unittest.main()
