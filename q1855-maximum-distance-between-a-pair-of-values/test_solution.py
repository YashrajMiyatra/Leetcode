import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.maxDistance([55,30,5,4,2], [100,20,10,10,5]), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.maxDistance([2,2,2], [10,10,1]), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.maxDistance([30,29,19,5], [25,25,25,25,25]), 2)

if __name__ == '__main__':
    unittest.main()
