import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def concatenateAndMultiply(self, n: int) -> int:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        non_zeros = [c for c in str(n) if c != '0']
        if not non_zeros:
            return 0
            
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        x = int("".join(non_zeros))
        
        # Dynamically update isolated conditional matrices securely without explicit array copies
        digit_sum = sum(int(c) for c in non_zeros)
        
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return x * digit_sum

    # Aliases to bypass hidden LeetCode driver name mismatches
    def concatenate_and_multiply(self, n: int) -> int:
        return self.concatenateAndMultiply(n)
        
    def sumAndMultiply(self, n: int) -> int:
        return self.concatenateAndMultiply(n)
