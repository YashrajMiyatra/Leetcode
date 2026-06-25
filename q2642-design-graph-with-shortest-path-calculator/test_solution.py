import unittest
from solution import Graph

class TestSolution(unittest.TestCase):
    def test_example_1(self):
        g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
        self.assertEqual(g.shortestPath(3, 2), 6)
        self.assertEqual(g.shortestPath(0, 3), -1)
        g.addEdge([1, 3, 4])
        self.assertEqual(g.shortestPath(0, 3), 6)

if __name__ == '__main__':
    unittest.main()
