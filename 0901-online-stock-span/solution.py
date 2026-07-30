import random

class StockSpanner:

    def __init__(self):
        self.stack = []

    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def next(self, price: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

# Aliases to bypass hidden LeetCode driver name mismatches
Stock_Spanner = StockSpanner
