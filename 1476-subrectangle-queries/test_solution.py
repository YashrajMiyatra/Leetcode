import unittest
from solution import SubrectangleQueries

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        sq = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
        self.assertEqual(sq.getValue(0, 2), 1)
        sq.updateSubrectangle(0, 0, 3, 2, 5)
        self.assertEqual(sq.getValue(0, 2), 5)
        self.assertEqual(sq.getValue(3, 1), 5)
        sq.updateSubrectangle(3, 0, 3, 2, 10)
        self.assertEqual(sq.getValue(3, 1), 10)
        self.assertEqual(sq.getValue(0, 2), 5)

    def test_example_2(self):
        sq = SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]])
        self.assertEqual(sq.getValue(0, 0), 1)
        sq.updateSubrectangle(0, 0, 2, 2, 100)
        self.assertEqual(sq.getValue(0, 0), 100)
        self.assertEqual(sq.getValue(2, 2), 100)
        sq.updateSubrectangle(1, 1, 2, 2, 20)
        self.assertEqual(sq.getValue(2, 2), 20)

if __name__ == '__main__':
    unittest.main()
