class Bank:
    """
    Hyper-optimized Simple Bank System.
    
    Optimizations:
    - __slots__: Completely eliminates the instance dictionary overhead to absolutely minimize memory.
    - Zero-allocation indexing: Instead of allocating a new array `[0] + balance` to 
      support 1-based indexing, we store a direct reference to the input list and mathematically 
      subtract 1 on the fly. This guarantees strict O(1) extra memory allocation.
    - Chained comparisons: Python evaluates `0 <= a1 < self.n` natively in C, providing 
      blazing fast bounds checking.
    """
    __slots__ = ['balance', 'n']

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Subtract 1 early to align with 0-based list indexing
        a1, a2 = account1 - 1, account2 - 1
        
        # O(1) chained comparison in C
        if 0 <= a1 < self.n and 0 <= a2 < self.n:
            if self.balance[a1] >= money:
                self.balance[a1] -= money
                self.balance[a2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        a = account - 1
        
        if 0 <= a < self.n:
            self.balance[a] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        a = account - 1
        
        if 0 <= a < self.n:
            if self.balance[a] >= money:
                self.balance[a] -= money
                return True
        return False
