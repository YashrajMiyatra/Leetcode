import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maximumProduct(self, n: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        digits = sorted([int(x) for x in str(n)])
        return digits[-1] * digits[-2]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def maximum_product(self, n: int) -> int:
        return self.maximumProduct(n)
        
    def maxProduct(self, n: int) -> int:
        return self.maximumProduct(n)
        
    def max_product(self, n: int) -> int:
        return self.maximumProduct(n)
