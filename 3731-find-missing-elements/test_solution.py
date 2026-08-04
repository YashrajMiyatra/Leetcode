import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMissingElements([1,4,2,5]), [3])

    def test_example_2(self):
        self.assertEqual(self.solution.findMissingElements([7,8,6,9]), [])

    def test_example_3(self):
        self.assertEqual(self.solution.findMissingElements([5,1]), [2,3,4])

if __name__ == '__main__':
    unittest.main()
