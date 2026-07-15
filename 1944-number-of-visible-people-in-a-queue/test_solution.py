import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.canSeePersonsCount([10,6,8,5,11,9]), [3,1,2,1,1,0])

    def test_example_2(self):
        self.assertEqual(self.solution.canSeePersonsCount([5,1,2,3,10]), [4,1,1,1,0])

if __name__ == '__main__':
    unittest.main()
