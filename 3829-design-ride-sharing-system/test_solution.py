import unittest
from solution import RideSharingSystem

class TestRideSharingSystem(unittest.TestCase):
    def test_example_1(self):
        sys = RideSharingSystem()
        sys.addRider(3)
        sys.addDriver(2)
        sys.addRider(1)
        self.assertEqual(sys.matchDriverWithRider(), [2, 3])
        sys.addDriver(5)
        sys.cancelRider(3)
        self.assertEqual(sys.matchDriverWithRider(), [5, 1])
        self.assertEqual(sys.matchDriverWithRider(), [-1, -1])

    def test_example_2(self):
        sys = RideSharingSystem()
        sys.addRider(8)
        sys.addDriver(8)
        sys.addDriver(6)
        self.assertEqual(sys.matchDriverWithRider(), [8, 8])
        sys.addRider(2)
        sys.cancelRider(2)
        self.assertEqual(sys.matchDriverWithRider(), [-1, -1])

if __name__ == '__main__':
    unittest.main()
