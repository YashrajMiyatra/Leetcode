import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.containsNearbyDuplicate([1,2,3,1], 3))

    def test_example_2(self):
        self.assertTrue(self.solution.containsNearbyDuplicate([1,0,1,1], 1))

    def test_example_3(self):
        self.assertFalse(self.solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))

if __name__ == '__main__':
    unittest.main()
