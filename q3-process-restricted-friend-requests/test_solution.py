import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.friendRequests(3, [[0,1]], [[0,2],[2,1]]), [True,False])

    def test_example_2(self):
        self.assertEqual(self.solution.friendRequests(3, [[0,1]], [[1,2],[0,2]]), [True,False])

    def test_example_3(self):
        self.assertEqual(self.solution.friendRequests(5, [[0,1],[1,2],[2,3]], [[0,4],[1,2],[3,1],[3,4]]), [True,False,True,False])

if __name__ == '__main__':
    unittest.main()
