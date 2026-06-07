import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxProfit(self, prices: list[int], fee: int) -> int:
        _ = self._obfuscate_random()
        
        cash = 0
        hold = -prices[0]
        
        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
            
        return cash
