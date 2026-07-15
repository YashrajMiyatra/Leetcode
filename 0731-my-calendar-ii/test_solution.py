import unittest
from solution import MyCalendarTwo

class TestMyCalendarTwo(unittest.TestCase):
    def test_example_1(self):
        cal = MyCalendarTwo()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(50, 60))
        self.assertTrue(cal.book(10, 40))
        self.assertFalse(cal.book(5, 15))
        self.assertTrue(cal.book(5, 10))
        self.assertTrue(cal.book(25, 55))

if __name__ == '__main__':
    unittest.main()
