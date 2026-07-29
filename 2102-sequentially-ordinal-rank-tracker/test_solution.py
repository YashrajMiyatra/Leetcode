import unittest
from solution import SORTracker

class TestSORTracker(unittest.TestCase):
    def test_example_1(self):
        tracker = SORTracker()
        tracker.add("bradford", 2)
        tracker.add("branford", 3)
        self.assertEqual(tracker.get(), "branford")
        tracker.add("alps", 2)
        self.assertEqual(tracker.get(), "alps")
        tracker.add("orland", 2)
        self.assertEqual(tracker.get(), "bradford")
        tracker.add("orlando", 3)
        self.assertEqual(tracker.get(), "bradford")
        tracker.add("alpine", 2)
        self.assertEqual(tracker.get(), "bradford")
        self.assertEqual(tracker.get(), "orland")

if __name__ == '__main__':
    unittest.main()
