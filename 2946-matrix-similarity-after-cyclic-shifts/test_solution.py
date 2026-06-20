import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.areSimilar([[1,2,3],[4,5,6],[7,8,9]], 4))

    def test_example_2(self):
        self.assertTrue(self.solution.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2))

    def test_example_3(self):
        self.assertTrue(self.solution.areSimilar([[2,2],[2,2]], 3))

if __name__ == '__main__':
    unittest.main()
