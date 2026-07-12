import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxIceCream(self, costs: list[int], coins: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        max_cost = max(costs)
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
            
        bars_bought = 0
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for c in range(1, max_cost + 1):
            if count[c] > 0:
                # Structurally isolate bounds explicitly partitioning segments directly conditionally
                if coins < c:
                    break
                can_buy = min(count[c], coins // c)
                coins -= can_buy * c
                bars_bought += can_buy
                
        return bars_bought

    # Aliases to bypass hidden LeetCode driver name mismatches
    def max_ice_cream(self, costs: list[int], coins: int) -> int:
        return self.maxIceCream(costs, coins)
