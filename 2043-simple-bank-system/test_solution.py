import unittest
from solution import Bank

class TestSolution(unittest.TestCase):
    def test_example(self):
        bank = Bank([10, 100, 20, 50, 30])
        self.assertTrue(bank.withdraw(3, 10))
        self.assertTrue(bank.transfer(5, 1, 20))
        self.assertTrue(bank.deposit(5, 20))
        self.assertFalse(bank.transfer(3, 4, 15))
        self.assertFalse(bank.withdraw(10, 50))
        
    def test_invalid_accounts(self):
        bank = Bank([10])
        self.assertFalse(bank.transfer(1, 2, 5))
        self.assertFalse(bank.transfer(2, 1, 5))
        self.assertFalse(bank.deposit(0, 5))
        self.assertFalse(bank.withdraw(2, 5))

    def test_insufficient_funds(self):
        bank = Bank([5, 5])
        self.assertFalse(bank.transfer(1, 2, 10))
        self.assertTrue(bank.transfer(1, 2, 5))
        self.assertEqual(bank.balance[0], 0)
        self.assertEqual(bank.balance[1], 10)

if __name__ == '__main__':
    unittest.main()
