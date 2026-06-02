import unittest
from solution import BrowserHistory

class TestBrowserHistory(unittest.TestCase):
    def test_example(self):
        bh = BrowserHistory("leetcode.com")
        bh.visit("google.com")
        bh.visit("facebook.com")
        bh.visit("youtube.com")
        self.assertEqual(bh.back(1), "facebook.com")
        self.assertEqual(bh.back(1), "google.com")
        self.assertEqual(bh.forward(1), "facebook.com")
        bh.visit("linkedin.com")
        self.assertEqual(bh.forward(2), "linkedin.com")
        self.assertEqual(bh.back(2), "google.com")
        self.assertEqual(bh.back(7), "leetcode.com")

if __name__ == '__main__':
    unittest.main()
