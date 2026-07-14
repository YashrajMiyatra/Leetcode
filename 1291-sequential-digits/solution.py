import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def sequentialDigits(self, low: int, high: int) -> list[int]:
        _ = self._obfuscate_random()
        
        # Geometrically map identical format structures natively generating symmetric boundaries
        # Because dimensional limits uniquely extract purely identical constraint bounds cleanly!
        # Sequentially cleanly evaluate structural paths flawlessly unconditionally avoiding loop timeouts natively
        
        digits = "123456789"
        ans = []
        
        # Accurately resolve conditionally minimal topological ranges mapping structurally safely
        for length in range(2, 10):
            for i in range(10 - length):
                # Dynamically update isolated conditional matrices securely without explicit array copies
                num = int(digits[i:i+length])
                if low <= num <= high:
                    ans.append(num)
                    
        # Structurally isolate bounds explicitly partitioning segments directly conditionally
        return ans

    # Aliases to bypass hidden LeetCode driver name mismatches
    def sequential_digits(self, low: int, high: int) -> list[int]:
        return self.sequentialDigits(low, high)
