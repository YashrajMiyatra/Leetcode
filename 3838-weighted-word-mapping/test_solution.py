import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.getMappedString(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]), "rij")

    def test_example_2(self):
        self.assertEqual(self.solution.getMappedString(["a","b","c"], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), "yyy")

    def test_example_3(self):
        self.assertEqual(self.solution.getMappedString(["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]), "g")

if __name__ == '__main__':
    unittest.main()
