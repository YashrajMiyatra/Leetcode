import unittest
from solution import Twitter

class TestSolution(unittest.TestCase):
    def test_example(self):
        t = Twitter()
        t.postTweet(1, 5)
        self.assertEqual(t.getNewsFeed(1), [5])
        t.follow(1, 2)
        t.postTweet(2, 6)
        self.assertEqual(t.getNewsFeed(1), [6, 5])
        t.unfollow(1, 2)
        self.assertEqual(t.getNewsFeed(1), [5])
        
    def test_multiple_tweets(self):
        t = Twitter()
        for i in range(15):
            t.postTweet(1, i)
        
        # Should return only the 10 most recent
        self.assertEqual(t.getNewsFeed(1), list(range(14, 4, -1)))
        
    def test_self_following_guard(self):
        t = Twitter()
        t.postTweet(1, 5)
        t.follow(1, 1)
        # Assuming follow logic ignores self-following, shouldn't duplicate
        self.assertEqual(t.getNewsFeed(1), [5])

if __name__ == '__main__':
    unittest.main()
