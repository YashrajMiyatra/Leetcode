import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_example(self):
        s = Solution(3, 1)
        
        # Total 3 elements: [0,0], [1,0], [2,0]
        # Flip all of them
        p1 = s.flip()
        p2 = s.flip()
        p3 = s.flip()
        
        # Ensure all unique
        t1 = tuple(p1)
        t2 = tuple(p2)
        t3 = tuple(p3)
        
        self.assertEqual(len({t1, t2, t3}), 3)
        
        valid_points = {(0, 0), (1, 0), (2, 0)}
        self.assertTrue(t1 in valid_points)
        self.assertTrue(t2 in valid_points)
        self.assertTrue(t3 in valid_points)
        
        # Reset and do it again
        s.reset()
        p4 = s.flip()
        self.assertTrue(tuple(p4) in valid_points)
        
    def test_massive_matrix(self):
        s = Solution(10000, 10000)
        p = s.flip()
        self.assertTrue(0 <= p[0] < 10000)
        self.assertTrue(0 <= p[1] < 10000)

if __name__ == '__main__':
    unittest.main()
