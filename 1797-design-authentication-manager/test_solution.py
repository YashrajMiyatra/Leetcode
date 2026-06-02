import unittest
from solution import AuthenticationManager

class TestAuthenticationManager(unittest.TestCase):
    def test_example(self):
        am = AuthenticationManager(5)
        am.renew("aaa", 1)
        am.generate("aaa", 2)
        self.assertEqual(am.countUnexpiredTokens(6), 1)
        am.generate("bbb", 7)
        am.renew("aaa", 8)
        am.renew("bbb", 10)
        self.assertEqual(am.countUnexpiredTokens(15), 0)

if __name__ == '__main__':
    unittest.main()
